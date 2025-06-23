
# 🛠️ Panel CLI en 15 Minutos con Python + Bash

Automatiza tu sistema con un **panel de control en terminal** hecho en Python y Bash.  
Con este proyecto puedes:
- Ver el estado del sistema (CPU, RAM, Disco)
- Gestionar tareas (añadir, listar, eliminar)
- Ejecutar scripts o comandos favoritos
- Añadir y eliminar scripts desde el panel

---

## 📂 Estructura del Proyecto

```text
cli_dashboard/
├── main.py               # Lógica del panel CLI
├── utils/
│   └── db.py             # Gestión de tareas en JSON
├── scripts/
│   └── launch.sh         # Script para iniciar el panel
├── scripts.json          # Scripts favoritos configurables
└── tareas.json           # Tareas almacenadas (se crea automáticamente)
```

---

## 🚀 Instalación y Ejecución

### 1. Clona el repositorio:
```bash
git clone https://github.com/Damian-Pxws/ControlPanelTerminal.git
cd cli_dashboard
```

### 2. Crea y activa el entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instala dependencias:
```bash
pip install rich psutil
```

### 4. Da permisos al script de inicio:
```bash
chmod +x scripts/launch.sh
```

### 5. Inicia el panel:
```bash
./scripts/launch.sh
```

---

## ⚙️ Tecnologías Usadas

- Python 3
- Bash
- Librerías: `psutil`, `rich`, `json`, `subprocess`
- Opcional: SQLite si deseas guardar historial (no incluido aún)

---

## 📜 Licencia

Este proyecto está licenciado bajo la **Apache 2.0 License**.  
Consulta el archivo [LICENSE](./LICENSE) para más detalles.
