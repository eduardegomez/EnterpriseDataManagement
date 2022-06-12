#! /bin/bash
mkdir -p /home/ubuntu/app/databaseBackups/compressed
date=$(date '+%Y%m%dT%H')
PGPASSWORD='backup' pg_dump -U backup -h localhost -w app  | gzip >  "/home/ubuntu/app/databaseBackups/compressed/$date.gz"