from typing import List


class Car:
    def __init__(
            self, comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        if 1 <= comfort_class <= 7:
            self.comfort_class = comfort_class
        if 1 <= clean_mark <= 10:
            self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_power: int,
        average_rating: float,
        count_of_ratings: int,
    ) -> None:

        if 1.0 <= distance_from_city_center <= 10.0:
            self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        if 1.0 <= average_rating <= 5.0:
            self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: List[Car]) -> float:
        total_cost = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                total_cost += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(total_cost, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (
            car.comfort_class
            * (self.clean_power - car.clean_mark)
            * self.average_rating
            / self.distance_from_city_center
        )
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, mark: int) -> None:
        self.average_rating = round(
            ((self.average_rating * self.count_of_ratings) + mark)
            / (self.count_of_ratings + 1),
            1,
        )
        self.count_of_ratings += 1
