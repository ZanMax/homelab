# First steps after OS installation

### Add ssh key

```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub 192.168.1.10
```
### Update / Upgrade packages 

```bash
wget https://raw.githubusercontent.com/ZanMax/homelab/main/scripts/upgrade.sh
```
```bash
chmod +x upgrade.sh
```
```bash
./upgrade.sh
```
### Install packages

```bash
sudo apt -y install python3-dev python3-pip python-is-python3 git zip wget curl ntp
```

### Resize DISK

```bash
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
```
```bash
sudo resize2fs /dev/mapper/ubuntu--vg-ubuntu--lv
```

### Docker

```bash
sudo apt -y install docker.io
```
```bash
sudo usermod -aG docker ${USER}
```
```bash
sudo reboot
```

### Docker-Compose

```bash
sudo apt -y install docker-compose
```

### Docker-Runner
```bash
wget https://raw.githubusercontent.com/ZanMax/scripts/master/sh/docker_runner.sh
```

```bash
chmod +x docker_runner.sh
```
```bash
./docker_runner.sh
```