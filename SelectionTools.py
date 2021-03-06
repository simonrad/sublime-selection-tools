import sublime, sublime_plugin


class MultiQuickFindAllCommand(sublime_plugin.TextCommand):
    """
    Sublime has a very helpful "Quick Find All" command (ctrl-command-G on Mac), which selects all occurrences of the currently selected string.
    However, it doesn't work with multiple selections (i.e. if I wanted to find all occurrences of either "strA" or "strB").
    This command performs the same behavior, but supports multiple initial selections.
    """
    def run(self, edit):
        selected_strings = [self.view.substr(region) for region in self.view.sel()]
        selected_strings = [string for string in selected_strings if string]
        for string in selected_strings:
            for region in self.view.find_all(string, sublime.LITERAL):
                self.view.sel().add(region)


class AlignIndentationCommand(sublime_plugin.TextCommand):
    """
    Given a multi-line selection, all lines except the first will be reindented to
    the character column of the beginning of the selection.

    This is convenient when used in conjunction with the command "Expand Selection to Brackets",
    which is shift-ctrl-m on Mac. If you have a function call with the arguments on several lines
    for example, this will indent it flush with the opening bracket.

    Currently this always uses spaces to do the indentation.
    Using tabs would be a bit weird because we'd have to mix tabs and spaces in the same line.
    """
    def run(self, edit):
        selected_regions = self.view.sel()
        to_replace = [] # List of (region, replacement_str) pairs.

        for region in selected_regions:
            # Calculate the indentation (i.e. the column of the start of the selection), even when tabs are present.
            begin_row, begin_col = self.view.rowcol(region.begin())
            begin_line = self.view.substr(self.view.line(region.begin()))
            indent = 0
            tab_size = self.view.settings().get('tab_size', 4)
            for col in range(begin_col):
                if begin_line[col] == '\t':
                    # Advance to the next tab stop.
                    indent = (indent / tab_size + 1) * tab_size
                else:
                    indent += 1
            indent = ' ' * indent

            # Record the regions that we want to replace with `indent`.
            lines = self.view.lines(region)
            for line in lines[1:]:
                # Take all the leading whitespace of the line.
                num_leading_whitespace_chars = 0
                for c in self.view.substr(line):
                    if c.isspace():
                        num_leading_whitespace_chars += 1
                    else:
                        break
                whitespace_region = sublime.Region(line.begin(), line.begin() + num_leading_whitespace_chars)
                to_replace.append((whitespace_region, indent))

        # Replace the regions starting from the last one, so that we do not mess up the indices.
        to_replace.sort(key = (lambda pair: pair[0].begin()), reverse = True)

        edit = self.view.begin_edit()
        for region, indent in to_replace:
            self.view.replace(edit, region, indent)
        self.view.end_edit(edit)


class ReverseSelectionDirectionCommand(sublime_plugin.TextCommand):
    """
    Toggles the cursor being at the front or the back of the selection.
    """
    def run(self, edit):
        # Decide direction to set.
        # Normally we set them to be backward (cursor at the start).
        # But if any of them are already backward, then we set them all to be forward.
        forward = False
        for s in self.view.sel():
            if s.b < s.a:
                forward = True

        # Compute the new selections.
        new_sels = []
        for s in self.view.sel():
            a = min(s.a, s.b)
            b = max(s.a, s.b)
            if not forward:
                a, b = b, a
            new_sels.append(sublime.Region(a, b))

        # Set the new selections.
        self.view.sel().clear()
        for s in new_sels:
            self.view.sel().add(s)


class ShortenSelectionCommand(sublime_plugin.TextCommand):
    """
    Shortens the selection by one character both at the front and the back.

    This can be useful in conjunction with expanding the selection to brackets or quotes.
    Sometimes you don't want the quotes, or the extra lines.
    """
    def run(self, edit):
        # Compute the new selections.
        new_sels = []
        for s in self.view.sel():
            a = s.a
            b = s.b
            if abs(a - b) >= 2:
                direction = 1 if a < b else -1
                a += direction
                b -= direction
            else:
                a = b = min(a, b)
            new_sels.append(sublime.Region(a, b))

        # Set the new selections.
        self.view.sel().clear()
        for s in new_sels:
            self.view.sel().add(s)

