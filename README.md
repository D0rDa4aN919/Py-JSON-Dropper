<h1 align="center">Py Json Dropper</h1>

The Py-JSON-Dropper is a POC for JSON-format dropper, and intended to make it easier to create and disseminate JSON-formatted malware droppers. A [dropper](https://medium.com/@dordaha491n/the-stealthy-evolution-of-malware-droppers-a-closer-look-cb269722d887) is a little program created to install and run additional harmful malware on a target machine. The program aids in producing a JSON file that contains base64-encoded malware bodies and file names and establishes an API interface in local/remote options, that can later be used to spread malware using API. After achieving the malware body from the API, it will use the file extension to choose the in-memory execution type(for Power-Shell, Jave, and Python) pr execution(for regular execution of executable).
<br><br>
The POC is to demonstrate the option to build a dropper via JSON format and drop malware using this method, focusing on the concept of JSON dropper and less the in-memory execution process due to the malicious uses.
<br><br>
<h4>Local mode:</h4>

![Local mode](pics/local_diagram.jpg)
<br>
<h4>Remote mode:</h4>

![Remote mode](pics/remote_diagram.jpg)
<br>

<h2 align="center">Important Note</h2>
This tool is intended for educational and ethical purposes only. It is important to follow legal and ethical guidelines when using and distributing software. The unauthorized use of malware or any malicious activities is strictly prohibited and can have serious legal consequences.
This is the POC of the JSON format dropper for defense evasion.

<h2 align="center">Features</h2>

<h3s>The Py-JSON-Dropper features:</h3>

<h4>create_json.py</h4>

- Note: Execute create_json.py from the attacker side.
- Encode malware bodies into base64 and store them in a JSON format.
- Simple user interface for providing malware file paths.
- Creates a JSON file that includes the encoded malware bodies and file names.
- In local mode: It will create Flask API/Download server.
- In remote mode(default): It will create new API interface in npoint.io and request to enter the json text.
- Add the new url to the dropper.py file and create with new dropper_final.py file.

<h3>dropper_final.py</h3>

- Note: Send and execute dropper_final.py from the traget machine.
- Check the extension type of the code for the execution.
- Execute the script.

<h2 align="center">Installation and Usage</h2>

<h3>Installation</h3>

To use this tool, make sure you have the required dependencies installed:

  ```shell
  python setup.py
  ```

![Execute script](pics/setup.jpg)
  
<h3>Usage</h3>

To use this tool, will require the malware to be written in Bash, Power-Shell, Java, or Python or exectuable files.
In the attacker side script (create_json.py) have to main function local or remote.
<br>
Note: It can run exe files but without EDR/AV, due the need to save the exe file (but it is in develop)
<br>
Note: In the example, can see a reverse shell prcoess that run via the dropper(On Windows machine).
<br>
- Run the creator.py script to create the JSON file:
  ```shell
  python3 create_json.py
  ```
- Enter the paths to your malware files by following the prompts. When you're finished, you'll be asked to give the JSON file a name. The malware's bodies and file names will be encoded in the final JSON file.

- <h4>Local mode</h4>

  - It will create a Flask website, and upload the JSON file.
  - Create new dropper with the url in dropper_final.py
  - Set a download page in the Flask website to download the dropper_final.py
  
  ![creator process](pics/local_json_create.jpg)

- <h4>Remote mode</h4>

  - Create new dropper with the url in dropper_final.py
  - It will create a new API link in npoint.io website, and the attcker will need to update the link with the JSON file.
  - Need to find the way to transfer the new dropper to the target.
  
  ![Remote Mode](pics/remote_json_create.jpg)

- Run the dropper_final.py in the target side:
  ```shell
  # Linux:
  python dropper_final.py
  # Windows:
  py dropper_final.py
  ```
![creator process](pics/dropper_process.jpg)

- In the final stage the attacker get the shell.

![Reverse shell](pics/shell.jpg)

<h2 align="center">Demonstration</h2>

<h3>Notes:</h3>

- The videos of the demnostration are in pics directory.
- The tool could bypass the defender using obfuscation of Power-shell scripts and python(it could be with exe and java with the right code edit).

<h4>Defender bypass:</h4>

![](pics/defender_bypass.jpg)

<h4>Local Mode:</h4>

![Local demonstration](pics/local_Demonstration.gif)

<h4>Remote Mode:</h4>

![Remote demonstration](pics/remote_Demonstration.gif)

<h2 align="center">License</h2>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<h2 align="center">Author</h2>

- [D0rDa4aN919](https://github.com/D0rDa4aN919)

<h2 align="center">Acknowledgments</h2>
The tool was developed to demonstrate how to produce and disseminate malware droppers in a controlled setting. It is not meant to support or facilitate any nefarious or unlawful activity.

- [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [Dropper](https://medium.com/@dordaha491n/the-stealthy-evolution-of-malware-droppers-a-closer-look-cb269722d887)
- [RastFul API](https://docs.github.com/en/rest?apiVersion=2022-11-28)
- [JSON-based dropper article](https://medium.com/@dordaha491n/malware-dropping-techniques-using-json-format-a-stealthy-approach-afbf8c00023d)
