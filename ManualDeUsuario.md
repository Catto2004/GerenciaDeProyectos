# Manual de Usuario - Gestión de Talento Humano

## 1. Objetivo de la aplicación

Esta aplicación permite gestionar el ciclo completo de talento humano desde una consola mejorada con formato visual. Su propósito es centralizar el control de todos los procesos de RR.HH. incluyendo selección, contratación, nómina, afiliaciones, capacitaciones, evaluaciones e inducciones.

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
- Gestión de Recursos Humanos (submenú)
- Desarrollador
- Manual de usuario

En la mayoría de pantallas se muestra un recuadro de estatus con la última acción realizada.

## 4. Dashboard principal

Desde el dashboard puedes acceder a las funciones principales:

1. Gestionar candidatos
2. Gestión de contratos
3. Reportes
4. Gestión de Recursos Humanos
5. Desarrollador
6. Manual de usuario
7. Salir

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

### 5.3 Eliminar candidato

Primero se muestra el listado de candidatos disponibles para eliminar. Luego se solicita el ID del candidato.

Al eliminar un candidato:

- Se borra el candidato de la base de datos
- Se eliminan los contratos asociados a ese candidato

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

- Se crea el registro en la tabla de contratos
- El estado del candidato cambia a `Contratado`

### 6.2 Despedir empleado

Se muestra el listado de candidatos disponibles para despedir. Después se solicita el ID del candidato.

Al despedir un empleado:

- Se eliminan sus contratos
- El estado del candidato cambia a `Despedido`

### 6.3 Listar empleados

Muestra una tabla con los candidatos que tienen contrato activo, incluyendo:

- ID
- Nombre
- Tipo de contrato
- Fecha

## 7. Gestión de Recursos Humanos

Este submenú contiene todas las funcionalidades de talento humano:

1. Nómina y Liquidaciones
2. Afiliaciones (Seguridad Social)
3. Evaluaciones de Desempeño
4. Capacitaciones
5. Retiro de Personal
6. Inducción
7. Certificaciones Laborales
8. Pruebas Psicotécnicas
9. Verificación de Referencias
10. Volver

### 7.1 Nómina y Liquidaciones

Permite liquidar la nómina quincenal de los colaboradores:

- Ingresar novedades (descuentos, bonificaciones, horas extras)
- Crear períodos de nómina
- Liquidar nómina
- Generar informes
- Enviar desprendibles por correo

### 7.2 Afiliaciones (Seguridad Social)

Gestión de afiliaciones a:

- ARL (Aseguradora de Riesgos Laborales)
- EPS (Empresa Prestadora de Salud)
- Caja de Compensación Familiar
- Fondo de Pensiones

### 7.3 Evaluaciones de Desempeño

Realización de evaluaciones de desempeño:

- Evaluación de período de prueba (2 meses directo, 3 meses temporal)
- Evaluación anual para personal con más de 6 meses
- Registro de puntajes y comentarios
- Generación de compromisos de mejora

### 7.4 Capacitaciones

Gestión del plan de capacitación:

- Ver todas las capacitaciones
- Crear capacitación
- Registrar asistencia
- Ver asistencia por capacitación
- Cambiar estado de capacitación
- Evaluación de eficacia

### 7.5 Retiro de Personal

Proceso de retiro de empleados:

- Examen de retiro
- Carta de certificación laboral
- Carta de cesantías
- Pago de liquidación
- Carta de no renovación (30 días antes)

### 7.6 Inducción

Gestión de inducciones:

- Inducción para personal nuevo (primeros 3-5 días)
- Reinducción anual (para más de 3 meses)
- Entrenamiento (para promociones internas o cambios)
- Registro de temas cubiertos

### 7.7 Certificaciones Laborales

Generación de certificaciones laborales para:

- Colaboradores actuales
- Exempleados

### 7.8 Pruebas Psicotécnicas

Gestión de pruebas psicotécnicas:

- Registrar prueba para candidato
- Registrar resultado
- Ver historial de pruebas

### 7.9 Verificación de Referencias

Verificación de referencias laborales:

- Registrar verificación
- Registrar resultado (favorable/no favorable)
- Ver verificaciones realizadas

## 8. Reportes

La sección de reportes muestra información general del sistema.

Incluye:

- Total de candidatos
- Total de contratos
- Estado de los candidatos
- Listado de candidatos
- Listado de contratados

## 9. Desarrollador

Esta sección está pensada para tareas de mantenimiento o pruebas.

### Opciones disponibles

1. Limpiar BD
2. Cargar ejemplo
3. Volver

### 9.1 Limpiar BD

Elimina todos los candidatos y contratos registrados, dejando el sistema en cero.

### 9.2 Cargar ejemplo

Carga datos de ejemplo:

- 10 candidatos
- 4 contratos

## 10. Manual de usuario

La opción de manual dentro de la aplicación ahora abre este archivo: `ManualDeUsuario.md`.

## 11. Notas de uso

- En varias pantallas se usa una pausa antes de limpiar la consola para que puedas leer la información.
- Si no ves una tabla inmediatamente, presiona Enter cuando aparezca el aviso de continuación.
- La opción de desarrollador puede borrar los datos actuales, así que úsala con cuidado.
- Todas las fechas se manejan en formato AAAA-MM-DD
- Los estados posibles para candidatos: Registrado, Evaluado, Contratado, Despedido

## 12. Estructura técnica resumida

- `App.py`: punto de entrada de la aplicación
- `db/database.py`: conexión e inicialización de la base de datos
- `services/`: lógica de negocio y acceso a datos
- `screens/`: pantallas y menús de consola
- `utils/`: utilidades de pantalla y estatus

## 13. Flujo recomendado

1. Inicia sesión con el usuario por defecto
2. Revisa el dashboard
3. Gestiona candidatos (agregar, listar)
4. Realiza selección (pruebas psicotécnicas, verificación de referencias)
5. Genera contratos
6. Gestiona nómina y afiliaciones
7. Ejecuta inducciones
8. Planifica capacitaciones
9. Realiza evaluaciones de desempeño
10. Consulta reportes

## 14. Cierre

Para salir de la aplicación, usa la opción `7 - Salir` del dashboard principal.
