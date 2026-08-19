import pytest
from datetime import date, time
from app.validators import (
    validate_customer_name,
    validate_service,
    validate_duration,
    validate_reservation_date,
    validate_reservation_time
)
from app.exceptions import (
    InvalidCustomerNameError,
    InvalidServiceError,
    InvalidDurationError,
    InvalidReservationDateError,
    InvalidReservationTimeError
)

@pytest.mark.parametrize(
    "input_name, expected",
    [
        ("  Carlos Pérez  ", "Carlos Pérez"),
        ("Ana", "Ana"),
        ("Valentina", "Valentina")
    ]
)
def test_validate_customer_name_valid(input_name, expected):
    assert validate_customer_name(input_name) == expected

@pytest.mark.parametrize("invalid_name", ["Al", "   ", "Jo", ""])
def test_validate_customer_name_invalid(invalid_name):
    with pytest.raises(InvalidCustomerNameError):
        validate_customer_name(invalid_name)

@pytest.mark.parametrize(
    "input_service, expected",
    [
        ("asesoria", "asesoria"),
        ("  SOPORTE  ", "soporte"),
        ("DEMOSTRACION", "demostracion")
    ]
)
def test_validate_service_valid(input_service, expected):
    assert validate_service(input_service) == expected

@pytest.mark.parametrize("invalid_service", ["consultoria", "auditoria", "   "])
def test_validate_service_invalid(invalid_service):
    with pytest.raises(InvalidServiceError):
        validate_service(invalid_service)

@pytest.mark.parametrize("duration", [30, 60])
def test_validate_duration_valid(duration):
    assert validate_duration(duration) == duration

@pytest.mark.parametrize("invalid_duration", [15, 45, 90, 120])
def test_validate_duration_invalid(invalid_duration):
    with pytest.raises(InvalidDurationError):
        validate_duration(invalid_duration)

def test_validate_reservation_date_valid():
    current = date(2026, 6, 3) # Miércoles
    future_valid = date(2026, 6, 4) # Jueves
    assert validate_reservation_date(future_valid, current) == future_valid

def test_validate_reservation_date_past():
    current = date(2026, 6, 3)
    past_date = date(2026, 6, 2)
    with pytest.raises(InvalidReservationDateError):
        validate_reservation_date(past_date, current)

@pytest.mark.parametrize(
    "weekend_date",
    [
        date(2026, 6, 6), # Sábado
        date(2026, 6, 7)  # Domingo
    ]
)
def test_validate_reservation_date_weekend(weekend_date):
    current = date(2026, 6, 3)
    with pytest.raises(InvalidReservationDateError):
        validate_reservation_date(weekend_date, current)

@pytest.mark.parametrize(
    "res_time, duration",
    [
        (time(8, 0), 30),   # Apertura exacta (Frontera)
        (time(16, 30), 30), # Termina exactamente a las 17:00 (Frontera)
        (time(9, 0), 60)
    ]
)
def test_validate_reservation_time_valid(res_time, duration):
    assert validate_reservation_time(res_time, duration) == res_time

@pytest.mark.parametrize(
    "res_time, duration",
    [
        (time(7, 30), 30),  # Antes de apertura (Frontera inválida)
        (time(16, 45), 30), # Termina a las 17:15 (Pasa del cierre)
        (time(17, 0), 30)   # Inicia a la hora de cierre
    ]
)
def test_validate_reservation_time_invalid(res_time, duration):
    with pytest.raises(InvalidReservationTimeError):
        validate_reservation_time(res_time, duration)