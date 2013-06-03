Sublime SelectionTools
======================

Some helpful commands for Sublime Text 2.

### Commands

- Multi Quick Find All
    - Given some initially selected strings, selects all occurrances of any of those strings.
    - Like Sublime's built-in "Quick Find All" command, but works with multiple initial selections.

- Reverse Selection Direction
    - Toggles the cursor being at the front or the back of the selection.

- Align Indentation
    - Given a multi-line selection, all lines except the first will be reindented to the character column of the beginning of the selection.
    - You can quickly indent a block to an exact column.
    - Handy when used together with the command "Expand Selection to Brackets".
    - [See screenshot](https://raw.github.com/wiki/simonrad/sublime-selection-tools/AlignIndentation.png)

- Shorten Selection
    - Shortens the selection by one character both at the front and the back.
    - This can be useful when expanding the selection to quotes or brackets. Sometimes you don't want to select the quotes, or the lines containing the brackets.


### To install

#### Via PackageControl

If you have the [PackageControl](http://wbond.net/sublime_packages/package_control) plugin installed, you can use that to install `SelectionTools`.

Just type `cmd-shift-p` (`ctrl-shift-p` on win/linux) to bring up the command pallate then type `install` and pick `Package Control: Install Package` from the dropdown.

Then type `SelectionTools` and choose the SelectionTools plugin from the dropdown.  Hit `enter` and it will install.


#### Manually

Manual installation should be as easy as cloning this git repository into your Sublime `Packages` directory.  On OSX:

    cd ~/Application\ Support/Sublime\ Text\ 2/Packages
    git clone git://github.com/simonrad/sublime-selection-tools.git SelectionTools


### To use

Add your desired key bindings to your User sublime-keymap file. An example keymap file is provided.
