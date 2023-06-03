from engine.engine import CarEngine


class SternmanEngine(CarEngine):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def need_Service(self):
        return self.warning_light_is_on
    