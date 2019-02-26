After boot detection failed or only black screen on ubuntu
-----------------------------------------------------------

Link: https://askubuntu.com/questions/162075/my-computer-boots-to-a-black-screen-what-options-do-i-have-to-fix-it

Edit grub file using recovery terminal:
---------------------------------------
    sudo nano /etc/default/grub

Modify Line in grub:
--------------------
    GRUB_CMDLINE_LINUX_DEFAULT="quite splash"
    
    to
    
    GRUB_CMDLINE_LINUX_DEFAULT=""

save grub and close
