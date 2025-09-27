class OldPaymentSystem:
    def charge(self, amount):
        print(f"Processing the payment of amount ${amount} using a legacy system")

class ThirdPartyPaymentGateway:
    def make_payment(self, amount_cents, currency):
        print(f"Processing payment of {amount_cents/100} {currency} using 3rd party payment api")


class PaymentProcessor:
    def process_payment(self, amount, currency):
        raise NotImplementedError("This method should be implemented by subclasses.")


class OldPaymentAdapter(PaymentProcessor):
    def __init__(self, old_payment_system: OldPaymentSystem):
        self.old_payment_system = old_payment_system

    def process_payment(self, amount, currency):
        self.old_payment_system.charge(amount)



class ThirdPartyPaymentAdapter(PaymentProcessor):
    def __init__(self, third_party_payment_gateway: ThirdPartyPaymentGateway):
        self.third_party_payment_gateway = third_party_payment_gateway
    
    def process_payment(self, amount, currency):
        self.third_party_payment_gateway.make_payment(amount*100, currency)


# Legacy and Third-Party Payment Systems
old_payment_system = OldPaymentSystem()
third_party_gateway = ThirdPartyPaymentGateway()

# Adapters
old_payment_adapter = OldPaymentAdapter(old_payment_system)
third_party_adapter = ThirdPartyPaymentAdapter(third_party_gateway)

# Unified Application Code
def process_order(payment_processor, amount, currency):
    payment_processor.process_payment(amount, currency)

# Using Legacy System
process_order(old_payment_adapter, 100, "USD")

# Using Third-Party Gateway
process_order(third_party_adapter, 250.75, "USD")
