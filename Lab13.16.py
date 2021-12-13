class VendingMachine:
    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print('Inventory: {} bottles'.format(self.bottles))

if __name__ == "__main__":
    # TODO: Create VendingMachine object
    # TODO: Purchase input number of drinks
    # TODO: Restock input number of bottles
    # TODO: Report inventory
    vendingMachine = VendingMachine()
    num_drinks = int(input())
    num_bottles = int(input())

    vendingMachine.purchase(num_drinks)
    vendingMachine.restock(num_bottles)

    vendingMachine.report()


