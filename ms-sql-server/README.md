```
sudo docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=your-password" -p 1433:1433 --name sql -h sql -d mcr.microsoft.com/mssql/server:2019-latest
```

Copy your backup file to the container tmp folder
```
sudo docker cp your-backup.bak sql:/tmp
```

Launch SQL Studio and connect to your docker
Restore your database from the /tmp folder inside the container

Database default folder: /var/opt/mssql

ODBC Driver use latest release due to extra TLS security
