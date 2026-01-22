#!/bin/bash

# --- Configuration Section ---
# Source directory where logs are stored
LOG_DIR="/home/serverpp/monitor/one_project/meus_logs"
# Target directory for backup files
BACKUP_DIR="/home/serverpp/backups_monitor"
# Generate a timestamp for unique filenames
TIMESTAMP=$(date +%Y-%m-%d_%H-%M)

# 1. Create the backup directory if it doesn't exist
mkdir -p "$BACKUP_DIR"

# 2. Compress the logs into a .tar.gz file to save disk space
# -c: create, -z: compress (gzip), -f: filename
tar -czf "$BACKUP_DIR/log_backup_$TIMESTAMP.tar.gz" -C "$LOG_DIR" .

# 3. Retention Policy: Remove backups older than 7 days
find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +7 -delete

echo "Backup completed successfully at: $BACKUP_DIR/log_backup_$TIMESTAMP.tar.gz"
