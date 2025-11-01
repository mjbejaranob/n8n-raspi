#!/bin/bash
# Usage: ./backup-db.sh backup.sql
OUTFILE=${1:-backup.sql}
docker exec -t postgres_n8n pg_dump -U ${POSTGRES_USER:-n8n} ${POSTGRES_DB:-n8n_db} > "${OUTFILE}"
echo "Backup saved to ${OUTFILE}"
