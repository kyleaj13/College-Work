import webbrowser
import subprocess


def print_options():
    print("")
    print("****Please choose one of the following****")
    print(" p - print options")
    print(" w - weekly maintenance")
    print(" m - monthly maintenance")
    print(" y - yearly maintenance")
    print(" k - peripheral maintenance")
    print(" ? - why is maintenance important?")
    print(" q - quit the program")


print("---- WARNING ----")
print("This program will open things for you, don't panic!")
print("!! Some of these functions will not work unless you are on the newest version of windows !!")
print_options()
print("****Please use Y or N when using the program****")
choice = input("Option: ").lower()


def weekly_m():
    print("")
    print("****Weekly****")
    weekly_list()
    w_choice = input("Option: ").lower()
    if w_choice == "b":
        backup()
    elif w_choice == "d":
        subprocess.call(["C:\Windows\system32\cleanmgr.exe"])
    elif w_choice == "v":
        subprocess.call(["C:\Program Files\Windows Defender\MSASCui.exe"])
    else:
        print("")


def monthly_m():
    print("")
    print("****Monthly****")
    monthly_list()
    m_choice = input("Option: ").lower()
    if m_choice == "d":

        subprocess.call(["C:\Windows\system32\dfrgui.exe"])
        print("")
        print("If the dialog box doesn't open, follow the instructions below")
        print("Press windows key + R")
        print("Type dfrgui.exe in the dialogue box")
        print("Select the drive you want to defragment and click optimize")
    elif m_choice == "u":
        print("")
        print("Open settings")
        print("Click on update and security")
        print("Click windows update")
        print("Select check for updates")
        print("If there are any updates available, they will now automatically download")
    elif m_choice == "a":
        webbrowser.open("ms-settings:windowsupdate")


def yearly_m():
    print("****Yearly****")
    pc()


def peripheral_m():
    print("****Peripheral****")
    kb_test = input("Would you like to test your keyboard? ").lower()
    m_test = input("Would you like to test your mouse? ").lower()
    if kb_test == "y" and m_test == "y":
        keyboard()
        mouse()
    elif kb_test == "y" and m_test == "n":
        keyboard()
    elif kb_test == "n" and m_test == "y":
        mouse()
    else:
        print("")


def keyboard():
    webbrowser.open("http://www.keyboardtester.com/")
    print("I have opened a utility that will allow you to test your keyboard!")
    kbworking = input("Is your keyboard working correctly? ").lower()
    if kbworking == "y":
        print("That's great!")
    elif kbworking == "n":
        print("")
        print("Unplug your keyboard from your computer")
        print("Tilt the keyboard up and shake to remove any loose debris")
        print("Cotton swab with rubbing alcohol to clean between the keys")
        print("A cloth with rubbing alcohol to clean the tops of the keys")
        print("Please allow time for the keyboard to dry off before using")
        print("")


def mouse():
    webbrowser.open("http://unixpapa.com/js/testmouse.html")
    print("I have opened a utility that will allow you to test your mouse!")
    mworking = input("Is your mouse working correctly? ").lower()
    if mworking == "y":
        print("That's great!")
    elif mworking == "n":
        print("")
        print("Unplug your mouse from your computer")
        print("Clean the top and under surface of your mouse with a damp cloth")
        print("Use rubbing alcohol or mild soap for stubborn grease")
        print("If you need to remove dust from the sensor, use a cotton swab")


def pc_inside():
    # clean = input("Have you cleaned the inside of your computer in the last 6 months? ").lower()
    # if clean == "y":
        # print("Great!")
    # elif clean == "n":
    webbrowser.open("https://www.howtogeek.com/72716/how-to-thoroughly-clean-your-dirty-desktop-computer/")
    air = input("Do you have your own compressed air? ").lower()
    if air == "y":
        print("Great!")
    elif air == "n":
        webbrowser.open("https://www.amazon.co.uk/Electronics-Compressed-Air-Dusters/b?ie=UTF8&node=200927031")


def pc_outside():
    print("")
    print("If you have glass in your case a regular glass cleaner will work fine")
    print("Use a damp cloth to wipe down the rest of your case")
    print("Be careful not to get any water in your computers ports!")


def pc():
    pc_cleaning = input("Have you cleaned your computer in the last 6 months? ").lower()
    if pc_cleaning == "y":
        print("")
        print("You're probably fine")
    elif pc_cleaning == "n":
        in_out = input("Would you like to clean the inside or outside of your PC? ").lower()
        if in_out == "inside":
            pc_inside()
        elif in_out == "outside":
            pc_outside()
        else:
            print("")
    else:
        print("Sorry, that input is not valid, please try again!")


def weekly_list():
    print("****Please choose one of the following****")
    print(" b - backup")
    print(" d - disk cleanup")
    print(" v - virus scan")


def monthly_list():
    print("****Please choose one of the following****")
    print(" d - disk defragmenter")
    print(" u - windows updates (manual)")
    print(" a - windows updates (automatic)")


def backup():
    print("")
    print("Open control panel")
    print("Click on system and security")
    print("Click on backup and restore")
    print("Click set up backup in the top right")
    print("Now follow the wizard")


def why():
    print("")
    print("Why is maintenance important?")
    print("- Keep your computer running well for much longer")
    print("- Keep your data protected from viruses and hackers")
    print("- Save you money in the long run by not having to replace parts")


while choice != "q":

    if choice == "w":
        weekly_m()
        
    elif choice == "m":
        monthly_m()

    elif choice == "y":
        yearly_m()
        
    elif choice == "k":
        peripheral_m()

    elif choice == "?":
        why()

    elif choice == "p":
        print_options()
        choice = input("Option: ")

    else:
        print("An invalid choice has been entered, please try again")

    print_options()
    choice = input("Option: ")
