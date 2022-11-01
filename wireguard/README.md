# Wireguard

#### Installation

```bash
mkdir wireguard
```

```bash
wget https://raw.githubusercontent.com/ZanMax/homelab/main/wireguard/docker-compose.yml
```
> Change option in docker-compose
- TZ - timezone
- SERVERURL - set your public IP
- PEERS - number of clients
- /path/to/appdata/config - path to your folver with wireguard ( for example /home/dev/wireguard/config )


```bash
docker-compose up -d
```

#### Get client config

```bash
cd /home/dev/wireguard/config/peer1
```

> Go to /home/dev/wireguard/config/peer1 (peer nubmer link 1,2,3 ...)
>> use peer1.conf or peer1.png file to connect
>> to show png file as QR code just exec
>>> docker exec -it wireguard /app/show-peer 2