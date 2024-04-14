# Docker

### Build an Image
```
docker build -t <name> . 
```

### Launch an Image
```
docker run  <name>
```

### Launch an Image in Background
```
docker run  <name> -d
```

### Display active containers
```
docker ps
```

### Display all containers
```
docker ps -a
```

### Build an Image locally and send it to a server
```
docker save <name> | bzip2 | pv | ssh <server> docker load
```

### Save Image as a tar file
```
docker save <name> -o <output>.tar
```
