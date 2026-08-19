class ReservationDomainError(Exception):
    """Excepción base para todos los errores de dominio de reservas."""
    pass

class InvalidCustomerNameError(ReservationDomainError):
    """Se lanza cuando el nombre del cliente no cumple con la longitud mínima."""
    pass

class InvalidServiceError(ReservationDomainError):
    """Se lanza cuando el servicio solicitado no está permitido."""
    pass

class InvalidDurationError(ReservationDomainError):
    """Se lanza cuando la duración no es de 30 o 60 minutos."""
    pass

class InvalidReservationDateError(ReservationDomainError):
    """Se lanza cuando la fecha es anterior a la actual o cae en fin de semana."""
    pass

class InvalidReservationTimeError(ReservationDomainError):
    """Se lanza cuando la hora está fuera de rango o la reserva excede las 17:00."""
    pass

class DuplicateReservationError(ReservationDomainError):
    """Se lanza cuando ya existe una reserva para la misma fecha y hora."""
    pass