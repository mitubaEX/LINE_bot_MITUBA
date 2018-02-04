#!/bin/sh
. ./env_var.txt

docker-compose up -d
# sleep 20s
until mysqladmin ping -h 0.0.0.0 --silent;
do
    echo 'waiting for mysqld to be connectable...'
    sleep 1s
done
docker exec --interactive dbserver mysql --host localhost --default-character-set=utf8mb4 --user=root --password=PASSWORD line_bot < data.sql
python3 index.py
