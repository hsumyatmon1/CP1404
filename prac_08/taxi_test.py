from prac_08.taxi import Taxi


def main():
    new_taxi = Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print(new_taxi.__str__())
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi.__str__())


if __name__ == '__main__':
    main()
