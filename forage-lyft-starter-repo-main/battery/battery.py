from abc import ABC, abstractmethod


class Battery(ABC):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def get_last_service_date(self):
        return self.last_service_date

    def get_current_date(self):
        return self.current_date

    @abstractmethod
    def need_Service(self):
        pass

    