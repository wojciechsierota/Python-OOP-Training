import random

class Rocket:
    def __init__(self):
        self.altitude = 0
        self.moves_count = 0
        self.average_speed = 0
        
    def move_up(self, distance):
        self.altitude += distance
        self.moves_count += 1

    def calculate_average(self):
        if self.moves_count > 0:
            self.average_speed = self.altitude / self.moves_count
        return self.average_speed
    
    def __str__(self):
        return f"Rocket altitude: {self.altitude}, average speed: {self.calculate_average():.2f}"



class RocketBoard:
    def __init__(self, amount_of_rockets=5):
        self.rockets = [Rocket() for _ in range(amount_of_rockets)]
        self._simulate_flights()

    def _simulate_flights(self):
        for rocket in self.rockets:
            for _ in range(10):
                speed = random.randint(0, 100)
                
                if speed <= 25:
                    rocket.move_up(random.randint(0, 5))
                elif 25 < speed <= 50:
                    rocket.move_up(random.randint(5, 10))
                elif 50 < speed <= 75:
                    rocket.move_up(random.randint(10, 15))
                elif 75 < speed <= 100:
                    rocket.move_up(random.randint(15, 20))

            print(rocket)


if __name__ == "__main__":
    RocketBoard()