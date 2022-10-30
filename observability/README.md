## Compose sample
### Observability stack (Prometheus + Grafana + Loki + Promtail)

Project structure:
```
.
├── compose.yaml
├── grafana
│   └── datasource.yml
├── prometheus
│   └── prometheus.yml
├── loki
│   └── config.yml
├── promtail
│   └── config.yml
└── README.md
```

Compose file:
The compose file defines a stack with two services `prometheus` and `grafana`.
When deploying the stack, docker compose maps port the default ports for each service to the equivalent ports on the host in order to inspect easier the web interface of each service.
Make sure the ports 9090 and 3000 on the host are not already in use.

## Deploy with docker compose

```
$ docker compose up -d

```

## Expected result

Listing containers must show two containers running and the port mapping as below:
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
dbdec637814f        prom/prometheus     "/bin/prometheus --c…"   8 minutes ago       Up 8 minutes        0.0.0.0:9090->9090/tcp   prometheus
79f667cb7dc2        grafana/grafana     "/run.sh"                8 minutes ago       Up 8 minutes        0.0.0.0:3000->3000/tcp   grafana
```

Navigate to `http://localhost:3000` in your web browser and use the login credentials specified in the compose file to access Grafana. It is already configured with prometheus as the default datasource.

![page](output.jpg)

Navigate to `http://localhost:9090` in your web browser to access directly the web interface of prometheus.

Stop and remove the containers. Use `-v` to remove the volumes if looking to erase all data.
```
$ docker compose down -v
```
# Observability stack


## OPTIONA: Install the grafana loki docker driver client
docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions

## OPTIONAL: Modify the AVIATOR docker-compose to push logs to loki
For each service on docker-compose add the logging option
```
logging:
  driver: loki
    options:
      loki-url: "http://your-docker-ip:3100/loki/api/v1/push"
```

## Run docker-compose
docker-compose up -d

## Test Prometheus UI
http://<your-ip>:9090

## Grafana UI
http://<your-ip>:3000/
admin/admin


