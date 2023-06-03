from battery.battery import Battery


class SpindlerBattery(Battery):
    def need_Service(self):
        # Implement the service criteria for SpindlerBattery (2 years)
        return self.current_date.year - self.last_service_date.year >= 2
    