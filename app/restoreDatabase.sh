#! /bin/bash
for ((var=1; var<=10; var++))
do
    PGPASSWORD='backup' psql -U backup -h localhost -w -d app -c "SELECT pg_terminate_backend(pg_stat_activity.pid) FROM pg_stat_activity WHERE pg_stat_activity.datname = 'app' AND pid <> pg_backend_pid()"
done
PGPASSWORD='backup' dropdb -U backup -h localhost -w -e app #Eliminamos la BD
PGPASSWORD='backup' createdb -U backup -h localhost -w -e app #Creamos la BD vacia
gunzip -c /home/ubuntu/app/media/backup.gz | PGPASSWORD='backup' psql -U backup -h localhost app