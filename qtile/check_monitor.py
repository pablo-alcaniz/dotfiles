import subprocess


#take de xrandr output 
def get_xrandr_output():
    return subprocess.run(["xrandr"], capture_output=True, text=True).stdout

#if second monitor is connected --> True; else ---> False
def multimonitor_bool():
    xrandr_output = get_xrandr_output()
    if "DP-2 connected" in xrandr_output: 
        return True
    else:
        return False

#set up the monitors
def main(): 
    status = multimonitor_bool()
    if status == True:
        print("Monitor DP-2 detectado. Configurando a 165 Hz...")
        subprocess.run(["xrandr", "--output", "DP-2","--primary", "--mode", "2560x1440", "--rate", "164.83"])
        subprocess.run(["xrandr", "--output", "eDP-1-1", "--noprimary", "--right-of", "DP-2", "--mode", "1920x1080", "--rate", "60.00"])
    if status == False:
        print("Monitor DP-2 no detectado. Aplicando configuración alternativa...")
        subprocess.run(["xrandr", "--output", "eDP-1-1", "--mode", "1920x1080", "--rate", "240.00"])


if __name__ == "__main__":
    main()       
