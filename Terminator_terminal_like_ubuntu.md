## To change background color and font color change:

`nano ~/.config/terminator/config`

```
[global_config]
  title_transmit_bg_color = "#e01b24"
  case_sensitive = False
[keybindings]
[profiles]
  [[default]]
    background_color = "#380c2a"
    cursor_color = "#aaaaaa"
    foreground_color = "#ffffff"
    copy_on_selection = True
  [[development]]
    cursor_color = "#aaaaaa"
[layouts]
  [[default]]
    [[[window0]]]
      type = Window
      parent = ""
    [[[child1]]]
      type = Terminal
      parent = window0
[plugins]
```
