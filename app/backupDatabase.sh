#! /bin/bash
PGPASSWORD='backup' pg_dump -U backup -h localhost -w app  | gzip >  "/home/ubuntu/app/media/backup.gz"