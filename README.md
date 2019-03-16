# revshellgen
Simple script to generate commands to achieve reverse shells. This is a python port of Shell Lover by DevoOverkill9.

![Screenshot](https://user-images.githubusercontent.com/45709553/54481816-b75ff180-4807-11e9-84db-17aadd39799c.PNG)

**Usage:**
revshellgen.py [-h] [-i IPADDR] [-p PORT] [-t SHELL_TYPE] [-l] [-a]<br/>

python revshellgen.py -i 127.0.0.1 -p 1234 -t bash<br/>

optional arguments:<br/>
  -h, --help            show this help message and exit<br/>
  -i IPADDR, --ipaddr IPADDR<br/>
                        IP address to connect back to<br/>
  -p PORT, --port PORT  Port to connect back to<br/>
  -t SHELL_TYPE, --type SHELL_TYPE<br/>
                        Type of reverse shell to generate<br/>
  -l, --list            List available shell types<br/>
  -a, --all             Generate all the shells!<br/>

**Shell Types:**<br/>
ASP<br/>
Bash<br/>
Java Server Page<br/>
Linux Binary<br/>
Lua<br/>
Netcat (regular, mknod, & mkfifo variants)<br/>
OSX Macho Binary<br/>
Perl<br/>
PHP<br/>
Powershell TCPClient<br/>
Powershell IEX<br/>
Python<br/>
Ruby<br/>
Socat (preferred for interactive sessions)<br/>
Telnet<br/>
War<br/>
Windows Binary<br/>
Xterm<br/>
