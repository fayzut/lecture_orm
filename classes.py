class Flight:
    counter = 1
    def __init__(self, origin, dest, duration):
        self.id = Flight.counter
        Flight.counter += 1

        self.passengers = []

        self.origin = origin
        self.destination = dest
        self.duration = duration
    def print_info(self):
        print(f"Вылет из: {self.origin}")
        print(f"Вылет в: {self.destination}")
        print(f"Время полета: {self.duration} мин")

        print(f"Пассажиры: ")
        for pas in self.passengers:
            print(pas.name, end=', ')

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id


class Passenger:
    def __init__(self, name):
        self.name = name


def main():
    f = Flight(origin="Nab Chelny", dest="Moscow", duration=180)
    f.delay(10)
    f.print_info()
    f1 = Flight("Москва", "Набережные Челны",180)
    f1.delay(-10)
    f1.print_info()

    ildar = Passenger("Ильдар")
    timur = Passenger("Тимур")

    f.add_passenger(ildar)
    f.add_passenger(timur)

    f.print_info()
#чтобы основная функция
#  не запускалась при импорте,
#  а запускалась только при вызове
if __name__ == "__main__":
    main()
