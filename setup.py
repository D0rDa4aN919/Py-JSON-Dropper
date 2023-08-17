import subprocess

from vars import *

def statement(pip, google):
    if pip == True and google == True:
        print(f"""
{color['BOLD']}{color['GREEN']}The machine is setup for the tool...
You are ready to go!!
Execute the create_json.py...{color['RESET']}""")
    elif pip == True and google == False:
        print(f"""
{color['BOLD']}{color['GREEN']}The machine is setup with requirements.txt...
{color['RED']}You need to fix the chrome installation!!{color['GREEN']}
After fixing the installation execute the create_json.py...{color['RESET']}""")
    elif pip == False and google == True:
        print(f"""
{color['BOLD']}{color['GREEN']}The machine is setup with google chrome...
{color['RED']}You need to fix the requirements.txt installation!!{color['GREEN']}
After fixing the installation execute the create_json.py...{color['RESET']}""")
    elif pip == False and google == False:
        print(f"""{color['BOLD']}{color['RED']}
You will need you to preform the process of installing the requirements.txt and google chrome
After fixing the installation execute the create_json.py...{color['RESET']}""")

def Linux():
    # Define the path to the .deb file
    deb_file_path = "drivers/google-chrome-stable_current_amd64.deb"
    # Define the command to check if 'google-chrome' is in PATH
    def is_google_chrome_installed():
        global final_check
        try:
            subprocess.run(["google-chrome", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except FileNotFoundError:
            return False

    # Define the setup function
    def setup_package_linux():
        final_check_google = False
        final_check_pip = False
        # Install the .deb file using 'dpkg'
        subprocess.run(["sudo", "dpkg", "-i", deb_file_path], stdout=subprocess.DEVNULL)

        # Check if 'google-chrome' is in PATH
        if is_google_chrome_installed():
            final_check_google = True
            print(f"{color['BOLD']}{color['GREEN']}Google Chrome is installed and accessible in PATH.{color['RESET']}")
        else:
            print(f"""{color['BOLD']}{color['GREEN']}Google Chrome is not installed or not accessible in PATH
Need to install manually the google chrome
1) sudo dpkg -i {deb_file_path}
2) google-chrome --version
3) If the command are execute without error the google-chrome is working.{color['RESET']}""")

        # Install packages from requirements.txt
        requirements_file = "requirements.txt"
        try:
            subprocess.run(["pip", "install", "-r", requirements_file], stdout=subprocess.DEVNULL)
            print(f"{color['BOLD']}{color['GREEN']}Required packages installed successfully.{color['RESET']}")
            final_check_pip = True
        except Exception as e:
            print(f"""{color['BOLD']}{color['RED']}An error occurred while installing packages: {e}
1) pip install -r {requirements_file}
2) Check that all of the packages in requirements.txt are installed.{color['RESET']}""")
        statement(final_check_google,final_check_pip)

    setup_package_linux()

def Windows():
    exe_file_path = ".\\drivers\\firefox_installer.exe"
    def is_firefox_installed():
        try:
            subprocess.run(["firefox", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except FileNotFoundError:
            return False

    # Define the setup function
    def setup_package_windows():
        final_check_firefox = False
        final_check_pip = False
        # Install the .exe file for Firefox
        subprocess.run([exe_file_path, "/silent"], stdout=subprocess.DEVNULL)

        # Check if 'firefox' is in PATH
        if is_firefox_installed():
            final_check_firefox = True
            print(f"{color['BOLD']}{color['GREEN']}Firefox is installed and accessible in PATH.{color['RESET']}")
        else:
            print(f"""{color['BOLD']}{color['RED']}Firefox is not installed or not accessible in PATH.
You need to manually install Firefox.{color['RESET']}""")

        # Install packages from requirements.txt
        requirements_file = "requirements.txt"
        try:
            subprocess.run(["pip", "install", "-r", requirements_file], stdout=subprocess.DEVNULL)
            print(f"{color['BOLD']}{color['GREEN']}Required packages installed successfully.{color['RESET']}")
            final_check_pip = True
        except Exception as e:
            print(f"""{color['BOLD']}{color['RED']}An error occurred while installing packages: {e}")
Try running: pip install -r {requirements_file}")
print("Check that all of the packages in requirements.txt are installed.{color['RESET']}""")

        statement(final_check_pip, final_check_firefox)
    setup_package_windows()

# Run the setup function
if __name__ == "__main__":
    if LIN:
        if lin_user():
            Linux()
        else:
            print(f"{color['BOLD']}{color['RED']}This script need to be run as root!!{color['RESET']}")
            exit(1)
    elif WIN:
        if win_admin():
            Windows()
        else:
            print(f"{color['BOLD']}{color['RED']}This script need to be run as administrator!!{color['RESET']}")
            exit(1)
