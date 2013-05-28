sublime-selection-tools
=======================

Some helpful commands for Sublime Text 2.

- Multi Quick Find All
    - Given some initially selected strings, selects all occurrances of any of those strings.
    - Like Sublime's built-in "Quick Find All" command, but works with multiple initial selections.

- Reverse Selection Direction
    - Toggles the cursor being at the front or the back of the selection.

- Align Indentation
    - Given a multi-line selection, all lines except the first will be reindented to the character column of the beginning of the selection.
    - Thus it allows you to quickly indent a block to an exact column.
    - Handy when used together with the command "Expand Selection to Brackets".
    - [See screenshot](https://raw.github.com/wiki/simonrad/sublime-selection-tools/AlignIndentation.png)

- Shorten Selection
    - Shortens the selection by one character both at the front and the back.
    - This can be useful when expanding the selection to quotes or brackets. Sometimes you don't want to select the quotes, or the lines containing the brackets.
