# GerenciaDeProyectos

Prototipo de gestión de talento humano en Python + SQLite, con una consola mejorada con Rich para navegar candidatos, contratos, reportes y utilidades de desarrollo.

**Vista general**

La aplicación centraliza operaciones básicas de administración de personal en una interfaz de consola limpia y fácil de usar. Incluye gestión de candidatos, contratos, reportes y herramientas para desarrolladores.

**Acceso por defecto**

- Usuario: `admin`
- Contraseña: `1234`

**Requisitos**

- Python 3.8+
- Dependencias listadas en `requirements.txt`

Instala las dependencias:

```powershell
python -m pip install -r requirements.txt
```

**Inicio rápido**

```powershell
python App.py
```

Al ejecutarlo, verás el menú principal con opciones para gestionar candidatos, contratos, reportes, herramientas de desarrollador y el manual integrado.

**Ruta de la base de datos**

La base de datos SQLite se crea automáticamente en `db/innovatech.db`.

**Estructura del proyecto**

- `App.py`: punto de entrada
- `db/`: inicialización y conexión a SQLite
- `services/`: lógica de negocio y acceso a datos
- `screens/`: menús y pantallas de consola
- `utils/`: utilidades compartidas
- `ManualDeUsuario.md`: guía de uso dentro del repositorio

**Funciones principales**

- Candidatos: agregar, listar, eliminar
- Contratos: generar contrato, despedir empleado, listar contratados
- Reportes: totales y listados
- Desarrollador: limpiar la base de datos, cargar datos de ejemplo

**Desarrollador / Mantenimiento**

- Limpiar la base de datos: opción en el menú de desarrollador (elimina candidatos y contratos de prueba).
- Cargar datos de ejemplo: opción para generar 10 candidatos y 4 contratos de ejemplo.

**Contribuir**

1. Haz un fork del repositorio.
2. Crea una rama con tu feature: `git checkout -b feature/nombre`
3. Añade tests si aplica y confirma que todo funciona.
4. Envía un pull request describiendo los cambios.

**Licencia**

Revisa el archivo `LICENSE` incluido en el repositorio para detalles de licencia.

**Documentación de usuario**

Consulta [ManualDeUsuario.md](ManualDeUsuario.md) para instrucciones detalladas de uso.

---

Si quieres, puedo también actualizar `requirements.txt` con versiones concretas, añadir un ejemplo de `.venv` o traducir el manual a otro idioma. ¿Qué prefieres que haga a continuación?

**Autores**

- Juan Benjumea
- Walter Peña
- Duvier Rojas Castaño


