



# 🧪 Pruebas automáticas en FastAPI (VS Code)

Este proyecto usa `pytest` para ejecutar pruebas del backend.

## 🔧 Ejecutar TODOS los tests

1. Abre la paleta de comandos: `Ctrl + Shift + P`
2. Escribe: `Run Task`
3. Elige: `Run ALL tests`

O desde terminal (PowerShell):

```powershell
$env:PYTHONPATH = "."
pytest

🔍 Ejecutar un test específico
Edita el task llamado:

json
Copiar
Editar
"Run specific test (edit args)"
Y cambia la línea "command": ... por el test que deseas correr, por ejemplo:

bash
Copiar
Editar
pytest tests/test_proyectos.py::test_crear_proyecto_exitoso

$env:PYTHONPATH = "."
pytest tests/test_comentarios.py 