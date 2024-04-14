from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    price_per_km = 1.23
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness=0.0):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.current_fare_distance = 0

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}, {self.current_fare_distance}km on current fare, $" \
               f"{self.price_per_km * self.fanciness:.2f}/km plus flagfall of {self.flagfall}"

    def get_fare(self):
        return super().get_fare() * self.fanciness + self.flagfall

    def start_fare(self):
        super().start_fare()

    def drive(self, distance):
        super().drive(distance)
