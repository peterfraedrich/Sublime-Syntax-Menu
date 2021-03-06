# Sublime Syntax Menu
A quick-switcher for syntaxes that lets you set a hotkey combination. Ripped the idea from Atom.

![alt tag](https://dl.dropboxusercontent.com/u/90638532/syntax-menu.gif)

## Hotkey Setup
To set up the switcher with a hotkey, add the command `open_syntax_menu` to your `Key Bindings - user` file. 
```json
[
  { "keys" : ["ctrl+shift+l"], "command" : "open_syntax_menu" }
]
```

### Known Issues
* Sublime's API doesn't provide a good way to switch syntax on the fly and relies on the syntax file name/path. This causes problems when switching to a syntax that doesn't share a common name between the folder and syntax file name. In these cases it will defauly to plain text.
* Right now only works 100% of the time with the standard syntaxes and syntaxes that share a folder/file name (ie, `Packages/INI/INI.sublime-syntax`).
