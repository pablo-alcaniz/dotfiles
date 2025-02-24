# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from curses.panel import top_panel
from operator import truediv
from libqtile import bar, layout, widget, hook 
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
import pulsectl_asyncio
import pulsectl


mod = "mod4"
terminal = guess_terminal()

color_iconos_activos = "#FFFFFF"
color_fg = "#282a36"
color_bg = "#282a36"
metodo_resalte = "block"  
color_resalte = "#FF8F00"
color_systray = "#242424"

tamaño_barra = 40
color_barra = "#0B0B0B"
tamaño_fuente_barra = 18


fuente_predeterminada = "Noto Sans Mono"


# funciones 

def fc_separador():
    return widget.Sep(
    linewidth = 2,
    padding = 30,
    foreground = color_resalte,
    background = color_barra
    )

def fc_separador_trans():
    return widget.Sep(
    linewidth = 1,
    padding = 20,
    foreground = color_barra,
    background = color_barra
    )

def longNameParse(text): 
    for string in ["Google Chrome", "Visual Studio Code", "MATLAB", "Simulink", "Edge", "Firefox"]: #Add any other apps that have long names here
        if string in text:
            text = string
        else:
            text = text
    return text
         



keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "z", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),


    ###############################   SHORTCUTS    ####################################### 

    #control de volumen 
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    #control de brillo
    Key([], "XF86MonBrightnessUp", lazy.spawn("blight set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("blight set -5%")),
    Key([mod], "End", lazy.spawn("blight set 0")),
    Key([mod], "Next", lazy.spawn("blight set 512")),
    
    #lanzar terminal 
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    #lanzar menu rofi 
    Key([mod], "q", lazy.spawn("rofi -show drun -font 'Noto Fonts 45'")),

    #lanzar edge 
    Key([mod], "m", lazy.spawn("firefox")),

    #lanzar thunar
    Key([mod], "t", lazy.spawn("nautilus")),

    #abrir code
    Key([mod], "c", lazy.spawn("code")),

    #mover hacia el grupo de la derecha 
    Key([mod, "mod1"], "Right", lazy.screen.next_group()),

    #mover hacia el grupo de la izquierda 
    Key([mod, "mod1"], "Left", lazy.screen.prev_group()),

    #apagar el equipo
    Key([mod, "mod1"], "BackSpace", lazy.spawn("poweroff")),


#######################################################################################################################33

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]


grupo1 = " 1_main "  
grupo2 = " 2_web " 
grupo3 = " 3_dev " 
grupo4 = " 4_term " 
grupo5 = " 5_git " 
grupo6 = " 6 " 
grupo7 = " 7 " 
grupo8 = " 8 " 
grupo9 = " 9 " 



groups = [
    Group(grupo1),
    Group(grupo2),
    Group(grupo3),
    Group(grupo4),
    Group(grupo5),
    Group(grupo6),
    Group(grupo7),
    Group(grupo8),
    Group(grupo9)
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                "1",
                lazy.group[grupo1].toscreen(),
                desc="Switch to group {}".format(grupo1),
            ),
            Key(
                [mod],
                "2",
                lazy.group[grupo2].toscreen(),
                desc="Switch to group {}".format(grupo2),
            ),
            Key(
                [mod],
                "3",
                lazy.group[grupo3].toscreen(),
                desc="Switch to group {}".format(grupo3),
            ),
            Key(
                [mod],
                "4",
                lazy.group[grupo4].toscreen(),
                desc="Switch to group {}".format(grupo4),
            ),
            Key(
                [mod],
                "5",
                lazy.group[grupo5].toscreen(),
                desc="Switch to group {}".format(grupo5),
            ),
            Key(
                [mod],
                "6",
                lazy.group[grupo6].toscreen(),
                desc="Switch to group {}".format(grupo6),
            ),
            Key(
                [mod],
                "7",
                lazy.group[grupo7].toscreen(),
                desc="Switch to group {}".format(grupo7),
            ),
            Key(
                [mod],
                "8",
                lazy.group[grupo8].toscreen(),
                desc="Switch to group {}".format(grupo8),
            ),
            Key(
                [mod],
                "9",
                lazy.group[grupo9].toscreen(),
                desc="Switch to group {}".format(grupo9),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                "1",
                lazy.window.togroup(grupo1, switch_group=False),
                desc="Switch to & move focused window to group {}".format(grupo1),
            ),
            Key(
                [mod, "shift"],
                "2",
                lazy.window.togroup(grupo2, switch_group=False),
                desc="Switch to & move focused window to group {}".format(grupo2),
            ),
            Key(
                [mod, "shift"],
                "3",
                lazy.window.togroup(grupo3, switch_group=False),
                desc="Switch to & move focused window to group {}".format(grupo3),
            ),
            Key(
                [mod, "shift"],
                "4",
                lazy.window.togroup(grupo4, switch_group=False),
                desc="Switch to & move focused window to group {}".format(grupo4),
            ),
            Key(
                [mod, "shift"],
                "5",
                lazy.window.togroup(grupo5, switch_group=False),
                desc="Switch to & move focused window to group {}".format(grupo5),
            ),
            Key(
                [mod, "shift"],
                "6",
                lazy.window.togroup(grupo6, switch_group=False),
                desc="Switch to & move focused window to group {}".format(grupo6),
            ),
            Key(
                [mod, "shift"],
                "7",
                lazy.window.togroup(grupo7, switch_group=False),
                desc="Switch to & move focused window to group {}".format(grupo7),
            ),
            Key(
                [mod, "shift"],
                "8",
                lazy.window.togroup(grupo8, switch_group=False),
                desc="Switch to & move focused window to group {}".format(grupo8),
            ),
            Key(
                [mod, "shift"],
                "9",
                lazy.window.togroup(grupo9, switch_group=False),
                desc="Switch to & move focused window to group {}".format(grupo9),
            ),
        ]
    )

