![logo](./static/cyberlux-logo.jpg?raw=true "CYBERSECURITY Luxembourg")

<table>
<tr>
  <td>API checks</td>
</tr>
<tr>
  <td>Container builder</td>
  <td><a href="https://github.com/CybersecurityLuxembourg/openxeco/actions/workflows/oxe-api_docker.yml"><img src="https://github.com/CybersecurityLuxembourg/openxeco/actions/workflows/oxe-api_docker.yml/badge.svg" /></a></td>
</tr>
<tr>
  <td>Bandit Workflow</td>
  <td><a href="https://github.com/CybersecurityLuxembourg/openxeco/actions/workflows/oxe-api_pycqa-bandit.yml"><img src="https://github.com/CybersecurityLuxembourg/openxeco/actions/workflows/oxe-api_pycqa-bandit.yml/badge.svg" /></a></td>
</tr>
<tr>
  <td>Prospector Workflow</td>
  <td><a href="https://github.com/CybersecurityLuxembourg/openxeco/actions/workflows/oxe-api_pycqa-prospector.yml"><img src="https://github.com/CybersecurityLuxembourg/openxeco/actions/workflows/oxe-api_pycqa-prospector.yml/badge.svg" /></a></td>
</tr>
</table>

<table>
<tr>
  <td>Admin web</td>
</tr>
<tr>
  <td>Package builder</td>
  <td><a href="https://github.com/CybersecurityLuxembourg/openxeco/actions/workflows/oxe-web-admin_package.yml"><img src="https://github.com/CybersecurityLuxembourg/openxeco/actions/workflows/oxe-web-admin_package.yml/badge.svg" /></a></td>
</tr>
</table>

<table>
<tr>
  <td>Community web</td>
</tr>
<tr>
  <td>Package builder</td>
  <td><a href="https://github.com/CybersecurityLuxembourg/openxeco/actions/workflows/oxe-web-community_package.yml"><img src="https://github.com/CybersecurityLuxembourg/openxeco/actions/workflows/oxe-web-community_package.yml/badge.svg" /></a></td>
</tr>
</table>

<table>
<tr>
  <td>Licence</td>
</tr>
<tr>
  <td>FOSSA</td>
  <td><a href="https://app.fossa.com/projects/git%2Bgithub.com%2FCybersecurityLuxembourg%2Fopenxeco-core?ref=badge_shield" alt="FOSSA Status"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2FCybersecurityLuxembourg%2Fopenxeco-core.svg?type=shield"/></a></td>
</tr>
</table>

<table>
<tr>
  <td>Social networks</td>
</tr>
<tr>
  <td>Twitter</td>
  <td><a href="https://twitter.com/cyberluxembourg"><img src="https://img.shields.io/twitter/follow/cyberluxembourg.svg?style=social&label=Follow" /></a></td>
</tr>
</table>

# Set up an instance

## For development

To set up the dev environment, please see those sub-project README files:

- [oxe-api/README.md](oxe-api/README.md)
- [oxe-web-admin/README.md](oxe-web-admin/README.md)
- [oxe-web-community/README.md](oxe-web-community/README.md)

## For testers

If you want to set up a local instance to test the project, please follow these instructions:

### Install docker

[Get Docker](https://docs.docker.com/get-docker/)

Linux:

```
$ sudo mkdir -p /etc/apt/keyrings/
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
$ echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
$ sudo apt update && sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin
$ sudo adduser <your-oxe-user> docker
$ newgrp docker
# If you want to verify your docker install run: docker run hello-world
```

### Install and run the openXeco containers and its dependencies

```
$ docker network create openxeco
$ docker run -d \
    --network openxeco \
    --network-alias mariadb \
    -p 3306:3306 \
    -e MARIADB_ROOT_PASSWORD=E4syPass \
    mariadb:10.7.3
$ docker run -d \
  --network openxeco \
  --network-alias smtp \
  -p 1025:1025 \
  -p 1080:1080 \
  reachfive/fake-smtp-server
$ docker build \
    -f openxeco-core-oxe-web-admin/Dockerfile \
    -t oxe-web-admin \
    --build-arg TARGET_DIR=openxeco-core-oxe-web-admin \
    https://github.com/CybersecurityLuxembourg/openxeco-core/releases/latest/download/openxeco-core-oxe-web-admin.tar.gz
$ docker run -d -p 3000:80 oxe-web-admin
$ docker build \
    -f openxeco-core-oxe-web-community/Dockerfile \
    -t oxe-web-community \
    --build-arg TARGET_DIR=openxeco-core-oxe-web-community \
    https://github.com/CybersecurityLuxembourg/openxeco-core/releases/latest/download/openxeco-core-oxe-web-community.tar.gz
$ docker run -d -p 3001:80 oxe-web-community
$ docker run -d -p 5000:5000 \
    --network openxeco \
    -e ENVIRONMENT=dev \
    -e JWT_SECRET_KEY=my_secret_developer_key \
    -e DB_HOSTNAME=mariadb \
    -e DB_PORT=3306 \
    -e DB_NAME=OPENXECO \
    -e DB_USERNAME=root \
    -e DB_PASSWORD=E4syPass \
    -e MAIL_SERVER=smtp \
    -e MAIL_PORT=1025 \
    -e MAIL_USE_TLS=True \
    -e MAIL_USE_SSL=False \
    -e MAIL_DEFAULT_SENDER=my-default-sender@example.org \
    -e IMAGE_FOLDER=/image_folder \
    -e DOCUMENT_FOLDER=/document_folder \
    -e INITIAL_ADMIN_EMAIL=my-default-admin@example.org \
    ghcr.io/cybersecurityluxembourg/openxeco-core-oxe-api:latest
```

### Install the app for dev with use docker-compose

- Run `docker-compose up`. Optionally can be used `-d` option to run as daemon.


### Enjoy the solution

Access the administrator interface:
- http://localhost:3000

Access the community interface:
- http://localhost:3001

Access the API documentation:
- http://localhost:5000
<br /><small>Note: if you are using Mac maybe port 5000 will be already in use. (check [solution](https://medium.com/pythonistas/port-5000-already-in-use-macos-monterey-issue-d86b02edd36c))</small>

Access the emails sent on the SMTP mock:
- http://localhost:1080

An initial account is created with the following email: "my-default-admin@example.org"
And a default password: "password"

## For production server

To set up the production instance, please see this file:

- [doc/INSTALL_SERVER.md](doc/INSTALL_SERVER.md)
