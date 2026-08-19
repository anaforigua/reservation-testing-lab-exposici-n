from datetime import date, time
from typing import Callable, Dict, Any
from app.repositories import InMemoryReservationRepository
from app.validators import (
    validate_customer_name,
    validate_service,
    validate_duration,
    validate_reservation_date,
    validate_reservation_time
)
from app.exceptions import DuplicateReservationError

class ReservationService:
    def __init__(self, repository: InMemoryReservationRepository, code_generator: Callable[[], str]):
        self.repository = repository
        self.code_generator = code_generator

    def create(self, data: Dict[str, Any], current_date: date) -> Dict[str, Any]:
        # 1. Validar y normalizar datos básicos
        customer_name = validate_customer_name(data.get("customer_name", ""))
        service = validate_service(data.get("service", ""))
        duration = validate_duration(data.get("duration", 0))
        
        res_date = data.get("date")
        if not isinstance(res_date, date):
            raise ValueError("La fecha de reserva debe ser un objeto date válido.")
        
        res_time = data.get("time")
        if not isinstance(res_time, time):
            raise ValueError("La hora de reserva debe ser un objeto time válido.")

        # 2. Validar reglas de fecha y horario
        validate_reservation_date(res_date, current_date)
        validate_reservation_time(res_time, duration)

        # 3. Comprobar regla de duplicados (RN-08)
        if self.repository.exists(res_date, res_time):
            raise DuplicateReservationError("Ya existe una reserva para la misma fecha y hora.")

        # 4. Generar código de confirmación y estado (RN-09, RN-10)
        confirmation_code = self.code_generator()

        reservation_record = {
            "customer_name": customer_name,
            "service": service,
            "duration": duration,
            "date": res_date,
            "time": res_time,
            "status": "confirmed",
            "confirmation_code": confirmation_code
        }

        # 5. Guardar en repositorio y devolver
        return self.repository.save(reservation_record)