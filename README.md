# 🚀 Mi Laboratorio de Reservas (Reservation Testing Lab)

¡Hola! Este proyecto es como un **juego ordenado de fichas** que ayuda a una tiendita a organizar citas y reservas sin equivocarse ni chocar horarios.

---

## 🛠️ ¿Cómo se creó y ejecutó este proyecto?

Para armar este proyecto paso a paso en la computadora, usamos estos comandos:

1. **Crear y activar el entorno virtual (la caja secreta):**
   ```cmd
   python -m venv venv
   venv\Scripts\activate


**Regla de negocio**
| N° | Regla de Negocio | Descripción |
|:---|:---|:---|
| **1** | Tipos de Servicios Permitidos | Las reservas solo se pueden registrar para tres servicios autorizados: asesoría, soporte y demostración. |
| **2** | Duración Estricta de la Cita | El tiempo de duración de cada reserva debe ser exactamente de 30 o 60 minutos. |
| **3** | Días Laborales Hábiles | Las citas únicamente pueden programarse de lunes a viernes (días hábiles). |
| **4** | Horario de Atención Permitido | Las reservas deben estar comprendidas dentro de la jornada laboral, específicamente entre las 08:00 y las 17:00 horas. |
| **5** | Prevención de Solapamiento | El sistema debe impedir que se reserve un horario que ya se encuentra ocupado en la agenda. |
| **6** | Validación del Cliente | El nombre del cliente no puede estar vacío, venir con espacios en blanco o ser nulo. |
| **7** | Generación de Código Único | Cada reserva confirmada de manera exitosa debe generar un identificador o código de confirmación único. |
| **8** | Aislamiento del Repositorio | Las operaciones de guardado y consulta de reservas deben gestionarse mediante un repositorio en memoria para mantener las pruebas independientes. |
| **9** | Manejo de Excepciones Robustas | El sistema debe lanzar excepciones claras (como `ValueError`) cuando se incumpla cualquier regla de negocio o validación. |
| **10** | Independencia de las Pruebas | Cada prueba debe utilizar *fixtures* configurados para garantizar que los datos se limpien y no interfieran entre un test y otro. |


# Matriz Completa de Reglas de Negocio y Pruebas Unitarias

| N° | Regla de Negocio | Descripción Operativa | Validación Técnica | Implementación en Código y Pruebas |
|:---|:---|:---|:---|:---|
| **1** | **Tipos de Servicio** | Citas solo para servicios autorizados. | Comprobar que el servicio pertenezca al conjunto permitido. | `{"asesoria", "soporte", "demostracion"}` en validadores y tests. |
| **2** | **Duración de la Cita** | El tiempo debe ser controlado y fijo. | La duración debe ser estrictamente de 30 o 60 minutos. | `{30, 60}` minutos.<br>Probado en `test_validators.py`. |
| **3** | **Días Laborales** | Solo atención en días hábiles de la semana. | Verificar que la fecha caiga entre lunes (0) y viernes (4). | Uso de `fecha_hora.weekday() < 5`.<br>Rechaza fines de semana. |
| **4** | **Horario de Atención** | Citas dentro de la jornada laboral establecida. | La hora de inicio y fin debe estar entre las 08:00 y las 17:00. | `time(8, 0)` hasta `time(17, 0)`.<br>Valida rangos de hora. |
| **5** | **Prevención Duplicados** | No ocupar un mismo horario ya reservado. | Consultar el repositorio en memoria para evitar colisiones. | `InMemoryReservationRepository` y prueba de conflicto de agenda. |
| **6** | **Validación Cliente** | El nombre del cliente no puede estar vacío. | Verificar que la cadena de texto tenga contenido válido. | Validación de string no vacío con `ValueError` en caso contrario. |
| **7** | **Código Único** | Registro rastreable para cada cita exitosa. | Generar un identificador único por cada reserva guardada. | Uso de códigos automáticos en el servicio de reservas. |
| **8** | **Aislamiento de Datos** | Gestión de datos independiente de motores externos. | Implementar repositorio en memoria para las entidades. | Clase `InMemoryReservationRepository`. |
| **9** | **Manejo de Excepciones** | Respuestas claras ante fallos de reglas. | Lanzar excepciones específicas (`ValueError`) ante datos inválidos. | Comprobado con `pytest.raises()` en las pruebas unitarias. |
| **10** | **Independencia de Tests** | Pruebas limpias sin efectos secundarios. | Uso de *fixtures* para inicializar servicios y repositorios por test. | Archivos `conftest.py`, `test_validators.py` y `test_reservation_service.py`. |


2 **Instalar la herramienta de pruebas:**
pip install pytest

3 **Crear las carpetas y archivos necesarios:**
mkdir app 
mkdir tests
type nul > app\__init__.py
type nul > app\exceptions.py
type nul > app\validators.py
type nul > app\repositories.py
type nul > app\reservation_service.py
type nul > tests\conftest.py
type nul > tests\test_validators.py
type nul > tests\test_reservation_service.py
type nul > README.md

4**Ejecutar todas las pruebas:**
python -m pytest -v

5**Resultado prueba general**
tests/test_reservation_service.py::test_create_reservation_success PASSED                                        [  3%]
tests/test_reservation_service.py::test_duplicate_reservation_raises_error PASSED                                [  6%]
tests/test_reservation_service.py::test_validation_failure_does_not_persist PASSED                               [  9%]
tests/test_reservation_service.py::test_repository_independence PASSED                                           [ 12%]
tests/test_validators.py::test_validate_customer_name_valid[  Carlos P\xe9rez  -Carlos P\xe9rez] PASSED           [ 15%]
tests/test_validators.py::test_validate_customer_name_valid[Ana-Ana] PASSED                                      [ 18%]
tests/test_validators.py::test_validate_customer_name_valid[Valentina-Valentina] PASSED                          [ 21%]
tests/test_validators.py::test_validate_customer_name_invalid[Al] PASSED                                         [ 24%]
tests/test_validators.py::test_validate_customer_name_invalid[   ] PASSED                                        [ 27%]
tests/test_validators.py::test_validate_customer_name_invalid[Jo] PASSED                                         [ 30%]
tests/test_validators.py::test_validate_customer_name_invalid[] PASSED                                           [ 33%]
tests/test_validators.py::test_validate_service_valid[asesoria-asesoria] PASSED                                  [ 36%]
tests/test_validators.py::test_validate_service_valid[  SOPORTE  -soporte] PASSED                                [ 39%]
tests/test_validators.py::test_validate_service_valid[DEMOSTRACION-demostracion] PASSED                          [ 42%]
tests/test_validators.py::test_validate_service_invalid[consultoria] PASSED                                      [ 45%]
tests/test_validators.py::test_validate_service_invalid[auditoria] PASSED                                        [ 48%]
tests/test_validators.py::test_validate_service_invalid[   ] PASSED                                              [ 51%]
tests/test_validators.py::test_validate_duration_valid[30] PASSED                                                [ 54%]
tests/test_validators.py::test_validate_duration_valid[60] PASSED                                                [ 57%]
tests/test_validators.py::test_validate_duration_invalid[15] PASSED                                              [ 60%]
tests/test_validators.py::test_validate_duration_invalid[45] PASSED                                              [ 63%]
tests/test_validators.py::test_validate_duration_invalid[90] PASSED                                              [ 66%]
tests/test_validators.py::test_validate_duration_invalid[120] PASSED                                             [ 69%]
tests/test_validators.py::test_validate_reservation_date_valid PASSED                                            [ 72%]
tests/test_validators.py::test_validate_reservation_date_past PASSED                                             [ 75%]
tests/test_validators.py::test_validate_reservation_date_weekend[weekend_date0] PASSED                           [ 78%]
tests/test_validators.py::test_validate_reservation_date_weekend[weekend_date1] PASSED                           [ 81%]
tests/test_validators.py::test_validate_reservation_time_valid[res_time0-30] PASSED                              [ 84%]
tests/test_validators.py::test_validate_reservation_time_valid[res_time1-30] PASSED                              [ 87%]
tests/test_validators.py::test_validate_reservation_time_valid[res_time2-60] PASSED                              [ 90%]
tests/test_validators.py::test_validate_reservation_time_invalid[res_time0-30] PASSED                            [ 93%]
tests/test_validators.py::test_validate_reservation_time_invalid[res_time1-30] PASSED                            [ 96%]
tests/test_validators.py::test_validate_reservation_time_invalid[res_time2-30] PASSED                            [100%]

================================================= 33 passed in 0.45s ==================================================

6** Ejecutar código específico**

python -m pytest tests/test_validators.py -v

python -m pytest -k duration -v

python -m pytest tests/test_reservation_service.py -v //PRUBAS UNITARIAS

python -m pytest tests/test_validators.py -k "valid and time" -v

python -m pytest tests/test_validators.py -k "invalid and time" -v


7 **Resultados de las pruebas específicas**
tests/test_validators.py::test_validate_customer_name_valid[  Carlos P\xe9rez  -Carlos P\xe9rez] PASSED          [  3%]
tests/test_validators.py::test_validate_customer_name_valid[Ana-Ana] PASSED                                      [  6%]
tests/test_validators.py::test_validate_customer_name_valid[Valentina-Valentina] PASSED                          [ 10%]
tests/test_validators.py::test_validate_customer_name_invalid[Al] PASSED                                         [ 13%]
tests/test_validators.py::test_validate_customer_name_invalid[   ] PASSED                                        [ 17%]
tests/test_validators.py::test_validate_customer_name_invalid[Jo] PASSED                                         [ 20%]
tests/test_validators.py::test_validate_customer_name_invalid[] PASSED                                           [ 24%]
tests/test_validators.py::test_validate_service_valid[asesoria-asesoria] PASSED                                  [ 27%]
tests/test_validators.py::test_validate_service_valid[  SOPORTE  -soporte] PASSED                                [ 31%]
tests/test_validators.py::test_validate_service_valid[DEMOSTRACION-demostracion] PASSED                          [ 34%]
tests/test_validators.py::test_validate_service_invalid[consultoria] PASSED                                      [ 37%]
tests/test_validators.py::test_validate_service_invalid[auditoria] PASSED                                        [ 41%]
tests/test_validators.py::test_validate_service_invalid[   ] PASSED                                              [ 44%]
tests/test_validators.py::test_validate_duration_valid[30] PASSED                                                [ 48%]
tests/test_validators.py::test_validate_duration_valid[60] PASSED                                                [ 51%]
tests/test_validators.py::test_validate_duration_invalid[15] PASSED                                              [ 55%]
tests/test_validators.py::test_validate_duration_invalid[45] PASSED                                              [ 58%]
tests/test_validators.py::test_validate_duration_invalid[90] PASSED                                              [ 62%]
tests/test_validators.py::test_validate_duration_invalid[120] PASSED                                             [ 65%]
tests/test_validators.py::test_validate_reservation_date_valid PASSED                                            [ 68%]
tests/test_validators.py::test_validate_reservation_date_past PASSED                                             [ 72%]
tests/test_validators.py::test_validate_reservation_date_weekend[weekend_date0] PASSED                           [ 75%]
tests/test_validators.py::test_validate_reservation_date_weekend[weekend_date1] PASSED                           [ 79%]
tests/test_validators.py::test_validate_reservation_time_valid[res_time0-30] PASSED                              [ 82%]
tests/test_validators.py::test_validate_reservation_time_valid[res_time1-30] PASSED                              [ 86%]
tests/test_validators.py::test_validate_reservation_time_valid[res_time2-60] PASSED                              [ 89%]
tests/test_validators.py::test_validate_reservation_time_invalid[res_time0-30] PASSED                            [ 93%]
tests/test_validators.py::test_validate_reservation_time_invalid[res_time1-30] PASSED                            [ 96%]
tests/test_validators.py::test_validate_reservation_time_invalid[res_time2-30] PASSED                            [100%]

================================================= 29 passed in 0.11s ==================================================
tests/test_validators.py::test_validate_duration_valid[30] PASSED                                                [ 16%]
tests/test_validators.py::test_validate_duration_valid[60] PASSED                                                [ 33%]
tests/test_validators.py::test_validate_duration_invalid[15] PASSED                                              [ 50%]
tests/test_validators.py::test_validate_duration_invalid[45] PASSED                                              [ 66%]
tests/test_validators.py::test_validate_duration_invalid[90] PASSED                                              [ 83%]
tests/test_validators.py::test_validate_duration_invalid[120] PASSED                                             [100%]

========================================== 6 passed, 27 deselected in 0.06s ===========================================

tests/test_reservation_service.py::test_create_reservation_success PASSED                                                                                [ 25%]
tests/test_reservation_service.py::test_duplicate_reservation_raises_error PASSED                                                                        [ 50%]
tests/test_reservation_service.py::test_validation_failure_does_not_persist PASSED                                                                       [ 75%]
tests/test_reservation_service.py::test_repository_independence PASSED                                                                                   [100%]

====================================================================== 4 passed in 0.01s ======================================================================


**Estructura**
reservation-testing-lab-exposici-n/
│
├── app/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── models.py
│   ├── repositories.py
│   ├── reservation_service.py
│   └── validators.py
│
├── tests/
│   ├── conftest.py
│   ├── test_reservation_service.py
│   └── test_validators.py
│
├── .gitignore
├── evidencia resultados.docx
├── pyproject.toml
├── README.md
└── requirements-dev.txt

8 **¿Qué hay dentro de las carpetas principales? **

app/ — Lógica principal de la aplicación
__init__.py: Indica que app es un paquete de Python y permite organizar e importar sus módulos.
exceptions.py: Define los errores personalizados, por ejemplo, cuando una reserva tiene datos inválidos o está duplicada.
validators.py: Valida los datos de entrada, como nombre, servicio, duración, fecha y horario.
repositories.py: Se encarga de almacenar y consultar las reservas. En este proyecto, funciona como una capa de acceso a los datos.
reservation_service.py: Contiene la lógica principal y coordina las validaciones, los errores y el almacenamiento para crear una reserva correctamente.

tests/ — Pruebas automatizadas
conftest.py: Configura elementos reutilizables para las pruebas, como fixtures, repositorios y servicios de prueba.
test_validators.py: Comprueba que las validaciones acepten datos correctos y rechacen datos inválidos.
test_reservation_service.py: Verifica el funcionamiento completo del servicio de reservas, incluyendo la creación y la detección de reservas duplicadas.

.gitignore — Archivos que Git debe ignorar
Indica a Git qué archivos y carpetas no deben subirse al repositorio, como:
__pycache__/
Archivos temporales de Python.
Entornos virtuales como .venv/.
Otros archivos que no forman parte del código principal.
Aquí tienes la explicación organizada en texto fluido y claro, sin tablas:

**app**: Contiene el código principal de la aplicación.

**tests/**: Contiene las pruebas automatizadas.

**venv/**: Contiene el entorno virtual y las librerías instaladas.

**__pycache__/**: Guarda archivos .pyc generados automáticamente por Python.

**.pytest_cache/**: Guarda información temporal generada por pytest.

**.gitignore**: Indica qué archivos o carpetas Git debe ignorar.

**requirements-dev.txt**: Lista las dependencias necesarias para desarrollo y pruebas.

**README.md**: Documenta y explica el proyecto.

**pyproject.toml**: Contiene la configuración del proyecto y de las herramientas de Python.

**Conclusión**
Hacer pruebas automáticas es como ponerle frenos seguros a una bicicleta antes de salir a rodar: nos permite atrapar los errores antes de que se conviertan en problemas grandes, asegurando que nuestro código funcione siempre a la primera y sin trampas.
