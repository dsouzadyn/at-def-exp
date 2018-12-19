#!/bin/sh
rm getroot
gcc -Os -Wall getroot.c -ogetroot
strip --strip-unneeded getroot
 
sudo chown root.root getroot
sudo chmod +s getroot
