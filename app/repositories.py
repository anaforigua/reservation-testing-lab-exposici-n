from datetime import date, time
from typing import List, Dict, Any

class InMemoryReservationRepository:
    def __init__(self):
        self._reservations: List[Dict[str, Any]] = []

    def exists(self, reservation_date: date, reservation_time: time) -> bool:
        """Comprueba si ya existe una reserva para una fecha y hora determinadas."""
        for res in self._reservations:
            if res["date"] == reservation_date and res["time"] == reservation_time:
                return True
        return False

    def save(self, reservation: Dict[str, Any]) -> Dict[str, Any]:
        """Guarda una nueva reserva en la lista interna."""
        self._reservations.append(reservation)
        return reservation

    def get_all(self) -> List[Dict[str, Any]]:
        """Devuelve una lista con todas las reservas almacenadas."""
        return list(self._reservations)

    def clear(self):
        """Limpia el repositorio (útil para aislar pruebas)."""
        self._reservations.clear()