import os
os.system("clear")
print("Welcome to the Infinite Reboot Setup!")
print("Please choose an option")
print("[(1) Less Destrictive] [(2) Most Destructive]")
str = input("")
if str == "1":
    option = 1
else:
    if str == "2":
        option = 2
os.system("clear")
if option == 1:
    print("Installing...")
    os.system("cp .oneminuteshutdown.desktop /etc/xdg/autostart/oneminuteshutdown.desktop")
if option == 2:
    print("Installing...")
    os.system("cp .autoshutdown.desktop /etc/xdg/autostart/autoshutdown.desktop")
if option == 1 or option == 2:
    print("Installed. Would You Like To Reboot? (y/n)")
    reboot = input("")
    if reboot == "y":
        os.system("shutdown -r -t 0")