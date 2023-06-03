from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, last_service_date, engine, battery):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    def get_last_service_date(self):
        return self.last_service_date

    def get_engine(self):
        return self.engine

    def get_battery(self):
        return self.battery

    @abstractmethod
    def need_Service(self):
        pass