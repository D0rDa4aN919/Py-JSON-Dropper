import base64, json

class Creator:
    def __init__(self):
        self.final_json = {}
        self.names = []

    def json_format(self, binary_file):
        if "/" in binary_file:
            binary_file = binary_file.split("/")[-1]
        elif "\\" in binary_file:
            binary_file = binary_file.split("\\")[-1]
        self.names.append(binary_file)
        with open(binary_file, "rb") as file:
            text = file.read()

        encoded = base64.b32encode(text)
        encoded = encoded.decode('utf-8')
        self.final_json[binary_file.split(".")[0]] = {"body": encoded, "fullName": binary_file}

    def save_json(self, file_name):
        with open(file_name, "w") as file:
            json.dump(self.final_json, file, indent=4)


def main():
    json_file = Creator()
    end = False
    files = []
    while not end:
        user_file = input("Enter the malware file path[for exit press no]:")
        if user_file.lower() == "no":
            end = True
        else:
            files.append(user_file)
    for file in files:
        json_file.json_format(file)
    name = input("Choose a name to the file: ")
    if ".json" in name:
        name.strip(".json")
    json_file.save_json(f"{name}.json")
    print(f"Done! You can see the json format in {name}.json")


if __name__ == '__main__':
    main()