layouts = [
    
    layout.Columns(
        border_focus = color_resalte,
        border_on_single = False, 
        border_normal = color_barra,
        border_width = 2,
        margin_on_single = 20,
        margin = 20,
        ),
    layout.Max(),
]

widget_defaults = dict(
    font = fuente_predeterminada,
    fontsize = tamaño_fuente_barra,
    padding = 1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                fc_separador_trans(),                    
                widget.GroupBox(
                    fontsize = 20,
                    active = color_iconos_activos,
                    borderwidth = 0,
                    disable_drag = True,
                    highlight_method = metodo_resalte,
                    margin_x = 0,
                    margin_y = 4,
                    padding_y = 0, 
                    this_current_screen_border = color_resalte
                ),
                fc_separador(),
                widget.WindowName(
                    parse_text = longNameParse,
                ),
                widget.Systray(
                    padding = 15,
                    icon_size = 28,
                    background = color_systray
                ),
                fc_separador(),
                widget.TextBox(text='VOL: '),
                widget.PulseVolume(
                    limit_max_volume = True
                ),
                fc_separador(),
                widget.TextBox(text='BRIGHT:'),
                widget.Backlight(
                    backlight_name = 'intel_backlight',
                    brightness_file = 'brightness'
                ),
                fc_separador(),                
                widget.Battery(
                    format = 'BAT: {percent:2.0%}',
                ),
                fc_separador(),
                widget.Clock(format="%H:%M %A %d-%m-%Y"),
                widget.Sep(
                    linewidth = 2,
                    padding = 3,
                    foreground = color_barra,
                    background = color_barra
                )
            ],
            size = tamaño_barra, 
            background = color_barra,
            border_width=[0, 0, 0, 0],
            opacity=1,
            margin=[10, 20, -10, 20],
    ))
]


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
follow_mouse_focus = "click_or_drag_only"

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call(home)
