# Postgresql image
Pull docker image, start docker container for pg:

```
docker run -p 5432:5432 --name pg-docker-protected -e POSTGRES_PASSWORD=<password>  postgres
```

NOTE: `docker run -p 5432:5432 --name pg-docker postgres` <- cannot start without password

Note: Database is uninitialized and superuser password is not specified.

![alt text](image.png)

To start existing docker

Solution #1: Use Docker Desktop  (UI)

Solution #2: Use command line
1. Get list of all docker containers
```
docker ps -a
```

2. Find ID of your container and start it
```
docker start bb4dbb063dc4
```

or

```
docker start -ai bb4dbb063dc4
```

or by name
```
docker start pg-docker-protected
```
![alt text](image-1.png)


# pg-admin image (same as DBeaver for MySQL)

```
docker run -p 5555:80 --name pg-admin -e PGADMIN_DEFAULT_EMAIL="<email>" -e PGADMIN_DEFAULT_PASSWORD=<password> dpage/pgadmin4
```

![alt text](image-2.png)

Connect to postgresql container running on the same machine, use `host.docker.internal` as host name/address:

![alt text](image-3.png)



# Inside container

In Docker Desktop navigate to `exec` window (container bash) and connect to postgres
```
psql -h localhost -U postgres
```

List all DBs:

```
\l
```

![alt text](image-4.png)

```
CREATE DATABASE <db_name>;
\c <db_name>
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane@example.com');
```
![alt text](image-6.png)
![alt text](image-7.png)



```
docker exec -it test_pg bash
psql -U postgres
CREATE SCHEMA ts;
CREATE TABLE ts.test_tab (id serial primary key, val int, task text);
INSERT INTO ts.test_tab (val,task) values (1,'abc'), (2, 'def');
SELECT * FROM ts.test_tab;
\q
```

Note: to install `psycopg2`, postgresql installation is required, even if you run it in a container,see https://stackoverflow.com/questions/33866695/error-installing-psycopg2-on-macos-10-9-5

![alt text](image-8.png)

```
brew install postgresql
export PATH=/Applications/Postgres.app/Contents/Versions/@latest/bin/:$PATH
```


https://www.psycopg.org/docs/


