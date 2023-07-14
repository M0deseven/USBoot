# USBoot
Simple cli based bootable USB creator

Uses bash utilities mkfs and dd to format a drive and write an iso file directly to it.
This a functional albeit unpolished usb creation tool. 

I will probably change the dev_umount() function to have a more straightforward way of getting logical drive strings. 

This does not support creating a Windows ISO. That will require Ventoy.

I plan to remake this from the ground up with a more polished UX, Windows USB support and perhaps even a Tkinter based gui.
