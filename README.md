
# AnyScan v1.1

### This tool can run any default scan from an host. The tools used by default are:
- Nmap
- Gobuster





# USE

#### To use this program, you have to:

```bash
python3 anyscan.py -H <IP>
```

#### Help:
```bash
python3 anyscan.py -h
```

#### Scan with WPscan:
```bash
python3 anyscan.py -H <IP> -wp
```

#### Scan with Nikto:
```bash
python3 anyscan.py -H <IP> -n
```

#### Scan with Enum4linux (SMB service only):
```bash
python3 anyscan.py -H <IP> -e
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