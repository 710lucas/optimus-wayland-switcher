# Optimus wayland switcher

This is a simple python script to change the conf file when using Nvidia cards with gdm.

You can choose to enable wayland options and use integrated graphics, or to use X11 and use Nvidia graphics.

## How to use

I recommend to do this on a tty, since you'll be forced to log out of your gnome session. Using a tty makes sure to keep the commands in the terminal, so you can use them even after the logou

Run the main.py file as sudo
`sudo python main.py`

Then run the commands that the program will give you. If you're not using a tty, make sure to remember them, because you'll be logged out.

If changing from Nvidia to integrated graphics, reboot.
