# page-distributor
Container which distributes several pages to further containers

## Installation
Run with root permission:
installs.py

### Add new page
1. Add proxy entry into pages folder
2. Enable site in Dockerfile. E.g: RUN a2ensite notstrommalters.ch.conf 

## Status
Check status of the installation with: 
systemctl status page-distributor.service

Check if container is running:
docker ps

## Connect to container
docker exec -it page-distributor /bin/bash
