<h1 style="text-align:center;">Py Json Dropper</h1>
The Py_Json_Dropper is intended to make it easier to create and disseminate JSON-formatted malware droppers. A dropper is a little program created to install and run additional harmful malware on a target machine. The program aids in producing a JSON file that contains base32-encoded malware bodies and file names that can later be used to spread malware using API.

<h2 style="text-align:center;">Important Note</h2>
This tool is intended for educational and ethical purposes only. It is important to follow legal and ethical guidelines when using and distributing software. Unauthorized use of malware or any malicious activities is strictly prohibited and can have serious legal consequences.
This is the POC of the JSON format dropper for defense evasion.

<h2 style="text-align:center;">Features</h2>
- Encode malware bodies into base32 and store them in a JSON format.
- Simple user interface for providing malware file paths.
- Creates a JSON file that includes the encoded malware bodies and file names.

<h2 style="text-align:center;">Installation and Usage</h2>

<h3>Installation</h3>
To use this tool, make sure you have the required dependencies installed:
Note: It is not a must step, because there is an installation process in the dropper.

  ```shell
pip install requests
  ```
<h3>Usage</h3>
- Run the creator.py script to create the JSON file:

  ```shell
python3 creator.py
  ```
- Enter the paths to your malware files by following the prompts. When you're finished, you'll be asked to give the JSON file a name. The malware's bodies and file names will be encoded in the final JSON file.
- Upload the JSON to the API editor or create a website API.
- Add this script for the main dropper script that will run before the execution of the dropped malware.
- Run the dropper script on the target side and it will decode the JSON API, extract malware bodies, and insert those bodies to files with the index number of malware.

<h2 style="text-align:center;">License</h2>
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<h2 style="text-align:center;">Author</h2>
- [D0rDa4aN919](https://github.com/D0rDa4aN919)

<h2 style="text-align:center;">Acknowledgments</h2>
The tool was developed to demonstrate how to produce and disseminate malware droppers in a controlled setting. It is not meant to support or facilitate any nefarious or unlawful activity.

