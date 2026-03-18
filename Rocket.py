import random

class Rocket:

    def __init__(self):
        self.altitude = 0
        self.movesCount = 0
        self.average = 0
        
    

    def moveUp(self,add):
        self.altitude += add
        self.movesCount += 1


    def calculate_average(self):
        if self.movesCount > 0:
            self.average = self.altitude / self.movesCount
        return self.average
    
    def __str__(self):
        return f"Wysokość rakiety: {self.altitude}, a jej średnia prędkość to: {self.calculate_average()}"



class RocketBoard:
    def __init__(self, amount_of_rockets = 5):
        self.rockets = [Rocket() for _ in range(amount_of_rockets)]


        for rocket in self.rockets:
            for _ in range(10):
                speed = random.randint(0,100)
                if speed <= 25:
                    rocket.moveUp(random.randint(0,5))
                elif 25 < speed <= 50:
                    rocket.moveUp(random.randint(5,10))
                elif 50 < speed <= 75:
                    rocket.moveUp(random.randint(10,15))
                elif 75 < speed <= 100:
                    rocket.moveUp(random.randint(15,20))
            print(rocket)


if __name__ == "__main__":
    RocketBoard()
