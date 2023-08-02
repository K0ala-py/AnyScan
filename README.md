
# AnyScan

### This tool can run any default scan from an host.





# USE

#### To use this program, you have to:

```bash
python3 anyscan.py -H <IP>
```
#### Scan with WPscan:
```bash
python3 anyscan.py -H <IP> -wp
```
#### Select port for Nmap:
```bash
python3 anyscan.py -H <IP> -p <port>
```

#### Select wordlist for Gobuster:
```bash
python3 anyscan.py -H <IP> -w <path>
```

### Example:
```bash
python3 anyscan.py --host 127.0.0.1 -wp -p 443 -w /usr/share/wordlists/dirb/big.txt
```
# Note

you must install "requirements.txt"
```bash
pip install -r requirements.txt
```