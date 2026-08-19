import pytest
from datetime import date, time
from app.repositories import InMemoryReservationRepository
from app.reservation_service import ReservationService

@pytest.fixture
def fixed_current_date():
    """Fixture que provee una fecha actual fija y conocida (miércoles)."""
    return date(2026, 6, 3)

@pytest.fixture
def valid_reservation_data():
    """Fixture que provee un diccionario con datos válidos de reserva."""
    return {
        "customer_name": "Ana Gómez",
        "service": "asesoria",
        "duration": 30,
        "date": date(2026, 6, 4),  # Jueves
        "time": time(10, 0)
    }

@pytest.fixture
def reservation_repository():
    """Fixture que provee una instancia nueva y vacía del repositorio en memoria."""
    return InMemoryReservationRepository()

@pytest.fixture
def deterministic_code_generator():
    """Fixture que provee un generador de código de confirmación determinista."""
    counter = 0
    def _generator():
        nonlocal counter
        counter += 1
        return f"CONF-TEST-{counter:03d}"
    return _generator

@pytest.fixture
def reservation_service(reservation_repository, deterministic_code_generator):
    """Fixture que provee una instancia de ReservationService construida con dependencias inyectadas."""
    return ReservationService(
        repository=reservation_repository,
        code_generator=deterministic_code_generator
    )