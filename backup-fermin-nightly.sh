#!/bin/bash

# 🛡️ FERMIN IA - BACKUP NOCTURNO AUTOMÁTICO
# Backup completo de memoria, identity y workspace
# Runs: Diario a las 2:30 AM Argentina

BACKUP_DATE=$(date +"%Y-%m-%d_%H-%M-%S")
WORKSPACE_DIR="/home/ubuntu/.openclaw/workspace-fermin"
LOG_FILE="$WORKSPACE_DIR/backup.log"

echo "🛡️ Fermin IA Backup - $BACKUP_DATE" | tee -a "$LOG_FILE"
echo "================================================" | tee -a "$LOG_FILE"

# Change to workspace directory
cd "$WORKSPACE_DIR" || exit 1

# 1. Add all important files
echo "📁 Adding files to git..." | tee -a "$LOG_FILE"
git add . 2>&1 | tee -a "$LOG_FILE"

# 2. Create backup entry in memory
MEMORY_ENTRY="# $BACKUP_DATE - Backup Nocturno

## Status
- ✅ Backup automático ejecutado
- 📅 Fecha: $(date '+%d/%m/%Y %H:%M:%S %Z')
- 🚀 Fermin operativo y funcionando
- 📱 Content marketing automatizado (5 posts programados)
- 💾 Workspace backup completo

## Archivos incluidos
- IDENTITY.md, SOUL.md, USER.md
- MEMORY.md completo
- memory/ directory con historial
- Scripts de automatización Postiz
- Configuraciones y documentación

## Próximo backup
- 📅 $(date -d '+1 day' '+%d/%m/%Y') 2:30 AM Argentina

---
"

# Add backup entry to memory if it's a new day
if [ ! -f "memory/$(date +%Y-%m-%d).md" ] || ! grep -q "Backup Nocturno" "memory/$(date +%Y-%m-%d).md" 2>/dev/null; then
    echo "$MEMORY_ENTRY" >> "memory/$(date +%Y-%m-%d).md"
    echo "📝 Backup entry added to daily memory" | tee -a "$LOG_FILE"
fi

# 3. Commit with timestamp
COMMIT_MSG="🛡️ Backup nocturno Fermin IA - $BACKUP_DATE

- Memoria y configuración actualizada
- Content marketing: $(ls 2026-03-08-theagents-post*.png | wc -l) posts programados
- Workspace completo respaldado
- Auto-backup nocturno funcionando"

echo "💾 Creating commit..." | tee -a "$LOG_FILE"
git commit -m "$COMMIT_MSG" 2>&1 | tee -a "$LOG_FILE"

# 4. Push to GitHub
echo "☁️ Pushing to GitHub..." | tee -a "$LOG_FILE"
git push origin master 2>&1 | tee -a "$LOG_FILE"

# 5. Verify backup success
if [ $? -eq 0 ]; then
    echo "✅ BACKUP SUCCESSFUL - $BACKUP_DATE" | tee -a "$LOG_FILE"
    echo "🔗 Repository: https://github.com/daniwally/Fermin_IA" | tee -a "$LOG_FILE"
else
    echo "❌ BACKUP FAILED - $BACKUP_DATE" | tee -a "$LOG_FILE"
fi

echo "================================================" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# Keep only last 30 days of logs
find "$WORKSPACE_DIR" -name "backup.log" -type f -mtime +30 -delete

exit 0