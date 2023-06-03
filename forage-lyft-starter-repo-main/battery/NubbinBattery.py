from battery.battery import Battery

class NubbinBattery(Battery):
    def need_Service(self):
        # Implement the service criteria for NubbinBattery (4 years)
        return self.current_date.year - self.last_service_date.year >= 4