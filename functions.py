import os
from rich import print

def AllNmapScan(ip):
    os.system(f'nmap {ip} -Pn -p- --open > nmapSCAN')

    ports = []
    with open('nmapSCAN','r') as file:
        for line in file:
            line = line.strip()
            if "/tcp" in line or "/udp" in line:
                port = line.split('/')
                port = port[0]
                ports.append(port)
    string = ""

    for port in ports:
        string = string + f"{port},"

    os.system(f'nmap {ip} -Pn -sC -sV -p{string} > nmapSCAN')

def checkwp(ip):
    os.system(f'wpscan --url {ip} > wpscan')
    with open('wpscan','r') as file:
        check = 0
        for line in file:
            if "The remote website is up, but does not seem to be running WordPress." in line:
                os.system(f'wpscan --url {ip}/wordpress > wpscan')
                for line in file:
                    if "The remote website is up, but does not seem to be running WordPress." in line:
                        print('\n[bold bright_green]✓[/bold bright_green] Scan wpscan : [bright_green]No WP page[/bright_green]')
                        check += 1
        if check == 0:        
            print('\n[bold bright_green]✓[/bold bright_green] Scan wpscan : [bright_green]ok[/bright_green]')


