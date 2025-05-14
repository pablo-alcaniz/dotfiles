#!/bin/bash

#????
prime-offload

#pantalla
/bin/python /home/pablo/.config/qtile/check_monitor.py

#volumen
volctl &
#google drive
insync start &
#teclado 
setxkbmap es
#compositor de escritorio
picom -b  &
#iconos del sistema
udiskie -t &
nm-applet &
blueman-applet &

caffeine &
#aplicaciones
optimus-manager &
optimus-manager-qt &


#fondo de pantalla
nitrogen --restore  &
