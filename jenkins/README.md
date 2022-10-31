# Jenkins

#### Installation

```bash
mkdir jenkins_home
```

```bash
wget https://github.com/nginx-proxy/docker-gen/releases/download/0.7.6/docker-gen-linux-amd64-0.7.6.tar.gz
```

```bash
docker-compose up -d
```

```bash
docker exec jenkins-lts cat /var/jenkins_home/secrets/initialAdminPassword
```

Go to jenkins.local and "Unlock Jenkins"