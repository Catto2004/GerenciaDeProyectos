# Manual de Usuario

## 1. Objetivo de la aplicación

Esta aplicación permite gestionar candidatos, contratos, reportes y acciones de administración desde una consola mejorada con formato visual. Su propósito es centralizar el control del ciclo básico de talento humano en una interfaz simple de usar.

## 2. Acceso al sistema

Al iniciar la aplicación se solicita autenticación.

Credenciales por defecto:

- Usuario: `admin`
- Contraseña: `1234`

Si las credenciales son correctas, se ingresa al dashboard principal.

## 3. Estructura general

La aplicación se organiza en estas secciones:

- Dashboard principal
- Gestión de candidatos
- Gestión de contratos
- Reportes
- Desarrollador
- Manual de usuario

En la mayoría de pantallas se muestra un recuadro de estatus con la última acción realizada.

## 4. Dashboard principal

Desde el dashboard puedes acceder a las funciones principales:

1. Gestionar candidatos
2. Gestión de contratos
3. Reportes
4. Desarrollador
5. Manual de usuario
6. Salir

El dashboard también muestra el total de candidatos y contratos registrados.

## 5. Gestión de candidatos

Esta sección permite administrar los candidatos registrados.

### Opciones disponibles

1. Agregar candidato
2. Listar candidatos
3. Eliminar candidato
4. Volver

### 5.1 Agregar candidato

Solicita los siguientes datos:

- Nombre
- Correo
- Teléfono

Al guardar, se crea un nuevo candidato con estado inicial `Registrado`.

### 5.2 Listar candidatos

Muestra una tabla con:

- ID
- Nombre
- Correo
- Teléfono
- Estado

Al terminar, la pantalla espera confirmación para no borrar la información inmediatamente.

### 5.3 Eliminar candidato

Primero se muestra el listado de candidatos disponibles para eliminar. Luego se solicita el ID del candidato.

Al eliminar un candidato:

- se borra el candidato de la base de datos
- se eliminan los contratos asociados a ese candidato

## 6. Gestión de contratos

Esta sección permite administrar contratos y empleados contratados.

### Opciones disponibles

1. Generar contrato
2. Despedir empleado
3. Listar empleados
4. Volver

### 6.1 Generar contrato

Se muestra primero el listado de candidatos disponibles para contratar.

Luego se solicita:

- ID del candidato
- Tipo de contrato (`Temporal` o `Indefinido`)

Al generar el contrato:

- se crea el registro en la tabla de contratos
- el estado del candidato cambia a `Contratado`

### 6.2 Despedir empleado

Se muestra el listado de candidatos disponibles para despedir. Después se solicita el ID del candidato.

Al despedir un empleado:

- se eliminan sus contratos
- el estado del candidato cambia a `Despedido`

### 6.3 Listar empleados

Muestra una tabla con los candidatos que tienen contrato activo, incluyendo:

- ID
- Nombre
- Tipo de contrato
- Fecha

## 7. Reportes

La sección de reportes muestra información general del sistema.

Incluye:

- total de candidatos
- total de contratos
- estado de los candidatos
- listado de candidatos
- listado de contratados

La pantalla se mantiene visible hasta que presiones Enter.

## 8. Desarrollador

Esta sección está pensada para tareas de mantenimiento o pruebas.

### Opciones disponibles

1. Limpiar BD
2. Cargar ejemplo
3. Volver

### 8.1 Limpiar BD

Elimina todos los candidatos y contratos registrados, dejando el sistema en cero.

### 8.2 Cargar ejemplo

Carga datos de ejemplo:

- 10 candidatos
- 4 contratos

## 9. Manual de usuario

La opción de manual dentro de la aplicación ahora abre este archivo: `ManualDeUsuario.md`.

## 10. Notas de uso

- En varias pantallas se usa una pausa antes de limpiar la consola para que puedas leer la información.
- Si no ves una tabla inmediatamente, presiona Enter cuando aparezca el aviso de continuación.
- La opción de desarrollador puede borrar los datos actuales, así que úsala con cuidado.

## 11. Estructura técnica resumida

- `App.py`: punto de entrada de la aplicación
- `db/database.py`: conexión e inicialización de la base de datos
- `services/`: lógica de negocio y acceso a datos
- `screens/`: pantallas y menús de consola
- `utils/`: utilidades de pantalla y estatus

## 12. Flujo recomendado

1. Inicia sesión con el usuario por defecto
2. Revisa el dashboard
3. Agrega o lista candidatos
4. Genera contratos
5. Consulta reportes
6. Usa el manual cuando necesites ayuda

## 13. Cierre

Para salir de la aplicación, usa la opción `6 - Salir` del dashboard principal.
