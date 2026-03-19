# VoHID
Yet another thing for typing.
# Setupping
1. Ensure that you're using Linux
```
$ uname
```
If the output is not "Linux" or if your MS Windows system yaps on this command, you're not using Linux. \
WSL also won't work because it's just a virtual machine that doesn't have full access to devices. \
2. Install requirements \
If you prefer pip more than apt, find the command by yourself.
```
# apt install python3-pygame python3-evdev
```
3. You have to have the permissions \
Also ensure that you have raw access to "/dev/input/event*".
```
$ ls -ll /dev/input/event0
crw-rw---- 1 root input 13, 64 Mar 19 10:04 /dev/input/event0
```
If you're not the owner and you're not in the group, add yourself to the group and relog-in.
```
# usermod -aG <group> <you>
```
# Run
```
$ python3 vohid.py
```
