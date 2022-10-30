# Docker-Gen

#### Installation

```bash
wget https://github.com/nginx-proxy/docker-gen/releases/download/0.7.6/docker-gen-linux-amd64-0.7.6.tar.gz
tar xvzf docker-gen-linux-amd64-0.7.6.tar.gz
```

```bash
mv docker-gen /bin
```

```bash
sudo wget https://raw.githubusercontent.com/jwilder/docker-gen/master/templates/nginx.tmpl -O /etc/systemd/system/docker-gen.service
```

```bash
sudo wget https://raw.githubusercontent.com/jwilder/docker-gen/master/templates/nginx.tmpl -O /etc/nginx.tmpl
```

```bash
sudo systemctl daemon-reload
sudo systemctl restart docker-gen
```