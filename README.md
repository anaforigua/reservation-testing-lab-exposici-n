# 🚀 Mi Laboratorio de Reservas (Reservation Testing Lab)

¡Hola! Este proyecto es como un **juego ordenado de fichas** que ayuda a una tiendita a organizar citas y reservas sin equivocarse ni chocar horarios.

---

## 🛠️ ¿Cómo se creó y ejecutó este proyecto?

Para armar este proyecto paso a paso en la computadora, usamos estos comandos:

1. **Crear y activar el entorno virtual (la caja secreta):**
   ```cmd
   python -m venv venv
   venv\Scripts\activate

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


8 **Estructura**
C:.
│   .gitignore
│   8.0.0
│   pyproject.toml
│   README.md
│   requirements-dev.txt
│
├───.pytest_cache
│   │   .gitignore
│   │   CACHEDIR.TAG
│   │   README.md
│   │
│   └───v
│       └───cache
│               nodeids
│
├───app
│   │   exceptions.py
│   │   repositories.py
│   │   reservation_service.py
│   │   validators.py
│   │   __init__.py
│   │
│   └───__pycache__
│           exceptions.cpython-314.pyc
│           repositories.cpython-314.pyc
│           reservation_service.cpython-314.pyc
│           validators.cpython-314.pyc
│           __init__.cpython-314.pyc
│
├───tests
│   │   conftest.py
│   │   test_reservation_service.py
│   │   test_validators.py
│   │
│   └───__pycache__
│           conftest.cpython-314-pytest-9.1.1.pyc
│           test_reservation_service.cpython-314-pytest-9.1.1.pyc
│           test_validators.cpython-314-pytest-9.1.1.pyc
│
└───venv
    │   .gitignore
    │   pyvenv.cfg
    │
    ├───Include
    ├───Lib
    │   └───site-packages
    │       │   py.py
    │       │
    │       ├───colorama
    │       │   │   ansi.py
    │       │   │   ansitowin32.py
    │       │   │   initialise.py
    │       │   │   win32.py
    │       │   │   winterm.py
    │       │   │   __init__.py
    │       │   │
    │       │   ├───tests
    │       │   │   │   ansitowin32_test.py
    │       │   │   │   ansi_test.py
    │       │   │   │   initialise_test.py
    │       │   │   │   isatty_test.py
    │       │   │   │   utils.py
    │       │   │   │   winterm_test.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           ansitowin32_test.cpython-314.pyc
    │       │   │           ansi_test.cpython-314.pyc
    │       │   │           initialise_test.cpython-314.pyc
    │       │   │           isatty_test.cpython-314.pyc
    │       │   │           utils.cpython-314.pyc
    │       │   │           winterm_test.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           ansi.cpython-314.pyc
    │       │           ansitowin32.cpython-314.pyc
    │       │           initialise.cpython-314.pyc
    │       │           win32.cpython-314.pyc
    │       │           winterm.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───colorama-0.4.6.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE.txt
    │       │
    │       ├───iniconfig
    │       │   │   exceptions.py
    │       │   │   py.typed
    │       │   │   _parse.py
    │       │   │   _version.py
    │       │   │   __init__.py
    │       │   │
    │       │   └───__pycache__
    │       │           exceptions.cpython-314.pyc
    │       │           _parse.cpython-314.pyc
    │       │           _version.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───iniconfig-2.3.0.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   top_level.txt
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───packaging
    │       │   │   dependency_groups.py
    │       │   │   direct_url.py
    │       │   │   errors.py
    │       │   │   markers.py
    │       │   │   metadata.py
    │       │   │   py.typed
    │       │   │   pylock.py
    │       │   │   ranges.py
    │       │   │   requirements.py
    │       │   │   specifiers.py
    │       │   │   tags.py
    │       │   │   utils.py
    │       │   │   version.py
    │       │   │   _elffile.py
    │       │   │   _manylinux.py
    │       │   │   _musllinux.py
    │       │   │   _parser.py
    │       │   │   _ranges.py
    │       │   │   _structures.py
    │       │   │   _tokenizer.py
    │       │   │   __init__.py
    │       │   │
    │       │   ├───licenses
    │       │   │   │   _spdx.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           _spdx.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           dependency_groups.cpython-314.pyc
    │       │           direct_url.cpython-314.pyc
    │       │           errors.cpython-314.pyc
    │       │           markers.cpython-314.pyc
    │       │           metadata.cpython-314.pyc
    │       │           pylock.cpython-314.pyc
    │       │           ranges.cpython-314.pyc
    │       │           requirements.cpython-314.pyc
    │       │           specifiers.cpython-314.pyc
    │       │           tags.cpython-314.pyc
    │       │           utils.cpython-314.pyc
    │       │           version.cpython-314.pyc
    │       │           _elffile.cpython-314.pyc
    │       │           _manylinux.cpython-314.pyc
    │       │           _musllinux.cpython-314.pyc
    │       │           _parser.cpython-314.pyc
    │       │           _ranges.cpython-314.pyc
    │       │           _structures.cpython-314.pyc
    │       │           _tokenizer.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───packaging-26.3.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │           LICENSE.APACHE
    │       │           LICENSE.BSD
    │       │
    │       ├───pip
    │       │   │   py.typed
    │       │   │   __init__.py
    │       │   │   __main__.py
    │       │   │   __pip-runner__.py
    │       │   │
    │       │   ├───_internal
    │       │   │   │   cache.py
    │       │   │   │   configuration.py
    │       │   │   │   exceptions.py
    │       │   │   │   main.py
    │       │   │   │   pyproject.py
    │       │   │   │   self_outdated_check.py
    │       │   │   │   wheel_builder.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   ├───build_env
    │       │   │   │   │   base.py
    │       │   │   │   │   installer.py
    │       │   │   │   │   noop.py
    │       │   │   │   │   venv.py
    │       │   │   │   │   virtual.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           base.cpython-314.pyc
    │       │   │   │           installer.cpython-314.pyc
    │       │   │   │           noop.cpython-314.pyc
    │       │   │   │           venv.cpython-314.pyc
    │       │   │   │           virtual.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───cli
    │       │   │   │   │   autocompletion.py
    │       │   │   │   │   base_command.py
    │       │   │   │   │   cmdoptions.py
    │       │   │   │   │   command_context.py
    │       │   │   │   │   index_command.py
    │       │   │   │   │   main.py
    │       │   │   │   │   main_parser.py
    │       │   │   │   │   parser.py
    │       │   │   │   │   progress_bars.py
    │       │   │   │   │   req_command.py
    │       │   │   │   │   spinners.py
    │       │   │   │   │   status_codes.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           autocompletion.cpython-314.pyc
    │       │   │   │           base_command.cpython-314.pyc
    │       │   │   │           cmdoptions.cpython-314.pyc
    │       │   │   │           command_context.cpython-314.pyc
    │       │   │   │           index_command.cpython-314.pyc
    │       │   │   │           main.cpython-314.pyc
    │       │   │   │           main_parser.cpython-314.pyc
    │       │   │   │           parser.cpython-314.pyc
    │       │   │   │           progress_bars.cpython-314.pyc
    │       │   │   │           req_command.cpython-314.pyc
    │       │   │   │           spinners.cpython-314.pyc
    │       │   │   │           status_codes.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───commands
    │       │   │   │   │   cache.py
    │       │   │   │   │   check.py
    │       │   │   │   │   completion.py
    │       │   │   │   │   configuration.py
    │       │   │   │   │   debug.py
    │       │   │   │   │   download.py
    │       │   │   │   │   freeze.py
    │       │   │   │   │   hash.py
    │       │   │   │   │   help.py
    │       │   │   │   │   index.py
    │       │   │   │   │   inspect.py
    │       │   │   │   │   install.py
    │       │   │   │   │   list.py
    │       │   │   │   │   lock.py
    │       │   │   │   │   search.py
    │       │   │   │   │   show.py
    │       │   │   │   │   uninstall.py
    │       │   │   │   │   wheel.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           cache.cpython-314.pyc
    │       │   │   │           check.cpython-314.pyc
    │       │   │   │           completion.cpython-314.pyc
    │       │   │   │           configuration.cpython-314.pyc
    │       │   │   │           debug.cpython-314.pyc
    │       │   │   │           download.cpython-314.pyc
    │       │   │   │           freeze.cpython-314.pyc
    │       │   │   │           hash.cpython-314.pyc
    │       │   │   │           help.cpython-314.pyc
    │       │   │   │           index.cpython-314.pyc
    │       │   │   │           inspect.cpython-314.pyc
    │       │   │   │           install.cpython-314.pyc
    │       │   │   │           list.cpython-314.pyc
    │       │   │   │           lock.cpython-314.pyc
    │       │   │   │           search.cpython-314.pyc
    │       │   │   │           show.cpython-314.pyc
    │       │   │   │           uninstall.cpython-314.pyc
    │       │   │   │           wheel.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───distributions
    │       │   │   │   │   base.py
    │       │   │   │   │   installed.py
    │       │   │   │   │   sdist.py
    │       │   │   │   │   wheel.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           base.cpython-314.pyc
    │       │   │   │           installed.cpython-314.pyc
    │       │   │   │           sdist.cpython-314.pyc
    │       │   │   │           wheel.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───index
    │       │   │   │   │   collector.py
    │       │   │   │   │   package_finder.py
    │       │   │   │   │   sources.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           collector.cpython-314.pyc
    │       │   │   │           package_finder.cpython-314.pyc
    │       │   │   │           sources.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───locations
    │       │   │   │   │   base.py
    │       │   │   │   │   _distutils.py
    │       │   │   │   │   _sysconfig.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           base.cpython-314.pyc
    │       │   │   │           _distutils.cpython-314.pyc
    │       │   │   │           _sysconfig.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───metadata
    │       │   │   │   │   base.py
    │       │   │   │   │   pkg_resources.py
    │       │   │   │   │   _json.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───importlib
    │       │   │   │   │   │   _compat.py
    │       │   │   │   │   │   _dists.py
    │       │   │   │   │   │   _envs.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _compat.cpython-314.pyc
    │       │   │   │   │           _dists.cpython-314.pyc
    │       │   │   │   │           _envs.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           base.cpython-314.pyc
    │       │   │   │           pkg_resources.cpython-314.pyc
    │       │   │   │           _json.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───models
    │       │   │   │   │   candidate.py
    │       │   │   │   │   direct_url.py
    │       │   │   │   │   format_control.py
    │       │   │   │   │   index.py
    │       │   │   │   │   installation_report.py
    │       │   │   │   │   link.py
    │       │   │   │   │   release_control.py
    │       │   │   │   │   scheme.py
    │       │   │   │   │   search_scope.py
    │       │   │   │   │   selection_prefs.py
    │       │   │   │   │   target_python.py
    │       │   │   │   │   wheel.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           candidate.cpython-314.pyc
    │       │   │   │           direct_url.cpython-314.pyc
    │       │   │   │           format_control.cpython-314.pyc
    │       │   │   │           index.cpython-314.pyc
    │       │   │   │           installation_report.cpython-314.pyc
    │       │   │   │           link.cpython-314.pyc
    │       │   │   │           release_control.cpython-314.pyc
    │       │   │   │           scheme.cpython-314.pyc
    │       │   │   │           search_scope.cpython-314.pyc
    │       │   │   │           selection_prefs.cpython-314.pyc
    │       │   │   │           target_python.cpython-314.pyc
    │       │   │   │           wheel.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───network
    │       │   │   │   │   auth.py
    │       │   │   │   │   cache.py
    │       │   │   │   │   download.py
    │       │   │   │   │   lazy_wheel.py
    │       │   │   │   │   session.py
    │       │   │   │   │   utils.py
    │       │   │   │   │   xmlrpc.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           auth.cpython-314.pyc
    │       │   │   │           cache.cpython-314.pyc
    │       │   │   │           download.cpython-314.pyc
    │       │   │   │           lazy_wheel.cpython-314.pyc
    │       │   │   │           session.cpython-314.pyc
    │       │   │   │           utils.cpython-314.pyc
    │       │   │   │           xmlrpc.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───operations
    │       │   │   │   │   check.py
    │       │   │   │   │   freeze.py
    │       │   │   │   │   prepare.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───build
    │       │   │   │   │   │   build_tracker.py
    │       │   │   │   │   │   metadata.py
    │       │   │   │   │   │   metadata_editable.py
    │       │   │   │   │   │   wheel.py
    │       │   │   │   │   │   wheel_editable.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           build_tracker.cpython-314.pyc
    │       │   │   │   │           metadata.cpython-314.pyc
    │       │   │   │   │           metadata_editable.cpython-314.pyc
    │       │   │   │   │           wheel.cpython-314.pyc
    │       │   │   │   │           wheel_editable.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───install
    │       │   │   │   │   │   wheel.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           wheel.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           check.cpython-314.pyc
    │       │   │   │           freeze.cpython-314.pyc
    │       │   │   │           prepare.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───req
    │       │   │   │   │   constructors.py
    │       │   │   │   │   pep723.py
    │       │   │   │   │   req_dependency_group.py
    │       │   │   │   │   req_file.py
    │       │   │   │   │   req_install.py
    │       │   │   │   │   req_set.py
    │       │   │   │   │   req_uninstall.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           constructors.cpython-314.pyc
    │       │   │   │           pep723.cpython-314.pyc
    │       │   │   │           req_dependency_group.cpython-314.pyc
    │       │   │   │           req_file.cpython-314.pyc
    │       │   │   │           req_install.cpython-314.pyc
    │       │   │   │           req_set.cpython-314.pyc
    │       │   │   │           req_uninstall.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───resolution
    │       │   │   │   │   base.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───legacy
    │       │   │   │   │   │   resolver.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           resolver.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───resolvelib
    │       │   │   │   │   │   base.py
    │       │   │   │   │   │   candidates.py
    │       │   │   │   │   │   factory.py
    │       │   │   │   │   │   found_candidates.py
    │       │   │   │   │   │   provider.py
    │       │   │   │   │   │   reporter.py
    │       │   │   │   │   │   requirements.py
    │       │   │   │   │   │   resolver.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           base.cpython-314.pyc
    │       │   │   │   │           candidates.cpython-314.pyc
    │       │   │   │   │           factory.cpython-314.pyc
    │       │   │   │   │           found_candidates.cpython-314.pyc
    │       │   │   │   │           provider.cpython-314.pyc
    │       │   │   │   │           reporter.cpython-314.pyc
    │       │   │   │   │           requirements.cpython-314.pyc
    │       │   │   │   │           resolver.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           base.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───utils
    │       │   │   │   │   appdirs.py
    │       │   │   │   │   compat.py
    │       │   │   │   │   compatibility_tags.py
    │       │   │   │   │   datetime.py
    │       │   │   │   │   deprecation.py
    │       │   │   │   │   direct_url_helpers.py
    │       │   │   │   │   egg_link.py
    │       │   │   │   │   entrypoints.py
    │       │   │   │   │   filesystem.py
    │       │   │   │   │   filetypes.py
    │       │   │   │   │   glibc.py
    │       │   │   │   │   hashes.py
    │       │   │   │   │   logging.py
    │       │   │   │   │   misc.py
    │       │   │   │   │   packaging.py
    │       │   │   │   │   pylock.py
    │       │   │   │   │   retry.py
    │       │   │   │   │   subprocess.py
    │       │   │   │   │   temp_dir.py
    │       │   │   │   │   unpacking.py
    │       │   │   │   │   urls.py
    │       │   │   │   │   virtualenv.py
    │       │   │   │   │   wheel.py
    │       │   │   │   │   _jaraco_text.py
    │       │   │   │   │   _log.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           appdirs.cpython-314.pyc
    │       │   │   │           compat.cpython-314.pyc
    │       │   │   │           compatibility_tags.cpython-314.pyc
    │       │   │   │           datetime.cpython-314.pyc
    │       │   │   │           deprecation.cpython-314.pyc
    │       │   │   │           direct_url_helpers.cpython-314.pyc
    │       │   │   │           egg_link.cpython-314.pyc
    │       │   │   │           entrypoints.cpython-314.pyc
    │       │   │   │           filesystem.cpython-314.pyc
    │       │   │   │           filetypes.cpython-314.pyc
    │       │   │   │           glibc.cpython-314.pyc
    │       │   │   │           hashes.cpython-314.pyc
    │       │   │   │           logging.cpython-314.pyc
    │       │   │   │           misc.cpython-314.pyc
    │       │   │   │           packaging.cpython-314.pyc
    │       │   │   │           pylock.cpython-314.pyc
    │       │   │   │           retry.cpython-314.pyc
    │       │   │   │           subprocess.cpython-314.pyc
    │       │   │   │           temp_dir.cpython-314.pyc
    │       │   │   │           unpacking.cpython-314.pyc
    │       │   │   │           urls.cpython-314.pyc
    │       │   │   │           virtualenv.cpython-314.pyc
    │       │   │   │           wheel.cpython-314.pyc
    │       │   │   │           _jaraco_text.cpython-314.pyc
    │       │   │   │           _log.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───vcs
    │       │   │   │   │   bazaar.py
    │       │   │   │   │   git.py
    │       │   │   │   │   mercurial.py
    │       │   │   │   │   subversion.py
    │       │   │   │   │   versioncontrol.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           bazaar.cpython-314.pyc
    │       │   │   │           git.cpython-314.pyc
    │       │   │   │           mercurial.cpython-314.pyc
    │       │   │   │           subversion.cpython-314.pyc
    │       │   │   │           versioncontrol.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           cache.cpython-314.pyc
    │       │   │           configuration.cpython-314.pyc
    │       │   │           exceptions.cpython-314.pyc
    │       │   │           main.cpython-314.pyc
    │       │   │           pyproject.cpython-314.pyc
    │       │   │           self_outdated_check.cpython-314.pyc
    │       │   │           wheel_builder.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_vendor
    │       │   │   │   bom.cdx.json
    │       │   │   │   README.rst
    │       │   │   │   vendor.txt
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   ├───cachecontrol
    │       │   │   │   │   adapter.py
    │       │   │   │   │   cache.py
    │       │   │   │   │   controller.py
    │       │   │   │   │   filewrapper.py
    │       │   │   │   │   heuristics.py
    │       │   │   │   │   LICENSE.txt
    │       │   │   │   │   py.typed
    │       │   │   │   │   serialize.py
    │       │   │   │   │   wrapper.py
    │       │   │   │   │   _cmd.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───caches
    │       │   │   │   │   │   file_cache.py
    │       │   │   │   │   │   redis_cache.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           file_cache.cpython-314.pyc
    │       │   │   │   │           redis_cache.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           adapter.cpython-314.pyc
    │       │   │   │           cache.cpython-314.pyc
    │       │   │   │           controller.cpython-314.pyc
    │       │   │   │           filewrapper.cpython-314.pyc
    │       │   │   │           heuristics.cpython-314.pyc
    │       │   │   │           serialize.cpython-314.pyc
    │       │   │   │           wrapper.cpython-314.pyc
    │       │   │   │           _cmd.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───certifi
    │       │   │   │   │   cacert.pem
    │       │   │   │   │   core.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           core.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───distlib
    │       │   │   │   │   compat.py
    │       │   │   │   │   LICENSE.txt
    │       │   │   │   │   resources.py
    │       │   │   │   │   scripts.py
    │       │   │   │   │   t32.exe
    │       │   │   │   │   t64-arm.exe
    │       │   │   │   │   t64.exe
    │       │   │   │   │   util.py
    │       │   │   │   │   w32.exe
    │       │   │   │   │   w64-arm.exe
    │       │   │   │   │   w64.exe
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           compat.cpython-314.pyc
    │       │   │   │           resources.cpython-314.pyc
    │       │   │   │           scripts.cpython-314.pyc
    │       │   │   │           util.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───distro
    │       │   │   │   │   distro.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           distro.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───idna
    │       │   │   │   │   cli.py
    │       │   │   │   │   codec.py
    │       │   │   │   │   compat.py
    │       │   │   │   │   core.py
    │       │   │   │   │   idnadata.py
    │       │   │   │   │   intranges.py
    │       │   │   │   │   LICENSE.md
    │       │   │   │   │   package_data.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   uts46data.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           cli.cpython-314.pyc
    │       │   │   │           codec.cpython-314.pyc
    │       │   │   │           compat.cpython-314.pyc
    │       │   │   │           core.cpython-314.pyc
    │       │   │   │           idnadata.cpython-314.pyc
    │       │   │   │           intranges.cpython-314.pyc
    │       │   │   │           package_data.cpython-314.pyc
    │       │   │   │           uts46data.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───msgpack
    │       │   │   │   │   COPYING
    │       │   │   │   │   exceptions.py
    │       │   │   │   │   ext.py
    │       │   │   │   │   fallback.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           exceptions.cpython-314.pyc
    │       │   │   │           ext.cpython-314.pyc
    │       │   │   │           fallback.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───packaging
    │       │   │   │   │   dependency_groups.py
    │       │   │   │   │   direct_url.py
    │       │   │   │   │   errors.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   LICENSE.APACHE
    │       │   │   │   │   LICENSE.BSD
    │       │   │   │   │   markers.py
    │       │   │   │   │   metadata.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   pylock.py
    │       │   │   │   │   requirements.py
    │       │   │   │   │   specifiers.py
    │       │   │   │   │   tags.py
    │       │   │   │   │   utils.py
    │       │   │   │   │   version.py
    │       │   │   │   │   _elffile.py
    │       │   │   │   │   _manylinux.py
    │       │   │   │   │   _musllinux.py
    │       │   │   │   │   _parser.py
    │       │   │   │   │   _structures.py
    │       │   │   │   │   _tokenizer.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───licenses
    │       │   │   │   │   │   _spdx.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _spdx.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           dependency_groups.cpython-314.pyc
    │       │   │   │           direct_url.cpython-314.pyc
    │       │   │   │           errors.cpython-314.pyc
    │       │   │   │           markers.cpython-314.pyc
    │       │   │   │           metadata.cpython-314.pyc
    │       │   │   │           pylock.cpython-314.pyc
    │       │   │   │           requirements.cpython-314.pyc
    │       │   │   │           specifiers.cpython-314.pyc
    │       │   │   │           tags.cpython-314.pyc
    │       │   │   │           utils.cpython-314.pyc
    │       │   │   │           version.cpython-314.pyc
    │       │   │   │           _elffile.cpython-314.pyc
    │       │   │   │           _manylinux.cpython-314.pyc
    │       │   │   │           _musllinux.cpython-314.pyc
    │       │   │   │           _parser.cpython-314.pyc
    │       │   │   │           _structures.cpython-314.pyc
    │       │   │   │           _tokenizer.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───pkg_resources
    │       │   │   │   │   LICENSE
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───platformdirs
    │       │   │   │   │   android.py
    │       │   │   │   │   api.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   macos.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   unix.py
    │       │   │   │   │   version.py
    │       │   │   │   │   windows.py
    │       │   │   │   │   _xdg.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           android.cpython-314.pyc
    │       │   │   │           api.cpython-314.pyc
    │       │   │   │           macos.cpython-314.pyc
    │       │   │   │           unix.cpython-314.pyc
    │       │   │   │           version.cpython-314.pyc
    │       │   │   │           windows.cpython-314.pyc
    │       │   │   │           _xdg.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───pygments
    │       │   │   │   │   console.py
    │       │   │   │   │   filter.py
    │       │   │   │   │   formatter.py
    │       │   │   │   │   lexer.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   modeline.py
    │       │   │   │   │   plugin.py
    │       │   │   │   │   regexopt.py
    │       │   │   │   │   scanner.py
    │       │   │   │   │   sphinxext.py
    │       │   │   │   │   style.py
    │       │   │   │   │   token.py
    │       │   │   │   │   unistring.py
    │       │   │   │   │   util.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   ├───filters
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───formatters
    │       │   │   │   │   │   _mapping.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _mapping.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───lexers
    │       │   │   │   │   │   python.py
    │       │   │   │   │   │   _mapping.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           python.cpython-314.pyc
    │       │   │   │   │           _mapping.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───styles
    │       │   │   │   │   │   _mapping.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _mapping.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           console.cpython-314.pyc
    │       │   │   │           filter.cpython-314.pyc
    │       │   │   │           formatter.cpython-314.pyc
    │       │   │   │           lexer.cpython-314.pyc
    │       │   │   │           modeline.cpython-314.pyc
    │       │   │   │           plugin.cpython-314.pyc
    │       │   │   │           regexopt.cpython-314.pyc
    │       │   │   │           scanner.cpython-314.pyc
    │       │   │   │           sphinxext.cpython-314.pyc
    │       │   │   │           style.cpython-314.pyc
    │       │   │   │           token.cpython-314.pyc
    │       │   │   │           unistring.cpython-314.pyc
    │       │   │   │           util.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───pyproject_hooks
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   _impl.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───_in_process
    │       │   │   │   │   │   _in_process.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           _in_process.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           _impl.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───requests
    │       │   │   │   │   adapters.py
    │       │   │   │   │   api.py
    │       │   │   │   │   auth.py
    │       │   │   │   │   certs.py
    │       │   │   │   │   compat.py
    │       │   │   │   │   cookies.py
    │       │   │   │   │   exceptions.py
    │       │   │   │   │   help.py
    │       │   │   │   │   hooks.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   models.py
    │       │   │   │   │   packages.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   sessions.py
    │       │   │   │   │   status_codes.py
    │       │   │   │   │   structures.py
    │       │   │   │   │   utils.py
    │       │   │   │   │   _internal_utils.py
    │       │   │   │   │   _types.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __version__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           adapters.cpython-314.pyc
    │       │   │   │           api.cpython-314.pyc
    │       │   │   │           auth.cpython-314.pyc
    │       │   │   │           certs.cpython-314.pyc
    │       │   │   │           compat.cpython-314.pyc
    │       │   │   │           cookies.cpython-314.pyc
    │       │   │   │           exceptions.cpython-314.pyc
    │       │   │   │           help.cpython-314.pyc
    │       │   │   │           hooks.cpython-314.pyc
    │       │   │   │           models.cpython-314.pyc
    │       │   │   │           packages.cpython-314.pyc
    │       │   │   │           sessions.cpython-314.pyc
    │       │   │   │           status_codes.cpython-314.pyc
    │       │   │   │           structures.cpython-314.pyc
    │       │   │   │           utils.cpython-314.pyc
    │       │   │   │           _internal_utils.cpython-314.pyc
    │       │   │   │           _types.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __version__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───resolvelib
    │       │   │   │   │   LICENSE
    │       │   │   │   │   providers.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   reporters.py
    │       │   │   │   │   structs.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───resolvers
    │       │   │   │   │   │   abstract.py
    │       │   │   │   │   │   criterion.py
    │       │   │   │   │   │   exceptions.py
    │       │   │   │   │   │   resolution.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           abstract.cpython-314.pyc
    │       │   │   │   │           criterion.cpython-314.pyc
    │       │   │   │   │           exceptions.cpython-314.pyc
    │       │   │   │   │           resolution.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           providers.cpython-314.pyc
    │       │   │   │           reporters.cpython-314.pyc
    │       │   │   │           structs.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───rich
    │       │   │   │   │   abc.py
    │       │   │   │   │   align.py
    │       │   │   │   │   ansi.py
    │       │   │   │   │   bar.py
    │       │   │   │   │   box.py
    │       │   │   │   │   cells.py
    │       │   │   │   │   color.py
    │       │   │   │   │   color_triplet.py
    │       │   │   │   │   columns.py
    │       │   │   │   │   console.py
    │       │   │   │   │   constrain.py
    │       │   │   │   │   containers.py
    │       │   │   │   │   control.py
    │       │   │   │   │   default_styles.py
    │       │   │   │   │   diagnose.py
    │       │   │   │   │   emoji.py
    │       │   │   │   │   errors.py
    │       │   │   │   │   filesize.py
    │       │   │   │   │   file_proxy.py
    │       │   │   │   │   highlighter.py
    │       │   │   │   │   json.py
    │       │   │   │   │   jupyter.py
    │       │   │   │   │   layout.py
    │       │   │   │   │   LICENSE
    │       │   │   │   │   live.py
    │       │   │   │   │   live_render.py
    │       │   │   │   │   logging.py
    │       │   │   │   │   markup.py
    │       │   │   │   │   measure.py
    │       │   │   │   │   padding.py
    │       │   │   │   │   pager.py
    │       │   │   │   │   palette.py
    │       │   │   │   │   panel.py
    │       │   │   │   │   pretty.py
    │       │   │   │   │   progress.py
    │       │   │   │   │   progress_bar.py
    │       │   │   │   │   prompt.py
    │       │   │   │   │   protocol.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   region.py
    │       │   │   │   │   repr.py
    │       │   │   │   │   rule.py
    │       │   │   │   │   scope.py
    │       │   │   │   │   screen.py
    │       │   │   │   │   segment.py
    │       │   │   │   │   spinner.py
    │       │   │   │   │   status.py
    │       │   │   │   │   style.py
    │       │   │   │   │   styled.py
    │       │   │   │   │   syntax.py
    │       │   │   │   │   table.py
    │       │   │   │   │   terminal_theme.py
    │       │   │   │   │   text.py
    │       │   │   │   │   theme.py
    │       │   │   │   │   themes.py
    │       │   │   │   │   traceback.py
    │       │   │   │   │   tree.py
    │       │   │   │   │   _cell_widths.py
    │       │   │   │   │   _emoji_codes.py
    │       │   │   │   │   _emoji_replace.py
    │       │   │   │   │   _export_format.py
    │       │   │   │   │   _extension.py
    │       │   │   │   │   _fileno.py
    │       │   │   │   │   _inspect.py
    │       │   │   │   │   _log_render.py
    │       │   │   │   │   _loop.py
    │       │   │   │   │   _null_file.py
    │       │   │   │   │   _palettes.py
    │       │   │   │   │   _pick.py
    │       │   │   │   │   _ratio.py
    │       │   │   │   │   _spinners.py
    │       │   │   │   │   _stack.py
    │       │   │   │   │   _timer.py
    │       │   │   │   │   _win32_console.py
    │       │   │   │   │   _windows.py
    │       │   │   │   │   _windows_renderer.py
    │       │   │   │   │   _wrap.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │   __main__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           abc.cpython-314.pyc
    │       │   │   │           align.cpython-314.pyc
    │       │   │   │           ansi.cpython-314.pyc
    │       │   │   │           bar.cpython-314.pyc
    │       │   │   │           box.cpython-314.pyc
    │       │   │   │           cells.cpython-314.pyc
    │       │   │   │           color.cpython-314.pyc
    │       │   │   │           color_triplet.cpython-314.pyc
    │       │   │   │           columns.cpython-314.pyc
    │       │   │   │           console.cpython-314.pyc
    │       │   │   │           constrain.cpython-314.pyc
    │       │   │   │           containers.cpython-314.pyc
    │       │   │   │           control.cpython-314.pyc
    │       │   │   │           default_styles.cpython-314.pyc
    │       │   │   │           diagnose.cpython-314.pyc
    │       │   │   │           emoji.cpython-314.pyc
    │       │   │   │           errors.cpython-314.pyc
    │       │   │   │           filesize.cpython-314.pyc
    │       │   │   │           file_proxy.cpython-314.pyc
    │       │   │   │           highlighter.cpython-314.pyc
    │       │   │   │           json.cpython-314.pyc
    │       │   │   │           jupyter.cpython-314.pyc
    │       │   │   │           layout.cpython-314.pyc
    │       │   │   │           live.cpython-314.pyc
    │       │   │   │           live_render.cpython-314.pyc
    │       │   │   │           logging.cpython-314.pyc
    │       │   │   │           markup.cpython-314.pyc
    │       │   │   │           measure.cpython-314.pyc
    │       │   │   │           padding.cpython-314.pyc
    │       │   │   │           pager.cpython-314.pyc
    │       │   │   │           palette.cpython-314.pyc
    │       │   │   │           panel.cpython-314.pyc
    │       │   │   │           pretty.cpython-314.pyc
    │       │   │   │           progress.cpython-314.pyc
    │       │   │   │           progress_bar.cpython-314.pyc
    │       │   │   │           prompt.cpython-314.pyc
    │       │   │   │           protocol.cpython-314.pyc
    │       │   │   │           region.cpython-314.pyc
    │       │   │   │           repr.cpython-314.pyc
    │       │   │   │           rule.cpython-314.pyc
    │       │   │   │           scope.cpython-314.pyc
    │       │   │   │           screen.cpython-314.pyc
    │       │   │   │           segment.cpython-314.pyc
    │       │   │   │           spinner.cpython-314.pyc
    │       │   │   │           status.cpython-314.pyc
    │       │   │   │           style.cpython-314.pyc
    │       │   │   │           styled.cpython-314.pyc
    │       │   │   │           syntax.cpython-314.pyc
    │       │   │   │           table.cpython-314.pyc
    │       │   │   │           terminal_theme.cpython-314.pyc
    │       │   │   │           text.cpython-314.pyc
    │       │   │   │           theme.cpython-314.pyc
    │       │   │   │           themes.cpython-314.pyc
    │       │   │   │           traceback.cpython-314.pyc
    │       │   │   │           tree.cpython-314.pyc
    │       │   │   │           _cell_widths.cpython-314.pyc
    │       │   │   │           _emoji_codes.cpython-314.pyc
    │       │   │   │           _emoji_replace.cpython-314.pyc
    │       │   │   │           _export_format.cpython-314.pyc
    │       │   │   │           _extension.cpython-314.pyc
    │       │   │   │           _fileno.cpython-314.pyc
    │       │   │   │           _inspect.cpython-314.pyc
    │       │   │   │           _log_render.cpython-314.pyc
    │       │   │   │           _loop.cpython-314.pyc
    │       │   │   │           _null_file.cpython-314.pyc
    │       │   │   │           _palettes.cpython-314.pyc
    │       │   │   │           _pick.cpython-314.pyc
    │       │   │   │           _ratio.cpython-314.pyc
    │       │   │   │           _spinners.cpython-314.pyc
    │       │   │   │           _stack.cpython-314.pyc
    │       │   │   │           _timer.cpython-314.pyc
    │       │   │   │           _win32_console.cpython-314.pyc
    │       │   │   │           _windows.cpython-314.pyc
    │       │   │   │           _windows_renderer.cpython-314.pyc
    │       │   │   │           _wrap.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │           __main__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───tomli
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   _parser.py
    │       │   │   │   │   _re.py
    │       │   │   │   │   _types.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           _parser.cpython-314.pyc
    │       │   │   │           _re.cpython-314.pyc
    │       │   │   │           _types.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───tomli_w
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   _writer.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           _writer.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───truststore
    │       │   │   │   │   LICENSE
    │       │   │   │   │   py.typed
    │       │   │   │   │   _api.py
    │       │   │   │   │   _macos.py
    │       │   │   │   │   _openssl.py
    │       │   │   │   │   _ssl_constants.py
    │       │   │   │   │   _windows.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           _api.cpython-314.pyc
    │       │   │   │           _macos.cpython-314.pyc
    │       │   │   │           _openssl.cpython-314.pyc
    │       │   │   │           _ssl_constants.cpython-314.pyc
    │       │   │   │           _windows.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   ├───urllib3
    │       │   │   │   │   connection.py
    │       │   │   │   │   connectionpool.py
    │       │   │   │   │   exceptions.py
    │       │   │   │   │   fields.py
    │       │   │   │   │   filepost.py
    │       │   │   │   │   LICENSE.txt
    │       │   │   │   │   poolmanager.py
    │       │   │   │   │   py.typed
    │       │   │   │   │   response.py
    │       │   │   │   │   _base_connection.py
    │       │   │   │   │   _collections.py
    │       │   │   │   │   _request_methods.py
    │       │   │   │   │   _version.py
    │       │   │   │   │   __init__.py
    │       │   │   │   │
    │       │   │   │   ├───contrib
    │       │   │   │   │   │   pyopenssl.py
    │       │   │   │   │   │   socks.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   ├───emscripten
    │       │   │   │   │   │   │   connection.py
    │       │   │   │   │   │   │   emscripten_fetch_worker.js
    │       │   │   │   │   │   │   fetch.py
    │       │   │   │   │   │   │   request.py
    │       │   │   │   │   │   │   response.py
    │       │   │   │   │   │   │   __init__.py
    │       │   │   │   │   │   │
    │       │   │   │   │   │   └───__pycache__
    │       │   │   │   │   │           connection.cpython-314.pyc
    │       │   │   │   │   │           fetch.cpython-314.pyc
    │       │   │   │   │   │           request.cpython-314.pyc
    │       │   │   │   │   │           response.cpython-314.pyc
    │       │   │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           pyopenssl.cpython-314.pyc
    │       │   │   │   │           socks.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───http2
    │       │   │   │   │   │   connection.py
    │       │   │   │   │   │   probe.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           connection.cpython-314.pyc
    │       │   │   │   │           probe.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   ├───util
    │       │   │   │   │   │   connection.py
    │       │   │   │   │   │   proxy.py
    │       │   │   │   │   │   request.py
    │       │   │   │   │   │   response.py
    │       │   │   │   │   │   retry.py
    │       │   │   │   │   │   ssltransport.py
    │       │   │   │   │   │   ssl_.py
    │       │   │   │   │   │   ssl_match_hostname.py
    │       │   │   │   │   │   timeout.py
    │       │   │   │   │   │   url.py
    │       │   │   │   │   │   util.py
    │       │   │   │   │   │   wait.py
    │       │   │   │   │   │   __init__.py
    │       │   │   │   │   │
    │       │   │   │   │   └───__pycache__
    │       │   │   │   │           connection.cpython-314.pyc
    │       │   │   │   │           proxy.cpython-314.pyc
    │       │   │   │   │           request.cpython-314.pyc
    │       │   │   │   │           response.cpython-314.pyc
    │       │   │   │   │           retry.cpython-314.pyc
    │       │   │   │   │           ssltransport.cpython-314.pyc
    │       │   │   │   │           ssl_.cpython-314.pyc
    │       │   │   │   │           ssl_match_hostname.cpython-314.pyc
    │       │   │   │   │           timeout.cpython-314.pyc
    │       │   │   │   │           url.cpython-314.pyc
    │       │   │   │   │           util.cpython-314.pyc
    │       │   │   │   │           wait.cpython-314.pyc
    │       │   │   │   │           __init__.cpython-314.pyc
    │       │   │   │   │
    │       │   │   │   └───__pycache__
    │       │   │   │           connection.cpython-314.pyc
    │       │   │   │           connectionpool.cpython-314.pyc
    │       │   │   │           exceptions.cpython-314.pyc
    │       │   │   │           fields.cpython-314.pyc
    │       │   │   │           filepost.cpython-314.pyc
    │       │   │   │           poolmanager.cpython-314.pyc
    │       │   │   │           response.cpython-314.pyc
    │       │   │   │           _base_connection.cpython-314.pyc
    │       │   │   │           _collections.cpython-314.pyc
    │       │   │   │           _request_methods.cpython-314.pyc
    │       │   │   │           _version.cpython-314.pyc
    │       │   │   │           __init__.cpython-314.pyc
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           __init__.cpython-314.pyc
    │       │           __main__.cpython-314.pyc
    │       │           __pip-runner__.cpython-314.pyc
    │       │
    │       ├───pip-26.2.1.dist-info
    │       │   │   entry_points.txt
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   REQUESTED
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │       │   AUTHORS.txt
    │       │       │   LICENSE.txt
    │       │       │
    │       │       └───src
    │       │           └───pip
    │       │               └───_vendor
    │       │                   ├───cachecontrol
    │       │                   │       LICENSE.txt
    │       │                   │
    │       │                   ├───certifi
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───distlib
    │       │                   │       LICENSE.txt
    │       │                   │
    │       │                   ├───distro
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───idna
    │       │                   │       LICENSE.md
    │       │                   │
    │       │                   ├───msgpack
    │       │                   │       COPYING
    │       │                   │
    │       │                   ├───packaging
    │       │                   │       LICENSE
    │       │                   │       LICENSE.APACHE
    │       │                   │       LICENSE.BSD
    │       │                   │
    │       │                   ├───pkg_resources
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───platformdirs
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───pygments
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───pyproject_hooks
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───requests
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───resolvelib
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───rich
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───tomli
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───tomli_w
    │       │                   │       LICENSE
    │       │                   │
    │       │                   ├───truststore
    │       │                   │       LICENSE
    │       │                   │
    │       │                   └───urllib3
    │       │                           LICENSE.txt
    │       │
    │       ├───pluggy
    │       │   │   py.typed
    │       │   │   _callers.py
    │       │   │   _hooks.py
    │       │   │   _manager.py
    │       │   │   _result.py
    │       │   │   _tracing.py
    │       │   │   _version.py
    │       │   │   _warnings.py
    │       │   │   __init__.py
    │       │   │
    │       │   └───__pycache__
    │       │           _callers.cpython-314.pyc
    │       │           _hooks.cpython-314.pyc
    │       │           _manager.cpython-314.pyc
    │       │           _result.cpython-314.pyc
    │       │           _tracing.cpython-314.pyc
    │       │           _version.cpython-314.pyc
    │       │           _warnings.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       ├───pluggy-1.6.0.dist-info
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   top_level.txt
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───pygments
    │       │   │   cmdline.py
    │       │   │   console.py
    │       │   │   filter.py
    │       │   │   formatter.py
    │       │   │   lexer.py
    │       │   │   modeline.py
    │       │   │   plugin.py
    │       │   │   regexopt.py
    │       │   │   scanner.py
    │       │   │   sphinxext.py
    │       │   │   style.py
    │       │   │   token.py
    │       │   │   unistring.py
    │       │   │   util.py
    │       │   │   __init__.py
    │       │   │   __main__.py
    │       │   │
    │       │   ├───filters
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───formatters
    │       │   │   │   bbcode.py
    │       │   │   │   groff.py
    │       │   │   │   html.py
    │       │   │   │   img.py
    │       │   │   │   irc.py
    │       │   │   │   latex.py
    │       │   │   │   other.py
    │       │   │   │   pangomarkup.py
    │       │   │   │   rtf.py
    │       │   │   │   svg.py
    │       │   │   │   terminal.py
    │       │   │   │   terminal256.py
    │       │   │   │   _mapping.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           bbcode.cpython-314.pyc
    │       │   │           groff.cpython-314.pyc
    │       │   │           html.cpython-314.pyc
    │       │   │           img.cpython-314.pyc
    │       │   │           irc.cpython-314.pyc
    │       │   │           latex.cpython-314.pyc
    │       │   │           other.cpython-314.pyc
    │       │   │           pangomarkup.cpython-314.pyc
    │       │   │           rtf.cpython-314.pyc
    │       │   │           svg.cpython-314.pyc
    │       │   │           terminal.cpython-314.pyc
    │       │   │           terminal256.cpython-314.pyc
    │       │   │           _mapping.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───lexers
    │       │   │   │   actionscript.py
    │       │   │   │   ada.py
    │       │   │   │   agile.py
    │       │   │   │   algebra.py
    │       │   │   │   ambient.py
    │       │   │   │   amdgpu.py
    │       │   │   │   ampl.py
    │       │   │   │   apdlexer.py
    │       │   │   │   apl.py
    │       │   │   │   archetype.py
    │       │   │   │   arrow.py
    │       │   │   │   arturo.py
    │       │   │   │   asc.py
    │       │   │   │   asm.py
    │       │   │   │   asn1.py
    │       │   │   │   automation.py
    │       │   │   │   bare.py
    │       │   │   │   basic.py
    │       │   │   │   bdd.py
    │       │   │   │   berry.py
    │       │   │   │   bibtex.py
    │       │   │   │   bitbake.py
    │       │   │   │   blueprint.py
    │       │   │   │   boa.py
    │       │   │   │   bqn.py
    │       │   │   │   business.py
    │       │   │   │   capnproto.py
    │       │   │   │   carbon.py
    │       │   │   │   cddl.py
    │       │   │   │   cel.py
    │       │   │   │   chapel.py
    │       │   │   │   clean.py
    │       │   │   │   codeql.py
    │       │   │   │   comal.py
    │       │   │   │   compiled.py
    │       │   │   │   configs.py
    │       │   │   │   console.py
    │       │   │   │   cplint.py
    │       │   │   │   crystal.py
    │       │   │   │   csound.py
    │       │   │   │   css.py
    │       │   │   │   c_cpp.py
    │       │   │   │   c_like.py
    │       │   │   │   d.py
    │       │   │   │   dalvik.py
    │       │   │   │   data.py
    │       │   │   │   dax.py
    │       │   │   │   devicetree.py
    │       │   │   │   diff.py
    │       │   │   │   dns.py
    │       │   │   │   dotnet.py
    │       │   │   │   dsls.py
    │       │   │   │   dylan.py
    │       │   │   │   ecl.py
    │       │   │   │   eiffel.py
    │       │   │   │   elm.py
    │       │   │   │   elpi.py
    │       │   │   │   email.py
    │       │   │   │   erlang.py
    │       │   │   │   esoteric.py
    │       │   │   │   ezhil.py
    │       │   │   │   factor.py
    │       │   │   │   fantom.py
    │       │   │   │   felix.py
    │       │   │   │   fift.py
    │       │   │   │   floscript.py
    │       │   │   │   forth.py
    │       │   │   │   fortran.py
    │       │   │   │   foxpro.py
    │       │   │   │   freefem.py
    │       │   │   │   func.py
    │       │   │   │   functional.py
    │       │   │   │   futhark.py
    │       │   │   │   gcodelexer.py
    │       │   │   │   gdscript.py
    │       │   │   │   gleam.py
    │       │   │   │   go.py
    │       │   │   │   grammar_notation.py
    │       │   │   │   graph.py
    │       │   │   │   graphics.py
    │       │   │   │   graphql.py
    │       │   │   │   graphviz.py
    │       │   │   │   gsql.py
    │       │   │   │   hare.py
    │       │   │   │   haskell.py
    │       │   │   │   haxe.py
    │       │   │   │   hdl.py
    │       │   │   │   hexdump.py
    │       │   │   │   html.py
    │       │   │   │   idl.py
    │       │   │   │   igor.py
    │       │   │   │   inferno.py
    │       │   │   │   installers.py
    │       │   │   │   int_fiction.py
    │       │   │   │   iolang.py
    │       │   │   │   j.py
    │       │   │   │   javascript.py
    │       │   │   │   jmespath.py
    │       │   │   │   jslt.py
    │       │   │   │   json5.py
    │       │   │   │   jsonnet.py
    │       │   │   │   jsx.py
    │       │   │   │   julia.py
    │       │   │   │   jvm.py
    │       │   │   │   kuin.py
    │       │   │   │   kusto.py
    │       │   │   │   ldap.py
    │       │   │   │   lean.py
    │       │   │   │   lilypond.py
    │       │   │   │   lisp.py
    │       │   │   │   macaulay2.py
    │       │   │   │   make.py
    │       │   │   │   maple.py
    │       │   │   │   markup.py
    │       │   │   │   math.py
    │       │   │   │   matlab.py
    │       │   │   │   maxima.py
    │       │   │   │   meson.py
    │       │   │   │   mime.py
    │       │   │   │   minecraft.py
    │       │   │   │   mips.py
    │       │   │   │   ml.py
    │       │   │   │   modeling.py
    │       │   │   │   modula2.py
    │       │   │   │   mojo.py
    │       │   │   │   monte.py
    │       │   │   │   mosel.py
    │       │   │   │   ncl.py
    │       │   │   │   nimrod.py
    │       │   │   │   nit.py
    │       │   │   │   nix.py
    │       │   │   │   numbair.py
    │       │   │   │   oberon.py
    │       │   │   │   objective.py
    │       │   │   │   ooc.py
    │       │   │   │   openscad.py
    │       │   │   │   other.py
    │       │   │   │   parasail.py
    │       │   │   │   parsers.py
    │       │   │   │   pascal.py
    │       │   │   │   pawn.py
    │       │   │   │   pddl.py
    │       │   │   │   perl.py
    │       │   │   │   phix.py
    │       │   │   │   php.py
    │       │   │   │   pointless.py
    │       │   │   │   pony.py
    │       │   │   │   praat.py
    │       │   │   │   procfile.py
    │       │   │   │   prolog.py
    │       │   │   │   promql.py
    │       │   │   │   prql.py
    │       │   │   │   ptx.py
    │       │   │   │   purescript.py
    │       │   │   │   python.py
    │       │   │   │   q.py
    │       │   │   │   qlik.py
    │       │   │   │   qvt.py
    │       │   │   │   r.py
    │       │   │   │   rdf.py
    │       │   │   │   rebol.py
    │       │   │   │   rego.py
    │       │   │   │   rell.py
    │       │   │   │   resource.py
    │       │   │   │   ride.py
    │       │   │   │   rita.py
    │       │   │   │   rnc.py
    │       │   │   │   roboconf.py
    │       │   │   │   robotframework.py
    │       │   │   │   ruby.py
    │       │   │   │   rust.py
    │       │   │   │   sas.py
    │       │   │   │   savi.py
    │       │   │   │   scdoc.py
    │       │   │   │   scripting.py
    │       │   │   │   sgf.py
    │       │   │   │   shell.py
    │       │   │   │   sieve.py
    │       │   │   │   slash.py
    │       │   │   │   smalltalk.py
    │       │   │   │   smithy.py
    │       │   │   │   smv.py
    │       │   │   │   snobol.py
    │       │   │   │   solidity.py
    │       │   │   │   soong.py
    │       │   │   │   sophia.py
    │       │   │   │   special.py
    │       │   │   │   spice.py
    │       │   │   │   sql.py
    │       │   │   │   srcinfo.py
    │       │   │   │   stata.py
    │       │   │   │   supercollider.py
    │       │   │   │   tablegen.py
    │       │   │   │   tact.py
    │       │   │   │   tal.py
    │       │   │   │   tcl.py
    │       │   │   │   teal.py
    │       │   │   │   templates.py
    │       │   │   │   teraterm.py
    │       │   │   │   testing.py
    │       │   │   │   text.py
    │       │   │   │   textedit.py
    │       │   │   │   textfmts.py
    │       │   │   │   theorem.py
    │       │   │   │   thingsdb.py
    │       │   │   │   tlb.py
    │       │   │   │   tls.py
    │       │   │   │   tnt.py
    │       │   │   │   trafficscript.py
    │       │   │   │   typoscript.py
    │       │   │   │   typst.py
    │       │   │   │   ul4.py
    │       │   │   │   unicon.py
    │       │   │   │   urbi.py
    │       │   │   │   usd.py
    │       │   │   │   varnish.py
    │       │   │   │   verification.py
    │       │   │   │   verifpal.py
    │       │   │   │   vip.py
    │       │   │   │   vyper.py
    │       │   │   │   web.py
    │       │   │   │   webassembly.py
    │       │   │   │   webidl.py
    │       │   │   │   webmisc.py
    │       │   │   │   wgsl.py
    │       │   │   │   whiley.py
    │       │   │   │   wowtoc.py
    │       │   │   │   wren.py
    │       │   │   │   x10.py
    │       │   │   │   xorg.py
    │       │   │   │   yang.py
    │       │   │   │   yara.py
    │       │   │   │   zig.py
    │       │   │   │   _ada_builtins.py
    │       │   │   │   _asy_builtins.py
    │       │   │   │   _cl_builtins.py
    │       │   │   │   _cocoa_builtins.py
    │       │   │   │   _csound_builtins.py
    │       │   │   │   _css_builtins.py
    │       │   │   │   _googlesql_builtins.py
    │       │   │   │   _julia_builtins.py
    │       │   │   │   _lasso_builtins.py
    │       │   │   │   _lilypond_builtins.py
    │       │   │   │   _luau_builtins.py
    │       │   │   │   _lua_builtins.py
    │       │   │   │   _mapping.py
    │       │   │   │   _mql_builtins.py
    │       │   │   │   _mysql_builtins.py
    │       │   │   │   _openedge_builtins.py
    │       │   │   │   _php_builtins.py
    │       │   │   │   _postgres_builtins.py
    │       │   │   │   _qlik_builtins.py
    │       │   │   │   _scheme_builtins.py
    │       │   │   │   _scilab_builtins.py
    │       │   │   │   _sourcemod_builtins.py
    │       │   │   │   _sql_builtins.py
    │       │   │   │   _stan_builtins.py
    │       │   │   │   _stata_builtins.py
    │       │   │   │   _tsql_builtins.py
    │       │   │   │   _usd_builtins.py
    │       │   │   │   _vbscript_builtins.py
    │       │   │   │   _vim_builtins.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           actionscript.cpython-314.pyc
    │       │   │           ada.cpython-314.pyc
    │       │   │           agile.cpython-314.pyc
    │       │   │           algebra.cpython-314.pyc
    │       │   │           ambient.cpython-314.pyc
    │       │   │           amdgpu.cpython-314.pyc
    │       │   │           ampl.cpython-314.pyc
    │       │   │           apdlexer.cpython-314.pyc
    │       │   │           apl.cpython-314.pyc
    │       │   │           archetype.cpython-314.pyc
    │       │   │           arrow.cpython-314.pyc
    │       │   │           arturo.cpython-314.pyc
    │       │   │           asc.cpython-314.pyc
    │       │   │           asm.cpython-314.pyc
    │       │   │           asn1.cpython-314.pyc
    │       │   │           automation.cpython-314.pyc
    │       │   │           bare.cpython-314.pyc
    │       │   │           basic.cpython-314.pyc
    │       │   │           bdd.cpython-314.pyc
    │       │   │           berry.cpython-314.pyc
    │       │   │           bibtex.cpython-314.pyc
    │       │   │           bitbake.cpython-314.pyc
    │       │   │           blueprint.cpython-314.pyc
    │       │   │           boa.cpython-314.pyc
    │       │   │           bqn.cpython-314.pyc
    │       │   │           business.cpython-314.pyc
    │       │   │           capnproto.cpython-314.pyc
    │       │   │           carbon.cpython-314.pyc
    │       │   │           cddl.cpython-314.pyc
    │       │   │           cel.cpython-314.pyc
    │       │   │           chapel.cpython-314.pyc
    │       │   │           clean.cpython-314.pyc
    │       │   │           codeql.cpython-314.pyc
    │       │   │           comal.cpython-314.pyc
    │       │   │           compiled.cpython-314.pyc
    │       │   │           configs.cpython-314.pyc
    │       │   │           console.cpython-314.pyc
    │       │   │           cplint.cpython-314.pyc
    │       │   │           crystal.cpython-314.pyc
    │       │   │           csound.cpython-314.pyc
    │       │   │           css.cpython-314.pyc
    │       │   │           c_cpp.cpython-314.pyc
    │       │   │           c_like.cpython-314.pyc
    │       │   │           d.cpython-314.pyc
    │       │   │           dalvik.cpython-314.pyc
    │       │   │           data.cpython-314.pyc
    │       │   │           dax.cpython-314.pyc
    │       │   │           devicetree.cpython-314.pyc
    │       │   │           diff.cpython-314.pyc
    │       │   │           dns.cpython-314.pyc
    │       │   │           dotnet.cpython-314.pyc
    │       │   │           dsls.cpython-314.pyc
    │       │   │           dylan.cpython-314.pyc
    │       │   │           ecl.cpython-314.pyc
    │       │   │           eiffel.cpython-314.pyc
    │       │   │           elm.cpython-314.pyc
    │       │   │           elpi.cpython-314.pyc
    │       │   │           email.cpython-314.pyc
    │       │   │           erlang.cpython-314.pyc
    │       │   │           esoteric.cpython-314.pyc
    │       │   │           ezhil.cpython-314.pyc
    │       │   │           factor.cpython-314.pyc
    │       │   │           fantom.cpython-314.pyc
    │       │   │           felix.cpython-314.pyc
    │       │   │           fift.cpython-314.pyc
    │       │   │           floscript.cpython-314.pyc
    │       │   │           forth.cpython-314.pyc
    │       │   │           fortran.cpython-314.pyc
    │       │   │           foxpro.cpython-314.pyc
    │       │   │           freefem.cpython-314.pyc
    │       │   │           func.cpython-314.pyc
    │       │   │           functional.cpython-314.pyc
    │       │   │           futhark.cpython-314.pyc
    │       │   │           gcodelexer.cpython-314.pyc
    │       │   │           gdscript.cpython-314.pyc
    │       │   │           gleam.cpython-314.pyc
    │       │   │           go.cpython-314.pyc
    │       │   │           grammar_notation.cpython-314.pyc
    │       │   │           graph.cpython-314.pyc
    │       │   │           graphics.cpython-314.pyc
    │       │   │           graphql.cpython-314.pyc
    │       │   │           graphviz.cpython-314.pyc
    │       │   │           gsql.cpython-314.pyc
    │       │   │           hare.cpython-314.pyc
    │       │   │           haskell.cpython-314.pyc
    │       │   │           haxe.cpython-314.pyc
    │       │   │           hdl.cpython-314.pyc
    │       │   │           hexdump.cpython-314.pyc
    │       │   │           html.cpython-314.pyc
    │       │   │           idl.cpython-314.pyc
    │       │   │           igor.cpython-314.pyc
    │       │   │           inferno.cpython-314.pyc
    │       │   │           installers.cpython-314.pyc
    │       │   │           int_fiction.cpython-314.pyc
    │       │   │           iolang.cpython-314.pyc
    │       │   │           j.cpython-314.pyc
    │       │   │           javascript.cpython-314.pyc
    │       │   │           jmespath.cpython-314.pyc
    │       │   │           jslt.cpython-314.pyc
    │       │   │           json5.cpython-314.pyc
    │       │   │           jsonnet.cpython-314.pyc
    │       │   │           jsx.cpython-314.pyc
    │       │   │           julia.cpython-314.pyc
    │       │   │           jvm.cpython-314.pyc
    │       │   │           kuin.cpython-314.pyc
    │       │   │           kusto.cpython-314.pyc
    │       │   │           ldap.cpython-314.pyc
    │       │   │           lean.cpython-314.pyc
    │       │   │           lilypond.cpython-314.pyc
    │       │   │           lisp.cpython-314.pyc
    │       │   │           macaulay2.cpython-314.pyc
    │       │   │           make.cpython-314.pyc
    │       │   │           maple.cpython-314.pyc
    │       │   │           markup.cpython-314.pyc
    │       │   │           math.cpython-314.pyc
    │       │   │           matlab.cpython-314.pyc
    │       │   │           maxima.cpython-314.pyc
    │       │   │           meson.cpython-314.pyc
    │       │   │           mime.cpython-314.pyc
    │       │   │           minecraft.cpython-314.pyc
    │       │   │           mips.cpython-314.pyc
    │       │   │           ml.cpython-314.pyc
    │       │   │           modeling.cpython-314.pyc
    │       │   │           modula2.cpython-314.pyc
    │       │   │           mojo.cpython-314.pyc
    │       │   │           monte.cpython-314.pyc
    │       │   │           mosel.cpython-314.pyc
    │       │   │           ncl.cpython-314.pyc
    │       │   │           nimrod.cpython-314.pyc
    │       │   │           nit.cpython-314.pyc
    │       │   │           nix.cpython-314.pyc
    │       │   │           numbair.cpython-314.pyc
    │       │   │           oberon.cpython-314.pyc
    │       │   │           objective.cpython-314.pyc
    │       │   │           ooc.cpython-314.pyc
    │       │   │           openscad.cpython-314.pyc
    │       │   │           other.cpython-314.pyc
    │       │   │           parasail.cpython-314.pyc
    │       │   │           parsers.cpython-314.pyc
    │       │   │           pascal.cpython-314.pyc
    │       │   │           pawn.cpython-314.pyc
    │       │   │           pddl.cpython-314.pyc
    │       │   │           perl.cpython-314.pyc
    │       │   │           phix.cpython-314.pyc
    │       │   │           php.cpython-314.pyc
    │       │   │           pointless.cpython-314.pyc
    │       │   │           pony.cpython-314.pyc
    │       │   │           praat.cpython-314.pyc
    │       │   │           procfile.cpython-314.pyc
    │       │   │           prolog.cpython-314.pyc
    │       │   │           promql.cpython-314.pyc
    │       │   │           prql.cpython-314.pyc
    │       │   │           ptx.cpython-314.pyc
    │       │   │           purescript.cpython-314.pyc
    │       │   │           python.cpython-314.pyc
    │       │   │           q.cpython-314.pyc
    │       │   │           qlik.cpython-314.pyc
    │       │   │           qvt.cpython-314.pyc
    │       │   │           r.cpython-314.pyc
    │       │   │           rdf.cpython-314.pyc
    │       │   │           rebol.cpython-314.pyc
    │       │   │           rego.cpython-314.pyc
    │       │   │           rell.cpython-314.pyc
    │       │   │           resource.cpython-314.pyc
    │       │   │           ride.cpython-314.pyc
    │       │   │           rita.cpython-314.pyc
    │       │   │           rnc.cpython-314.pyc
    │       │   │           roboconf.cpython-314.pyc
    │       │   │           robotframework.cpython-314.pyc
    │       │   │           ruby.cpython-314.pyc
    │       │   │           rust.cpython-314.pyc
    │       │   │           sas.cpython-314.pyc
    │       │   │           savi.cpython-314.pyc
    │       │   │           scdoc.cpython-314.pyc
    │       │   │           scripting.cpython-314.pyc
    │       │   │           sgf.cpython-314.pyc
    │       │   │           shell.cpython-314.pyc
    │       │   │           sieve.cpython-314.pyc
    │       │   │           slash.cpython-314.pyc
    │       │   │           smalltalk.cpython-314.pyc
    │       │   │           smithy.cpython-314.pyc
    │       │   │           smv.cpython-314.pyc
    │       │   │           snobol.cpython-314.pyc
    │       │   │           solidity.cpython-314.pyc
    │       │   │           soong.cpython-314.pyc
    │       │   │           sophia.cpython-314.pyc
    │       │   │           special.cpython-314.pyc
    │       │   │           spice.cpython-314.pyc
    │       │   │           sql.cpython-314.pyc
    │       │   │           srcinfo.cpython-314.pyc
    │       │   │           stata.cpython-314.pyc
    │       │   │           supercollider.cpython-314.pyc
    │       │   │           tablegen.cpython-314.pyc
    │       │   │           tact.cpython-314.pyc
    │       │   │           tal.cpython-314.pyc
    │       │   │           tcl.cpython-314.pyc
    │       │   │           teal.cpython-314.pyc
    │       │   │           templates.cpython-314.pyc
    │       │   │           teraterm.cpython-314.pyc
    │       │   │           testing.cpython-314.pyc
    │       │   │           text.cpython-314.pyc
    │       │   │           textedit.cpython-314.pyc
    │       │   │           textfmts.cpython-314.pyc
    │       │   │           theorem.cpython-314.pyc
    │       │   │           thingsdb.cpython-314.pyc
    │       │   │           tlb.cpython-314.pyc
    │       │   │           tls.cpython-314.pyc
    │       │   │           tnt.cpython-314.pyc
    │       │   │           trafficscript.cpython-314.pyc
    │       │   │           typoscript.cpython-314.pyc
    │       │   │           typst.cpython-314.pyc
    │       │   │           ul4.cpython-314.pyc
    │       │   │           unicon.cpython-314.pyc
    │       │   │           urbi.cpython-314.pyc
    │       │   │           usd.cpython-314.pyc
    │       │   │           varnish.cpython-314.pyc
    │       │   │           verification.cpython-314.pyc
    │       │   │           verifpal.cpython-314.pyc
    │       │   │           vip.cpython-314.pyc
    │       │   │           vyper.cpython-314.pyc
    │       │   │           web.cpython-314.pyc
    │       │   │           webassembly.cpython-314.pyc
    │       │   │           webidl.cpython-314.pyc
    │       │   │           webmisc.cpython-314.pyc
    │       │   │           wgsl.cpython-314.pyc
    │       │   │           whiley.cpython-314.pyc
    │       │   │           wowtoc.cpython-314.pyc
    │       │   │           wren.cpython-314.pyc
    │       │   │           x10.cpython-314.pyc
    │       │   │           xorg.cpython-314.pyc
    │       │   │           yang.cpython-314.pyc
    │       │   │           yara.cpython-314.pyc
    │       │   │           zig.cpython-314.pyc
    │       │   │           _ada_builtins.cpython-314.pyc
    │       │   │           _asy_builtins.cpython-314.pyc
    │       │   │           _cl_builtins.cpython-314.pyc
    │       │   │           _cocoa_builtins.cpython-314.pyc
    │       │   │           _csound_builtins.cpython-314.pyc
    │       │   │           _css_builtins.cpython-314.pyc
    │       │   │           _googlesql_builtins.cpython-314.pyc
    │       │   │           _julia_builtins.cpython-314.pyc
    │       │   │           _lasso_builtins.cpython-314.pyc
    │       │   │           _lilypond_builtins.cpython-314.pyc
    │       │   │           _luau_builtins.cpython-314.pyc
    │       │   │           _lua_builtins.cpython-314.pyc
    │       │   │           _mapping.cpython-314.pyc
    │       │   │           _mql_builtins.cpython-314.pyc
    │       │   │           _mysql_builtins.cpython-314.pyc
    │       │   │           _openedge_builtins.cpython-314.pyc
    │       │   │           _php_builtins.cpython-314.pyc
    │       │   │           _postgres_builtins.cpython-314.pyc
    │       │   │           _qlik_builtins.cpython-314.pyc
    │       │   │           _scheme_builtins.cpython-314.pyc
    │       │   │           _scilab_builtins.cpython-314.pyc
    │       │   │           _sourcemod_builtins.cpython-314.pyc
    │       │   │           _sql_builtins.cpython-314.pyc
    │       │   │           _stan_builtins.cpython-314.pyc
    │       │   │           _stata_builtins.cpython-314.pyc
    │       │   │           _tsql_builtins.cpython-314.pyc
    │       │   │           _usd_builtins.cpython-314.pyc
    │       │   │           _vbscript_builtins.cpython-314.pyc
    │       │   │           _vim_builtins.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───styles
    │       │   │   │   abap.py
    │       │   │   │   algol.py
    │       │   │   │   algol_nu.py
    │       │   │   │   arduino.py
    │       │   │   │   autumn.py
    │       │   │   │   borland.py
    │       │   │   │   bw.py
    │       │   │   │   coffee.py
    │       │   │   │   colorful.py
    │       │   │   │   default.py
    │       │   │   │   dracula.py
    │       │   │   │   emacs.py
    │       │   │   │   friendly.py
    │       │   │   │   friendly_grayscale.py
    │       │   │   │   fruity.py
    │       │   │   │   gh_dark.py
    │       │   │   │   gruvbox.py
    │       │   │   │   igor.py
    │       │   │   │   inkpot.py
    │       │   │   │   lightbulb.py
    │       │   │   │   lilypond.py
    │       │   │   │   lovelace.py
    │       │   │   │   manni.py
    │       │   │   │   material.py
    │       │   │   │   monokai.py
    │       │   │   │   murphy.py
    │       │   │   │   native.py
    │       │   │   │   night_owl.py
    │       │   │   │   nord.py
    │       │   │   │   onedark.py
    │       │   │   │   paraiso_dark.py
    │       │   │   │   paraiso_light.py
    │       │   │   │   pastie.py
    │       │   │   │   perldoc.py
    │       │   │   │   rainbow_dash.py
    │       │   │   │   rrt.py
    │       │   │   │   sas.py
    │       │   │   │   solarized.py
    │       │   │   │   staroffice.py
    │       │   │   │   stata_dark.py
    │       │   │   │   stata_light.py
    │       │   │   │   tango.py
    │       │   │   │   trac.py
    │       │   │   │   vim.py
    │       │   │   │   vs.py
    │       │   │   │   xcode.py
    │       │   │   │   zenburn.py
    │       │   │   │   _mapping.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           abap.cpython-314.pyc
    │       │   │           algol.cpython-314.pyc
    │       │   │           algol_nu.cpython-314.pyc
    │       │   │           arduino.cpython-314.pyc
    │       │   │           autumn.cpython-314.pyc
    │       │   │           borland.cpython-314.pyc
    │       │   │           bw.cpython-314.pyc
    │       │   │           coffee.cpython-314.pyc
    │       │   │           colorful.cpython-314.pyc
    │       │   │           default.cpython-314.pyc
    │       │   │           dracula.cpython-314.pyc
    │       │   │           emacs.cpython-314.pyc
    │       │   │           friendly.cpython-314.pyc
    │       │   │           friendly_grayscale.cpython-314.pyc
    │       │   │           fruity.cpython-314.pyc
    │       │   │           gh_dark.cpython-314.pyc
    │       │   │           gruvbox.cpython-314.pyc
    │       │   │           igor.cpython-314.pyc
    │       │   │           inkpot.cpython-314.pyc
    │       │   │           lightbulb.cpython-314.pyc
    │       │   │           lilypond.cpython-314.pyc
    │       │   │           lovelace.cpython-314.pyc
    │       │   │           manni.cpython-314.pyc
    │       │   │           material.cpython-314.pyc
    │       │   │           monokai.cpython-314.pyc
    │       │   │           murphy.cpython-314.pyc
    │       │   │           native.cpython-314.pyc
    │       │   │           night_owl.cpython-314.pyc
    │       │   │           nord.cpython-314.pyc
    │       │   │           onedark.cpython-314.pyc
    │       │   │           paraiso_dark.cpython-314.pyc
    │       │   │           paraiso_light.cpython-314.pyc
    │       │   │           pastie.cpython-314.pyc
    │       │   │           perldoc.cpython-314.pyc
    │       │   │           rainbow_dash.cpython-314.pyc
    │       │   │           rrt.cpython-314.pyc
    │       │   │           sas.cpython-314.pyc
    │       │   │           solarized.cpython-314.pyc
    │       │   │           staroffice.cpython-314.pyc
    │       │   │           stata_dark.cpython-314.pyc
    │       │   │           stata_light.cpython-314.pyc
    │       │   │           tango.cpython-314.pyc
    │       │   │           trac.cpython-314.pyc
    │       │   │           vim.cpython-314.pyc
    │       │   │           vs.cpython-314.pyc
    │       │   │           xcode.cpython-314.pyc
    │       │   │           zenburn.cpython-314.pyc
    │       │   │           _mapping.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           cmdline.cpython-314.pyc
    │       │           console.cpython-314.pyc
    │       │           filter.cpython-314.pyc
    │       │           formatter.cpython-314.pyc
    │       │           lexer.cpython-314.pyc
    │       │           modeline.cpython-314.pyc
    │       │           plugin.cpython-314.pyc
    │       │           regexopt.cpython-314.pyc
    │       │           scanner.cpython-314.pyc
    │       │           sphinxext.cpython-314.pyc
    │       │           style.cpython-314.pyc
    │       │           token.cpython-314.pyc
    │       │           unistring.cpython-314.pyc
    │       │           util.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │           __main__.cpython-314.pyc
    │       │
    │       ├───pygments-2.21.0.dist-info
    │       │   │   entry_points.txt
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           AUTHORS
    │       │           LICENSE
    │       │
    │       ├───pytest
    │       │   │   py.typed
    │       │   │   __init__.py
    │       │   │   __main__.py
    │       │   │
    │       │   └───__pycache__
    │       │           __init__.cpython-314.pyc
    │       │           __main__.cpython-314.pyc
    │       │
    │       ├───pytest-9.1.1.dist-info
    │       │   │   entry_points.txt
    │       │   │   INSTALLER
    │       │   │   METADATA
    │       │   │   RECORD
    │       │   │   REQUESTED
    │       │   │   top_level.txt
    │       │   │   WHEEL
    │       │   │
    │       │   └───licenses
    │       │           LICENSE
    │       │
    │       ├───_pytest
    │       │   │   cacheprovider.py
    │       │   │   capture.py
    │       │   │   compat.py
    │       │   │   debugging.py
    │       │   │   deprecated.py
    │       │   │   doctest.py
    │       │   │   faulthandler.py
    │       │   │   fixtures.py
    │       │   │   freeze_support.py
    │       │   │   helpconfig.py
    │       │   │   hookspec.py
    │       │   │   junitxml.py
    │       │   │   legacypath.py
    │       │   │   logging.py
    │       │   │   main.py
    │       │   │   monkeypatch.py
    │       │   │   nodes.py
    │       │   │   outcomes.py
    │       │   │   pastebin.py
    │       │   │   pathlib.py
    │       │   │   py.typed
    │       │   │   pytester.py
    │       │   │   pytester_assertions.py
    │       │   │   python.py
    │       │   │   python_api.py
    │       │   │   raises.py
    │       │   │   recwarn.py
    │       │   │   reports.py
    │       │   │   runner.py
    │       │   │   scope.py
    │       │   │   setuponly.py
    │       │   │   setupplan.py
    │       │   │   skipping.py
    │       │   │   stash.py
    │       │   │   stepwise.py
    │       │   │   subtests.py
    │       │   │   terminal.py
    │       │   │   terminalprogress.py
    │       │   │   threadexception.py
    │       │   │   timing.py
    │       │   │   tmpdir.py
    │       │   │   tracemalloc.py
    │       │   │   unittest.py
    │       │   │   unraisableexception.py
    │       │   │   warnings.py
    │       │   │   warning_types.py
    │       │   │   _argcomplete.py
    │       │   │   _version.py
    │       │   │   __init__.py
    │       │   │
    │       │   ├───assertion
    │       │   │   │   compare_text.py
    │       │   │   │   highlight.py
    │       │   │   │   rewrite.py
    │       │   │   │   truncate.py
    │       │   │   │   util.py
    │       │   │   │   _compare_any.py
    │       │   │   │   _compare_mapping.py
    │       │   │   │   _compare_sequence.py
    │       │   │   │   _compare_set.py
    │       │   │   │   _guards.py
    │       │   │   │   _typing.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           compare_text.cpython-314.pyc
    │       │   │           highlight.cpython-314.pyc
    │       │   │           rewrite.cpython-314.pyc
    │       │   │           truncate.cpython-314.pyc
    │       │   │           util.cpython-314.pyc
    │       │   │           _compare_any.cpython-314.pyc
    │       │   │           _compare_mapping.cpython-314.pyc
    │       │   │           _compare_sequence.cpython-314.pyc
    │       │   │           _compare_set.cpython-314.pyc
    │       │   │           _guards.cpython-314.pyc
    │       │   │           _typing.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───config
    │       │   │   │   argparsing.py
    │       │   │   │   exceptions.py
    │       │   │   │   findpaths.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           argparsing.cpython-314.pyc
    │       │   │           exceptions.cpython-314.pyc
    │       │   │           findpaths.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───mark
    │       │   │   │   expression.py
    │       │   │   │   structures.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           expression.cpython-314.pyc
    │       │   │           structures.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_code
    │       │   │   │   code.py
    │       │   │   │   source.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           code.cpython-314.pyc
    │       │   │           source.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_io
    │       │   │   │   pprint.py
    │       │   │   │   saferepr.py
    │       │   │   │   terminalwriter.py
    │       │   │   │   wcwidth.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           pprint.cpython-314.pyc
    │       │   │           saferepr.cpython-314.pyc
    │       │   │           terminalwriter.cpython-314.pyc
    │       │   │           wcwidth.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   ├───_py
    │       │   │   │   error.py
    │       │   │   │   path.py
    │       │   │   │   __init__.py
    │       │   │   │
    │       │   │   └───__pycache__
    │       │   │           error.cpython-314.pyc
    │       │   │           path.cpython-314.pyc
    │       │   │           __init__.cpython-314.pyc
    │       │   │
    │       │   └───__pycache__
    │       │           cacheprovider.cpython-314.pyc
    │       │           capture.cpython-314.pyc
    │       │           compat.cpython-314.pyc
    │       │           debugging.cpython-314.pyc
    │       │           deprecated.cpython-314.pyc
    │       │           doctest.cpython-314.pyc
    │       │           faulthandler.cpython-314.pyc
    │       │           fixtures.cpython-314.pyc
    │       │           freeze_support.cpython-314.pyc
    │       │           helpconfig.cpython-314.pyc
    │       │           hookspec.cpython-314.pyc
    │       │           junitxml.cpython-314.pyc
    │       │           legacypath.cpython-314.pyc
    │       │           logging.cpython-314.pyc
    │       │           main.cpython-314.pyc
    │       │           monkeypatch.cpython-314.pyc
    │       │           nodes.cpython-314.pyc
    │       │           outcomes.cpython-314.pyc
    │       │           pastebin.cpython-314.pyc
    │       │           pathlib.cpython-314.pyc
    │       │           pytester.cpython-314.pyc
    │       │           pytester_assertions.cpython-314.pyc
    │       │           python.cpython-314.pyc
    │       │           python_api.cpython-314.pyc
    │       │           raises.cpython-314.pyc
    │       │           recwarn.cpython-314.pyc
    │       │           reports.cpython-314.pyc
    │       │           runner.cpython-314.pyc
    │       │           scope.cpython-314.pyc
    │       │           setuponly.cpython-314.pyc
    │       │           setupplan.cpython-314.pyc
    │       │           skipping.cpython-314.pyc
    │       │           stash.cpython-314.pyc
    │       │           stepwise.cpython-314.pyc
    │       │           subtests.cpython-314.pyc
    │       │           terminal.cpython-314.pyc
    │       │           terminalprogress.cpython-314-pytest-9.1.1.pyc
    │       │           terminalprogress.cpython-314.pyc
    │       │           threadexception.cpython-314.pyc
    │       │           timing.cpython-314.pyc
    │       │           tmpdir.cpython-314.pyc
    │       │           tracemalloc.cpython-314.pyc
    │       │           unittest.cpython-314.pyc
    │       │           unraisableexception.cpython-314.pyc
    │       │           warnings.cpython-314.pyc
    │       │           warning_types.cpython-314.pyc
    │       │           _argcomplete.cpython-314.pyc
    │       │           _version.cpython-314.pyc
    │       │           __init__.cpython-314.pyc
    │       │
    │       └───__pycache__
    │               py.cpython-314.pyc
    │
    └───Scripts
            activate
            activate.bat
            activate.fish
            Activate.ps1
            deactivate.bat
            pip.exe
            pip3.14.exe
            pip3.exe
            py.test.exe
            pygmentize.exe
            pytest.exe
            python.exe
            pythonw.exe



9 **¿Qué hay dentro de las carpetas principales? **

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

Conclusión
Hacer pruebas automáticas es como ponerle frenos seguros a una bicicleta antes de salir a rodar: nos permite atrapar los errores antes de que se conviertan en problemas grandes, asegurando que nuestro código funcione siempre a la primera y sin trampas.
