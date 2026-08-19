import pytest
from datetime import date, time
from app.exceptions import DuplicateReservationError, InvalidCustomerNameError

def test_create_reservation_success(reservation_service, reservation_repository, fixed_current_date, valid_reservation_data):
    # Act
    result = reservation_service.create(valid_reservation_data, fixed_current_date)

    # Assert
    assert result["status"] == "confirmed"
    assert result["confirmation_code"] == "CONF-TEST-001"
    assert result["customer_name"] == "Ana Gómez"
    assert len(reservation_repository.get_all()) == 1

def test_duplicate_reservation_raises_error(reservation_service, fixed_current_date, valid_reservation_data):
    # Arrange: Crear primera reserva exitosa
    reservation_service.create(valid_reservation_data, fixed_current_date)

    # Act & Assert: Intentar crear exactamente la misma fecha y hora debe lanzar excepción
    with pytest.raises(DuplicateReservationError):
        reservation_service.create(valid_reservation_data, fixed_current_date)

def test_validation_failure_does_not_persist(reservation_service, reservation_repository, fixed_current_date, valid_reservation_data):
    # Modificar con nombre inválido para provocar error de validación
    invalid_data = valid_reservation_data.copy()
    invalid_data["customer_name"] = "AB"

    with pytest.raises(InvalidCustomerNameError):
        reservation_service.create(invalid_data, fixed_current_date)

    # Comprobar que no se guardó ninguna reserva en el repositorio ante el fallo
    assert len(reservation_repository.get_all()) == 0

def test_repository_independence(reservation_service, reservation_repository, fixed_current_date, valid_reservation_data):
    # Comprobar que el repositorio inicia vacío y mantiene aislamiento
    assert len(reservation_repository.get_all()) == 0
    reservation_service.create(valid_reservation_data, fixed_current_date)
    assert len(reservation_repository.get_all()) == 1