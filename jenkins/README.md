# Jenkins

#### Installation

```bash
mkdir jenkins_home
```

```bash
wget https://raw.githubusercontent.com/ZanMax/homelab/main/jenkins/docker-compose.yml
```

##### Edit docker-compose.yml and add full path to jenkins_home

```bash
docker-compose up -d
```

```bash
docker exec jenkins-lts cat /var/jenkins_home/secrets/initialAdminPassword
```

##### Go to jenkins.local and "Unlock Jenkins"