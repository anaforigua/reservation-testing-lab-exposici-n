from datetime import date, time
from app.exceptions import (
    InvalidCustomerNameError,
    InvalidServiceError,
    InvalidDurationError,
    InvalidReservationDateError,
    InvalidReservationTimeError
)

VALID_SERVICES = {"asesoria", "soporte", "demostracion"}
VALID_DURATIONS = {30, 60}

def validate_customer_name(name: str) -> str:
    if not isinstance(name, str):
        raise InvalidCustomerNameError("El nombre debe ser una cadena de texto.")
    normalized_name = name.strip()
    if len(normalized_name) < 3:
        raise InvalidCustomerNameError("El nombre del cliente debe tener mínimo 3 caracteres después de eliminar espacios.")
    return normalized_name

def validate_service(service: str) -> str:
    if not isinstance(service, str):
        raise InvalidServiceError("El servicio debe ser una cadena de texto.")
    normalized_service = service.strip().lower()
    if normalized_service not in VALID_SERVICES:
        raise InvalidServiceError(f"Servicio no permitido. Debe ser uno de: {VALID_SERVICES}")
    return normalized_service

def validate_duration(duration: int) -> int:
    if duration not in VALID_DURATIONS:
        raise InvalidDurationError("La duración permitida es únicamente 30 o 60 minutos.")
    return duration

def validate_reservation_date(res_date: date, current_date: date) -> date:
    if res_date < current_date:
        raise InvalidReservationDateError("No se puede crear una reserva para una fecha anterior a la actual.")
    # El método weekday() devuelve 5 para Sábado y 6 para Domingo
    if res_date.weekday() >= 5:
        raise InvalidReservationDateError("Solo se permiten reservas de lunes a viernes.")
    return res_date

def validate_reservation_time(res_time: time, duration_minutes: int) -> time:
    opening_time = time(8, 0)
    closing_time = time(17, 0)

    if res_time < opening_time:
        raise InvalidReservationTimeError("El horario de atención inicia a las 08:00.")

    # Convertir a minutos totales desde medianoche para calcular el cierre
    start_total_minutes = res_time.hour * 60 + res_time.minute
    end_total_minutes = start_total_minutes + duration_minutes
    closing_total_minutes = closing_time.hour * 60 + closing_time.minute

    if end_total_minutes > closing_total_minutes:
        raise InvalidReservationTimeError("La reserva debe finalizar máximo a las 17:00.")

    return res_time