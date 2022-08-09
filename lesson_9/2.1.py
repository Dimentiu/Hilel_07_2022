class Connection:
    def send_data(self, data):
        print(f"Connected based on {data}")


class PaymentSystem:
    def __init__(self, data):
        self.data = data

    def __do_connection(self, url):
        print(f"Connection to {url}")
        return Connection()

    def checkout(self):
        connection = self.__do_connection(self.url)
        connection.send_data(self.data)
        print("Success")


class Stripe(PaymentSystem):
    url = "https://stripe.com"

    def checkout(self):
        connection = self.__do_connection(self.url)
        connection.send_data(self.data)

        print("Success")


class PayPal(PaymentSystem):
    url = "https://paypal.com"


paypal = PayPal({"username": "john", "product": "iphone"})
stripe = Stripe({"username": "john", "product": "iphone"})

paypal.checkout()
stripe.checkout()