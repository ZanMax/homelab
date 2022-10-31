# GitLab

#### Installation

```bash
mkdir gitlab
```

```bash
export GITLAB_HOME=$(pwd)/gitlab
```

```bash
wget https://raw.githubusercontent.com/ZanMax/homelab/main/gitlab/docker-compose.yml
```

```bash
docker-compose up -d
```

```bash
docker exec -it gitlab-ce grep 'Password:' /etc/gitlab/initial_root_password
```

#### GitLab runner configuration


>Go to the address: http://localhost:8080/admin/runners and click the Copy token button.

```bash
docker exec -it gitlab-runner gitlab-runner register --url "http://gitlab-ce" --clone-url "http://gitlab-ce"
```

>Enter the GitLab instance URL: confirm the entered value (click enter)
Enter the registration token: enter the token copied before.
Enter a description for the runner: enter the name of the runner, e.g. docker-runner
Enter tags for the runner: leave the field blank here
Enter an executor: enter docker here
Enter the default Docker image: here we provide the default docker image, e.g. maven: latest


```bash
sudo nano gitlab/gitlab-runner/config.toml
```

> Then we add new line to the end of the runner configuration: network_mode = "gitlab-network"


>>Check Runner is available
http://localhost:8080/admin/runners
