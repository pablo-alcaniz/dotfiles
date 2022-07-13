#!/bin/bash

#compositor de escritorio
picom --experimental-backends &


#iconos del sistema
udiskie -t &
nm-applet &
blueman-applet &
volctl &

#aplicaciones
python3 /opt/thefanclub/overgrive/overgrive &
optimus-manager &
optimus-manager-qt &

#fondo de pantalla
nitrogen --restore  &

#openfrezer
#python3 /home/pablo/programas/OpenFreezer/indicator.py >/dev/null 2>&1 & exit

#synaptics
synclient VertScrollDelta=-60 &
synclient TapButton1=1 &
synclient PalmDetect=1 & 
synclient PalmMinWidth=8 & 
synclient PalmMinZ=300 &

#dock 
plank &
