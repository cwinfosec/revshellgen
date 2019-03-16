# revshellgen
Simple script to generate commands to achieve reverse shells. This is a python port of Shell Lover by DevoOverkill9.

![Screenshot](https://user-images.githubusercontent.com/45709553/54481816-b75ff180-4807-11e9-84db-17aadd39799c.PNG)

**Usage:**
revshellgen.py [-h] [-i IPADDR] [-p PORT] [-t SHELL_TYPE] [-l] [-a]

python revshellgen.py -i 127.0.0.1 -p 1234 -t bash

optional arguments:
  -h, --help            show this help message and exit
  -i IPADDR, --ipaddr IPADDR
                        IP address to connect back to
  -p PORT, --port PORT  Port to connect back to
  -t SHELL_TYPE, --type SHELL_TYPE
                        Type of reverse shell to generate
  -l, --list            List available shell types
  -a, --all             Generate all the shells!

**Shell Types:**
ASP
Bash
Java Server Page
Linux Binary
Lua
Netcat (regular, mknod, & mkfifo variants)
OSX Macho Binary
Perl
PHP
Powershell TCPClient
Powershell IEX
Python
Ruby
Socat (preferred for interactive sessions)
Telnet
War
Windows Binary
Xterm
