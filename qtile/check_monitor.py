import subprocess

# Obtener la salida de xrandr
xrandr_output = subprocess.run(["xrandr"], capture_output=True, text=True).stdout
# Comprobar si DP-2 está conectado
if "DP-2 connected" in xrandr_output:
    print("Monitor DP-2 detectado. Configurando a 165 Hz...")
    subprocess.run(["xrandr", "--output", "DP-2", "--mode", "2560x1440", "--rate", "164.83"])
else:
    print("Monitor DP-2 no detectado. Aplicando configuración alternativa...")
    subprocess.run(["xrandr", "--output", "eDP-1-1", "--mode", "1920x1080", "--rate", "240.00"])
