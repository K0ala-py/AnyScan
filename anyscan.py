# library used
import requests
import socket
import os
import threading as th
import argparse
import textwrap
from rich import print
from time import sleep

# intro of program
parser = argparse.ArgumentParser(description="ScanVUN is a beautifull script for the Vulnerability",
formatter_class = argparse.RawDescriptionHelpFormatter,
epilog=textwrap.dedent('''Exemption:\n
scanvul.py -i 127.0.0.1 -wp
'''))

#help
def help():
    
    print("\n[bold]scanvul.py [-h] or [--help] to display the help command[bold]")
    os.system("python scanvul -h")
    return ''

parser.add_argument('-H','--host',type=str, help=' Enter IP or domain')
parser.add_argument('-wp','--wordpress',action="store_true",help='Also scan with WPscan')
parser.add_argument('-p','--port',type=int, help='Enter port')
parser.add_argument('-w','--wordlist',type=str, help='Wordlist for gubster scan')
parser.add_argument('-e','--enumerationSMB',action="store_true", help='SMB scan')
parser.add_argument('-n','--nikto',action="store_true", help='Nikto scan')


args = parser.parse_args()

# collection of arguments
ip = args.host
if args.port:
    port = args.port
else:
    port = 0

if args.wordlist:
    wordlist = args.wordlist
else:
    wordlist = "/usr/share/wordlists/dirb/small.txt"

# main function
def main(ip,port,wordlsit):
    try:
        ip = socket.gethostbyname(ip)
    except:
        print('[bold yellow]No Connect[/bold yellow]')
        quit()
    process(ip,port,wordlist)

# nmap function scan
def nmap(ip,port):
    if args.port:    # if PORT is selected...
        os.system(f'nmap {ip} -Pn -sC -sV -p {port} > nmapSCAN')
    else:            # if PORT isn't selected...   
        from functions import AllNmapScan
        AllNmapScan(ip)            # function in functins.py file, where it will speed the Nmap Scan (it'll use: -sC -sV)
    print('\n[bold bright_green]✓[/bold bright_green] Scan Nmap : [bright_green]ok[/bright_green]')

# nikto function scan
def nikto(ip):
    os.system(f'nikto -h {ip} -ask no -C all > niktoSCAN')
    print('\n[bold bright_green]✓[/bold bright_green] Scan Nikto : [bright_green]ok[/bright_green]')

# gobuster function scan 
def gobuster(ip,wordlist):
    print('[cyan]Gobuster Scan :[/cyan]')
    os.system(f'gobuster dir -u http://{ip}/ -w {wordlist} > gobusterSCAN')
    print('\n[bold bright_green]✓[/bold bright_green] Scan Gobuster : [bright_green]ok[/bright_green]')

# wordpress funcion scan
def wpscan(ip):
    from functions import checkwp
    checkwp(ip)            # function in functions.py, where check if the WPscan works

# enum4linux function scan (SMB service)
def e4l(ip):
    os.system(f'enum4linux -a {ip} > enumsmbSCAN.txt')
    print('\n[bold bright_green]✓[/bold bright_green] Scan Enum4linux : [bright_green]ok[/bright_green]')

# clear function and import of banner file
def clear():
    os.system('clear')
    import banner

# starts processes
def process(ip,port,wordlist):
    th.Thread(target=clear).start()
    sleep(2)
    th.Thread(target=nmap,args=(ip,port,)).start()
    sleep(1)
    if args.nikto:
        th.Thread(target=nikto,args=(ip,)).start()
        sleep(1)
    th.Thread(target=gobuster,args=(ip,wordlist,)).start()
    if args.wordpress:
        sleep(1)
        th.Thread(target=wpscan,args=(ip,)).start()
    if args.enumerationSMB:
        sleep(1)
        th.Thread(target=e4l,args=(ip,)).start()
    

main(ip, port,wordlist)
