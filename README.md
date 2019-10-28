# revshellgen
Simple script to generate commands to achieve reverse shells. Thanks to DevoOverkill9 for the great idea!

![Screenshot](https://user-images.githubusercontent.com/45709553/54481816-b75ff180-4807-11e9-84db-17aadd39799c.PNG)

## Usage

```
revshellgen.py [-h] [-i IPADDR] [-p PORT] [-t SHELL_TYPE] [-l] [-a]

python revshellgen.py --help

optional arguments:
  -h, --help            show this help message and exit
  -i IPADDR, --ipaddr IPADDR
                        IP address to connect back to
  -p PORT, --port PORT  Port to connect back to
  -t SHELL_TYPE, --type SHELL_TYPE
                        Type of reverse shell to generate
  -l, --list            List available shell types
  -a, --all             Generate all the shells!
```

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

## Recommended Setup Steps

For ease of use, it's recommended to add revshellgen to your path variable and give it executable permissions. 

```
chmod +x /dir/to/revshellgen.py
export PATH=$PATH:/dir/to/revshellgen
```

Alternatively, you can integrate it with other Kali tools by performing the following:

```
chmod +x /dir/to/revshellgen.py
ln -s /dir/to/revshellgen.py /usr/bin/revshellgen
```

Keep in mind, this isn't ideal for systems with multiple users, and you should use root-privilege symbolic links with discretion. It's imperative that revshellgen.py is restricted from write access by untrusted users with this. 

**Another Example:**

![Screenshot](https://user-images.githubusercontent.com/45709553/54481815-b5962e00-4807-11e9-84a1-80c7901452c7.PNG)
