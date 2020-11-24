## Docker compose networking with multiple hosts example

docker-compose.yaml contains two containers, a api that connects to the PostgreSQL DB

Run `docker-compose build` and then `docker-compose up` to get the containers up and running.
View the docker networks with `docker network list`

Reach the API with `curl http://127.0.0.1:5000/database` and look at the output of the containers.

You should see the following if a connection was made from the `api` container to the `database` container:

```
database_1  | 2020-11-23 20:40:42.046 UTC [32] FATAL:  password authentication failed for user "postgres"
database_1  | 2020-11-23 20:40:42.046 UTC [32] DETAIL:  Password does not match for user "postgres".
database_1  | 	Connection matched pg_hba.conf line 99: "host all all all md5"
```