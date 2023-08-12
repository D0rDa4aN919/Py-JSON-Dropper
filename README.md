<h1 align="center">Py Json Dropper</h1>
The Py-JSON-Dropper is intended to make it easier to create and disseminate JSON-formatted malware droppers. A dropper is a little program created to install and run additional harmful malware on a target machine. The program aids in producing a JSON file that contains base32-encoded malware bodies and file names that can later be used to spread malware using API. After achiving the malware body from the API, it will use the file extention for choose the in memory execution.

<h2 align="center">Important Note</h2>
This tool is intended for educational and ethical purposes only. It is important to follow legal and ethical guidelines when using and distributing software. The unauthorized use of malware or any malicious activities is strictly prohibited and can have serious legal consequences.
This is the POC of the JSON format dropper for defense evasion.

<h2 align="center"">Features</h2>

The Py-JSON-Dropper features:
- Encode malware bodies into base32 and store them in a JSON format.
- Simple user interface for providing malware file paths.
- Creates a JSON file that includes the encoded malware bodies and file names.

<h2 align="center"">Installation and Usage</h2>

<h3>Installation</h3>
To use this tool, make sure you have the required dependencies installed:

Note: It is not a must step, because there is an installation process in the dropper.

  ```shell
  pip install requests
  ```
  
<h3>Usage</h3>

To using this tool, it will require from the malware to be writen in Bash, Power-Shell, Java or Python.

- Run the creator.py script to create the JSON file:
  ```shell
  python3 create_json.py
  ```
![creator process](pics/create_json_process.jpg)
- Enter the paths to your malware files by following the prompts. When you're finished, you'll be asked to give the JSON file a name. The malware's bodies and file names will be encoded in the final JSON file.
- Upload the JSON to the API editor or create a website API.
- Add this script for the main dropper script that will run before the execution of the dropped malware.
- Run the dropper script on the target side and it will decode the JSON API, extract malware bodies, and insert those bodies to files with the index number of malware ("{file name}_{index}.{ext}").
- Or for a practice run it on the Linux machine to see the results:
  ```shell
  python3 dropper.py
  ```

![creator process](pics/dropper_process.jpg)

- You could compare between the old file and the new file to check the download process working

![creator process](pics/compere.jpg)

<h2 align="center"">Defense Evasion - show case</h2>
The tool is checked on two EDRs (Sophos Home and Windows Defender) and new unknown fetch malware.

[New uknown fetch malware](https://bazaar.abuse.ch/sample/39effc8ad793805f7a5558b804d72b01de87db3a89657c91d5508612c15d3761/)

- The process on the target side:

![Running script example](pics/evasion.jpg)

- An example: (Sophos Home)

![Sophos Home example](pics/evasion_sophos_home.jpg)

- An example: (Windows Defender)

![Windows Defender example](pics/evasion_defender.jpg)

Note: You can add an encryption stage to the script, it will encrypt the binary text before the JSON insert and could add to the JSON the decryption key. Using this an attacker can add another layer of protection to the malware and decrypt the malware body before it executes.

<h2 align="center"">License</h2>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<h2 align="center">Author</h2>

- [D0rDa4aN919](https://github.com/D0rDa4aN919)

<h2 align="center">Acknowledgments</h2>
The tool was developed to demonstrate how to produce and disseminate malware droppers in a controlled setting. It is not meant to support or facilitate any nefarious or unlawful activity.

- [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [Dropper](https://encyclopedia.kaspersky.com/glossary/trojan-droppers/)
- [RastFul API](https://docs.github.com/en/rest?apiVersion=2022-11-28)
