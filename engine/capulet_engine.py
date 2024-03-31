from abc import ABC

class Engine(ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        raise NotImplementedError("Subclasses must implement engine_should_be_serviced method")

class CapuletEngine(Engine):
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 30000
