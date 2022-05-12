from prac_08.unreliable_car import UnreliableCar


def main():
    new_car = UnreliableCar("Toyota", 100, 40.6)
    print(new_car.__str__())
    print("distance driven = {}km".format(new_car.drive(40)))


if __name__ == '__main__':
    main()
