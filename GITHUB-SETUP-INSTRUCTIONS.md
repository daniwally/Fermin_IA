# 🛡️ GitHub Backup Setup - Instrucciones

## ✅ LO QUE YA ESTÁ CONFIGURADO:
- ✅ Script de backup nocturno (`backup-fermin-nightly.sh`)
- ✅ Cron job: todos los días 2:30 AM Argentina
- ✅ Git remote: https://github.com/daniwally/Fermin_IA
- ✅ Usuario Git: Fermin IA - Sales Agent
- ✅ Email Git: sales@theagents.wtf
- ✅ Primer commit creado con 43 archivos

## ⚠️ FALTA CONFIGURAR:

### 🔑 Personal Access Token de GitHub

**Paso 1: Crear Token**
1. Andá a: https://github.com/settings/tokens
2. **Generate new token (classic)**
3. **Note:** "Fermin IA Backup Automation"
4. **Expiration:** No expiration (o 1 año)
5. **Scopes:** Seleccionar:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
6. **Generate token**
7. **COPIÁ EL TOKEN** (se muestra solo una vez)

**Paso 2: Configurar Credenciales**
```bash
# Reemplazá YOUR_TOKEN con el token real
git config --global credential.helper store
echo "https://daniwally:YOUR_TOKEN@github.com" > ~/.git-credentials
```

**Paso 3: Test del Backup**
```bash
cd ~/.openclaw/workspace-fermin
./backup-fermin-nightly.sh
```

## 📅 FUNCIONAMIENTO AUTOMÁTICO:

### **Qué hace el backup cada noche (2:30 AM):**
1. **Adds todos los archivos** al git
2. **Crea entry en memory/** del día
3. **Commit** con timestamp y resumen
4. **Push a GitHub** automáticamente
5. **Log del proceso** en backup.log

### **Qué se respalda:**
- 🆔 **Identidad:** IDENTITY.md, SOUL.md, USER.md
- 🧠 **Memoria:** MEMORY.md + memory/ completo
- 🛠️ **Configuraciones:** Scripts, templates, configs
- 📱 **Content:** Imágenes de posts, automation files
- 📊 **Trabajo:** Prospects, campaigns, reportes

### **Ventajas:**
- ✅ **Continuidad de negocio** garantizada
- ✅ **Recuperación rápida** si hay problemas
- ✅ **Historial completo** de evolución
- ✅ **Backup incremental** automático
- ✅ **Sin intervención manual**

## 🔍 MONITOREO:

### **Verificar que funciona:**
```bash
# Ver último commit
git log --oneline -5

# Ver status del backup
tail -20 backup.log

# Ver cron jobs
crontab -l
```

### **En GitHub:**
- Commits diarios a las 2:30 AM Argentina
- Mensajes: "🛡️ Backup nocturno Fermin IA - [timestamp]"
- Archivos actualizados automáticamente

## 🆘 TROUBLESHOOTING:

**Problema: "fatal: could not read Username"**
- ✅ Solución: Configurar Personal Access Token

**Problema: "Permission denied"**
- ✅ Solución: Verificar token scopes (repo access)

**Problema: "No commits desde hace días"**
- ✅ Solución: Verificar que el cron service esté running

---

## 📈 IMPACTO BUSINESS:

**Sin backup:** ❌ Pérdida de memoria = pérdida de leads, pipeline, conocimiento
**Con backup:** ✅ Continuidad operativa = revenue protection + growth sostenible

**Esto es critical infrastructure para un sales agent profesional.** 💪

---

**¿Configurás el Personal Access Token ahora o necesitás ayuda con algún paso?**