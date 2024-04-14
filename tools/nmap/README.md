# NMap

### Classic Enumeration Phase for CTF challenge
```
nmap -sC -sV -p- --min-rate=5000 <ip>
```

### Target a specific port
```
nmap -p <port> <ip>
```

### Start a NMap Script
```
nmap --script <script> -p <port> <ip>
```

### Save Output to a file
```
nmap -oN <filename> <ip>
```
