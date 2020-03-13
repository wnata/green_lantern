from __future__ import annotations

from typing import List


class Jungle:

    def __init__(self, predators: List[Predator], herbivorous: List[Herbivorous]):
        self.predators = predators
        self.herbivorous = herbivorous


class Animal:

    def __init__(self, weight, speed):
        self.weight = weight
        self.speed = speed


class Predator(Animal):
    def __init__(self, weight, speed, power):
        super().__init__(weight, speed)
        self.power = power

    def hunt(self, jungle):
        for herb in jungle.herbivorous:
            if self.is_herb_a_victim(herb):
                return True
        return False

    def speed_of_herb_in_percent(self, herb: Herbivorous):
        return int(herb.speed * 100 / self.speed)

    def is_herb_a_victim(self, herb: Herbivorous):
        return self.power * 3 > herb.weight and self.speed > herb.speed * 1.15


class Herbivorous(Animal):
    pass


if __name__ == "__main__":
    simba = Predator(weight=100, speed=50, power=70)
    timon = Herbivorous(weight=10, speed=55)

    savana = Jungle(
        predators=[simba],
        herbivorous=[timon]
    )

    print(simba.hunt(savana))


