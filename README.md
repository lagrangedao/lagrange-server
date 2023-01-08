#  Lagrange server
lagrange-server is the Python Backend for lagrange platform

## Backend Deployment
### create your own .env
copy _.env.template_ to _.env_

update the filed to your own value.

### Start the server

```shell
chmod +x run-server.sh
./run-server.sh
```

You need to change the _DOMAIN_ value to your ip, if you want to deploy it as a server on production

# Frontend Deployment

```shell
cd web
docker build -t lagrangedao/lagrange-dao-web . 
docker run  -p 8082:8082 lagrangedao/lagrange-dao-web
```

Now you can visit the site at http://127.0.0.1:8082

