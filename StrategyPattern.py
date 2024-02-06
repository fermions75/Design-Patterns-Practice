class PaymnetStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymnetStrategy):
    def pay(self, amount):
        print("Paying with Credit Card: ", amount)

class PayPalPayment(PaymnetStrategy):
    def pay(self, amount):
        print("Paying with PayPal: ", amount)

class BankTransferPayment(PaymnetStrategy):
    def pay(self, amount):
        print("Paying with Bank Transfer: ", amount)

class PaymentWay:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def make_payment(self, amount):
        self.payment_stragegy.pay(amount)


# Client code
if __name__ == "__main__":
    credit_card_payment = CreditCardPayment()
    pay_pal_payment = PayPalPayment()
    bank_transfer_payment = BankTransferPayment()

    way_of_payment = PaymentWay(credit_card_payment)
    way_of_payment.make_payment(100)

    way_of_payment = PaymentWay(pay_pal_payment)
    way_of_payment.make_payment(200)

    way_of_payment = PaymentWay(bank_transfer_payment)
    way_of_payment.make_payment(300)