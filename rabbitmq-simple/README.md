Docker run
```
docker run -d -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=ImagineDB1 -p 15672:15672 -p 5672:5672 -h bunny1 --name bunny1 rabbitmq:3-management
```

Dockerfile
```
FROM rabbitmq:3-management
RUN rabbitmq-plugins enable --offline rabbitmq_prometheus rabbitmq_tracing
```

Build new image
```
docker build -t imagine/rabbitmq .
```

Docker run again with new imagine image (note the new port)
```
docker run -d -e RABBITMQ_DEFAULT_USER=admin -e RABBITMQ_DEFAULT_PASS=ImagineDB1 -p 15672:15672 -p 5672:5672 -p 15692:15692 -h bunny1 --name bunny1 imagine/rabbitmq
```

http://hostname:15692/metrics

