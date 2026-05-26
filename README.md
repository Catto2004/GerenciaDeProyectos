# GerenciaDeProyectos

> Prototipo de gestión de talento humano en Python + SQLite, con una consola mejorada con Rich para navegar candidatos, contratos, reportes y utilidades de desarrollo.

## Vista general

La aplicación centraliza operaciones básicas de administración de personal en una interfaz de consola limpia, ordenada y fácil de usar. Incluye:

- gestión de candidatos
- generación y administración de contratos
- reportes resumidos
- panel de desarrollador para limpieza y carga de datos de ejemplo
- manual de usuario integrado desde la app

## Acceso por defecto

- Usuario: `admin`
- Contraseña: `1234`

## Menú principal

1. Gestionar candidatos
2. Gestión de contratos
3. Reportes
4. Desarrollador
5. Manual de usuario
6. Salir

## Funciones destacadas

### Candidatos

- agregar candidatos
- listar candidatos
- eliminar candidatos

### Contratos

- generar contrato para un candidato
- despedir empleado
- listar empleados contratados

### Reportes

- total de candidatos
- total de contratos
- candidatos por estado
- listado de candidatos
- listado de contratados

### Desarrollador

- limpiar la base de datos
- cargar 10 candidatos y 4 contratos de ejemplo

## Manual de usuario

El manual detallado de uso está disponible dentro del proyecto en:

- [ManualDeUsuario.md](ManualDeUsuario.md)

También puede abrirse desde la opción `5 - Manual de usuario` dentro de la app.

## Inicio rápido

```powershell
python App.py
```

## Estructura del proyecto

- `App.py`: punto de entrada de la aplicación
- `db/`: inicialización y conexión a SQLite
- `services/`: lógica de negocio y acceso a datos
- `screens/`: menús y pantallas de consola
- `utils/`: utilidades compartidas de pantalla y estatus
- `ManualDeUsuario.md`: documentación detallada del uso

## Datos y persistencia

La base de datos se crea automáticamente en `db/innovatech.db`.

Si usas la opción de desarrollador para limpiar la BD, se eliminan candidatos y contratos para reiniciar el sistema.

## Nota

Este proyecto está pensado como base académica y se puede ampliar con autenticación más robusta, validaciones adicionales y nuevas vistas de administración.


