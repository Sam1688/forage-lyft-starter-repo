import unittest

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from car_factory import CarFactory
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from datetime import date



class BatteryTests(unittest.TestCase):
    def test_nubbin_battery_needs_service(self):
        current_date = date(2023, 6, 2)
        last_service_date = date(2014, 5, 15)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_does_not_need_service(self):
        current_date = date(2023, 6, 2)
        last_service_date = date(2022, 5, 15)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_spindler_battery_needs_service(self):
        current_date = date(2025, 6, 2)
        last_service_date = date(2022, 5, 15)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_does_not_need_service(self):
        current_date = date(2022, 6, 2)
        last_service_date = date(2022, 5, 15)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class EngineTests(unittest.TestCase):
    def test_capulet_engine_needs_service(self):
        current_mileage = 100000
        last_service_mileage = 60000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_does_not_need_service(self):
        current_mileage = 50000
        last_service_mileage = 40000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_needs_service(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_does_not_need_service(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_needs_service(self):
        current_mileage = 80000
        last_service_mileage = 10000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_does_not_need_service(self):
        current_mileage = 40000
        last_service_mileage = 30000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class CarTests(unittest.TestCase):
    def test_car_creation(self):
        engine = CapuletEngine(100000, 70000)
        battery = SpindlerBattery(date(2023, 6, 2), date(2022, 5, 15))
        car = Car(engine, battery)
        self.assertEqual(car.engine, engine)
        self.assertEqual(car.battery, battery)


class CarFactoryTests(unittest.TestCase):
    def test_create_calliope(self):
        current_date = date(2023, 6, 2)
        last_service_date = date(2022, 5, 15)
        current_mileage = 100000
        last_service_mileage = 70000
        car = CarFactory.create_calliope(
            current_date, last_service_date, current_mileage, last_service_mileage
        )
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_create_glissade(self):
        current_date = date(2023, 6, 2)
        last_service_date = date(2022, 5, 15)
        current_mileage = 80000
        last_service_mileage = 50000
        car = CarFactory.create_glissade(
            current_date, last_service_date, current_mileage, last_service_mileage
        )
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_create_palindrome(self):
        current_date = date(2023, 6, 2)
        last_service_date = date(2022, 5, 15)
        warning_light_is_on = True
        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, SternmanEngine)
        self.assertIsInstance(car.battery, SpindlerBattery)

    def test_create_rorschach(self):
        current_date = date(2023, 6, 2)
        last_service_date = date(2022, 5, 15)
        current_mileage = 40000
        last_service_mileage = 30000
        car = CarFactory.create_rorschach(
            current_date, last_service_date, current_mileage, last_service_mileage
        )
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, WilloughbyEngine)
        self.assertIsInstance(car.battery, NubbinBattery)

    def test_create_thovex(self):
        current_date = date(2023, 6, 2)
        last_service_date = date(2022, 5, 15)
        current_mileage = 50000
        last_service_mileage = 40000
        car = CarFactory.create_thovex(
            current_date, last_service_date, current_mileage, last_service_mileage
        )
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car.engine, CapuletEngine)
        self.assertIsInstance(car.battery, NubbinBattery)


if __name__ == '__main__':
    unittest.main()

