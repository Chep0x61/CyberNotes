# Hydra

### Bruteforce Protocol with know User
```
hydra -l <user> -P <wordlist> <protocol>://<ip>
```

### Bruteforce Protocol with lists
```
hydra -l <users_list> -P <passwords_list> <protocol>://<ip>
```

### Specify number of threads
```
hydra -l <user> -P <passwordlist> <protocol>://<ip> -t <threads>
```

### Bruteforce Http Form
```
hydra -l <user> -P <wordlist> http-post-form://<ip>:<form_parameters>:<failure_string>
```

### Save Output into a file
```
hydra -l <user> -P <passwordlist> <protocol>://<ip> -o <outputfile>
```
