from datetime import datetime, time

class Reserva:
    # Servicios permitidos por las reglas de negocio
    SERVICIOS_PERMITIDOS = {"asesoria", "soporte", "demostracion"}
    
    # Duraciones permitidas en minutos
    DURACIONES_PERMITIDAS = {30, 60}
    
    # Horario de atención (Lunes a Viernes de 08:00 a 17:00)
    HORA_INICIO = time(8, 0)
    HORA_FIN = time(17, 0)

    def __init__(self, cliente: str, servicio: str, fecha_hora: datetime, duracion_minutos: int, codigo_confirmacion: str = None):
        self.cliente = cliente
        self.servicio = servicio
        self.fecha_hora = fecha_hora
        self.duracion_minutos = duracion_minutos
        self.codigo_confirmacion = codigo_confirmacion or self._generar_codigo()

    def _generar_codigo(self) -> str:
        """Genera un código de confirmación único basado en el cliente y la marca de tiempo."""
        import uuid
        return f"RES-{uuid.uuid4().hex[:8].upper()}"

    def es_dia_laboral(self) -> bool:
        """Verifica que la reserva sea de lunes (0) a viernes (4)."""
        return self.fecha_hora.weekday() < 5

    def esta_en_horario_atencion(self) -> bool:
        """Verifica que la hora de la reserva esté entre las 08:00 y las 17:00."""
        hora_reserva = self.fecha_hora.time()
        return self.HORA_INICIO <= hora_reserva <= self.HORA_FIN

    def validar(self):
        """Valida todas las reglas de negocio antes de aceptar la reserva."""
        if not self.cliente or not self.cliente.strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")
        
        if self.servicio not in self.SERVICIOS_PERMITIDOS:
            raise ValueError(f"Servicio no permitido. Opciones válidas: {', '.join(self.SERVICIOS_PERMITIDOS)}")
        
        if self.duracion_minutos not in self.DURACIONES_PERMITIDAS:
            raise ValueError("La duración debe ser estrictamente de 30 o 60 minutos.")
        
        if not self.es_dia_laboral():
            raise ValueError("Las reservas solo se permiten de lunes a viernes.")
        
        if not self.esta_en_horario_atencion():
            raise ValueError("La hora de la reserva debe estar entre las 08:00 y las 17:00.")

    def __repr__(self):
        return f"<Reserva {self.codigo_confirmacion} - {self.cliente} ({self.servicio})>"