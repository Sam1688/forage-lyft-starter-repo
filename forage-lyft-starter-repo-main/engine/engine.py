from abc import ABC, abstractmethod


class CarEngine(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def get_last_service_date(self):
        return self.last_service_date

    @abstractmethod
    def need_Service(self):
        pass
