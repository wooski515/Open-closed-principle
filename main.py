# Принцип відкритості/закритості (Open/Closed Principle)

class Discount:
    def calculate(self, amount):
        raise NotImplementedError("Підкласи повинні перевизначати метод розрахунку")

class LoyaltyDiscount(Discount):
    def calculate(self, amount):
        return amount * 0.1 

class HolidayDiscount(Discount):
    def calculate(self, amount):
        return amount * 0.2  

class Order:
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, discount: Discount):
        return self.amount - discount.calculate(self.amount)

if __name__ == "__main__":
    order = Order(1000)  

    loyalty_discount = LoyaltyDiscount()
    holiday_discount = HolidayDiscount()

    print(f"Початкова сума: ${order.amount}")
    print(f"Сума після знижки за лояльність: ${order.apply_discount(loyalty_discount):.2f}")
    print(f"Сума після святкової знижки: ${order.apply_discount(holiday_discount):.2f}")
