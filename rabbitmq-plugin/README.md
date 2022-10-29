## Build new image
```
docker build -t local/rabbitmq .
```

## Docker run again with new image (note the new port)
```
docker run -d -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=your-password -p 15672:15672 -p 5672:5672 -p 15692:15692 -h bunny1 --name bunny1 local/rabbitmq
```

http://hostname:15692/metrics
