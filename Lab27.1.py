class SimpleCar:
    def __init__(self):
        self.miles = 0

    def drive(self, dist):
        self.miles = self.miles + dist

    def reverse(self, dist):
        self.miles = self.miles - dist

    def get_odometer(self):
        return self.miles

    def honk_horn(self):
        print('beep beep')

    def report(self):
        print('Car has driven: {} miles'.format(self.miles))

if __name__ == "__main__":
    # TODO: Create SimpleCar object
    # TODO: Drive input number of miles forward
    # TODO: Drive input number of miles in reverse
    # TODO: Honk the horn
    # TODO: Report car status
    my_car = SimpleCar()
    miles_forward = int(input())
    miles_reverse = int(input())

    my_car.reverse(miles_reverse)
    my_car.drive(miles_forward)

    my_car.honk_horn()
    my_car.report()



