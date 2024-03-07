class Billing:
    def __init__(self, **kwargs):
        self.products = kwargs
        self.gst = 18

    def total_price(self):
        price = 0
        for key, value in self.products.items():
            price += value
        return price

    def total_gst(self):
        return self.total_price()*self.gst/100

    def print_bill(self):
        print(f"Billing Name: {self.name}")
        for key, value in self.products.items():
            print(f"{key} : {value}")
        print("=" * 20)
        print(f"Total Price: {self.total_price()}")
        print(f"GST Price: {self.total_gst()}")
        print("=" * 20)
        print(f"Grand Total: {self.total_gst() + self.total_price()}")


class Customers(Billing):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name


bill = Customers(name="Sourav", Rice=300, Wheat=500)
bill.print_bill()




