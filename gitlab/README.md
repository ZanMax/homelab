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

> Username: root

```bash
docker exec -it gitlab-ce grep 'Password:' /etc/gitlab/initial_root_password
```
#### Configuration
>  turn off open registration for everyone
http://gitlab.local/admin/application_settings/general#js-signup-setting

>  change the root user
http://gitlab.local/-/profile/account

>  change the password
http://gitlab.local/-/profile/password/edit

#### GitLab runner configuration


> Go to the address: http://gitlab.local/admin/runners and click the "Copy token button" (Register an instance runner).


```bash
docker exec -it gitlab-runner gitlab-runner register --url "http://gitlab-ce" --clone-url "http://gitlab-ce"
```

>Enter the GitLab instance URL: confirm the entered value (click enter)
Enter the registration token: enter the token copied before.
Enter a description for the runner: docker-runner
Enter tags for the runner: blank here
Enter an executor: docker
Enter the default Docker image: maven: latest


```bash
sudo nano gitlab/gitlab-runner/config.toml
```

> Then we add new line to the end of the runner configuration: network_mode = "gitlab-network"


>>Check Runner is available
http://gitlab.local/admin/runners


>Create new porject
http://gitlab.local/projects/new 
