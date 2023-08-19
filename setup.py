import os
import subprocess

from vars import *


def statement(pip, google):
    if pip is True and google is True:
        print(f"""
{add_color('BOLD')}{add_color('GREEN')}The machine is setup for the tool...
You are ready to go!!
Execute the create_json.py...{add_color('RESET')}""")
    elif pip is True and google is False:
        print(f"""
{add_color('BOLD')}{add_color('GREEN')}The machine is setup with requirements.txt...
{add_color('RED')}You need to fix the chrome installation!!{add_color('GREEN')}
After fixing the installation execute the create_json.py...{add_color('RESET')}""")
    elif pip is False and google is True:
        print(f"""
{add_color('BOLD')}{add_color('GREEN')}The machine is setup with google chrome...
{add_color('RED')}You need to fix the requirements.txt installation!!{add_color('GREEN')}
After fixing the installation execute the create_json.py...{add_color('RESET')}""")
    elif pip is False and google is False:
        print(f"""{add_color('BOLD')}{add_color('RED')}
You will need you to preform the process of installing the requirements.txt and google chrome
After fixing the installation execute the create_json.py...{add_color('RESET')}""")


def add_color(color_choose):
    if admin is True:
        return ""
    else:
        return color[f"{color_choose}"]


def linux():
    # Define the path to the .deb file
    deb_file_path = "drivers/google_chrome.deb"
    final_check = ""

    # Download the chrome deb file
    def download_chrome_installer():
        import requests
        print(f"{color['BOLD']}{color['CYAN']}Importing the web driver...{color['RESET']}")
        download_url = f"https://www.mediafire.com/file/tq8y4n4bxzmhzwc/google-chrome-stable_current_amd64.deb/file"
        if os.path.exists(deb_file_path):
            print(
                f"{color['BOLD']}{color['CYAN']}{deb_file_path} already exists in drivers. Skipping download.{color['RESET']}")
            return

        response = requests.get(download_url)
        download_url = response.text.split('input popsok')[1].split('href="')[1].split('"')[0]
        response = requests.get(download_url)

        if response.status_code == 200:
            with open(deb_file_path, "wb") as installer_file:
                installer_file.write(response.content)
            print(f"{color['BOLD']}{color['GREEN']}{deb_file_path} downloaded and saved to drivers{color['RESET']}")
        else:
            print(
                f"{color['BOLD']}{color['RED']}Failed to download {deb_file_path}. HTTP status code: {response.status_code}{color['RESET']}")

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
        subprocess.run(["sudo", "dpkg", "-i", deb_file_path], stdout=subprocess.DEVNULL)
        # Importing the chrome deb file for the create_json.py file
        download_chrome_installer()
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
        statement(final_check_google, final_check_pip)

    setup_package_linux()


def windows():
    exe_file_path = ".\\drivers\\firefox_installer.exe"

    # Download the firefox deb file
    def download_firefox_installer():
        import requests
        print(f"{add_color('BOLD')}{add_color('CYAN')}Importing the web driver...{add_color('RESET')}")
        download_url = f"https://www.mediafire.com/file/tnl4wa295q2t7xg/firefox_installer.exe/file"
        if os.path.exists(exe_file_path):
            print(
                f"{add_color('BOLD')}{add_color('CYAN')}{exe_file_path} already exists in drivers. Skipping download.{add_color('RESET')}")
            return

        response = requests.get(download_url)
        download_url = response.text.split('input popsok')[1].split('href="')[1].split('"')[0]
        response = requests.get(download_url)
        if response.status_code == 200:
            with open(exe_file_path, "wb") as installer_file:
                installer_file.write(response.content)
            print(
                f"{add_color('BOLD')}{add_color('GREEN')}{exe_file_path} downloaded and saved to drivers{add_color('RESET')}")
        else:
            print(
                f"{add_color('BOLD')}{add_color('RED')}Failed to download {exe_file_path}. HTTP status code: {response.status_code}{add_color('RESET')}")

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
        # Importing the firefox exe file for the create_json.py file
        download_firefox_installer()
        # Install the .exe file for Firefox
        subprocess.run([exe_file_path, "/silent"], stdout=subprocess.DEVNULL)

        # Check if 'firefox' is in PATH
        if is_firefox_installed():
            final_check_firefox = True
            print(
                f"{add_color('BOLD')}{add_color('GREEN')}Firefox is installed and accessible in PATH.{add_color('RESET')}")
        else:
            print(f"""{add_color('BOLD')}{add_color('RED')}Firefox is not installed or not accessible in PATH.
You need to manually install Firefox.{add_color('RESET')}""")

        # Install packages from requirements.txt
        requirements_file = "requirements.txt"
        try:
            subprocess.run(["pip", "install", "-r", requirements_file], stdout=subprocess.DEVNULL)
            print(
                f"{add_color('BOLD')}{add_color('GREEN')}Required packages installed successfully.{add_color('RESET')}")
            final_check_pip = True
        except Exception as e:
            print(f"""{add_color('BOLD')}{add_color('RED')}An error occurred while installing packages: {e}")
Try running: pip install -r {requirements_file}")
print("Check that all of the packages in requirements.txt are installed.{add_color('RESET')}""")

        statement(final_check_pip, final_check_firefox)

    setup_package_windows()


# Run the setup function
if __name__ == "__main__":
    subprocess.run(["pip", "install", "requests"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if LIN:
        if lin_user():
            admin = lin_user(1)
            linux()
    elif WIN:
        admin = win_admin()
        windows()
