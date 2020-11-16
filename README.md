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

### Shell Types:

- ASP: `asp`
- AWK: `awk`
- Bash: `bash`, `bash-2`, `bash-3`
- Java: `java`
- Java Server Page: `jsp`
- Linux Binary: `lin-bin`
- Lua: `lua`
- Netcat (regular, mknod, & mkfifo variants): `nc`, `nc-c`, `nc-mkfifo`, `nc-mknod`, `nc-pipe`, `ncat`
- Nodejs: `nodejs`
- OSX Macho Binary: `osx-bin`
- Perl: `perl`, `perl-2`, `perl-windows`
- PHP: `php`, `php-2`, `php-3`, `php-4`, `php-5`
- Powershell TCPClient: `ps-tcp`, 
- Powershell IEX: `ps-iex`, `ps-b64`
- Python: `python`, `python-2`
- Ruby: `ruby`, `ruby-2`, `ruby-windows`
- Socat (preferred for interactive sessions): `socat`
- Tclsh: `tclsh`
- Telnet: `telnet`, `telnet-mkfifo`
- War: `war`
- Windows Binary: `win-bin`
- Xterm: `xterm`

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
