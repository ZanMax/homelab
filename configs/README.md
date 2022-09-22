# Config homelab cluster

### Preparation of PC

#### Change hostname

`sudo nano /etc/hostname`

`sudo nano /etc/hosts`

#### Update all packages

`sudo apt -y update && sudo apt-get -y upgrade && sudo apt -y dist-upgrade && sudo apt -y full-upgrade`

#### Install necessary packages

`sudo apt -y install python3-dev python3-pip libssl-dev libevent-dev libpq-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev python3-virtualenv python3-pip build-essential libmysqlclient-dev git zip wget curl ntp nfs-common cron systemd-timesyncd`


### Install k3s

#### Master

`curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC='server --no-deploy traefik' sh -`


#### Node

`curl -sfL https://get.k3s.io | K3S_URL="https://<MASTER_IP>:6443" K3S_TOKEN="<token>::server:91b275d5aa678d3298ed43fa39089d2f" sh -`