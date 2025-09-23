from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount
        
    @abstractmethod
    def payment(self, amount):
        self.amount = amount
        pass
        


class CardPayment(Payment):
    def __init__(self, amount):
        self.amount = amount
    
    def payment(self):
        print(f"카드로 {self.amount}원을 결제합니다")


class CashPayment(Payment):
    def __init__(self, amount):
        self.amount = amount
    
    def payment(self):
        print(f"현금으로 {self.amount}원을 결제합니다.")

cardpayment = CardPayment(10000)
cashpayment = CashPayment(5000)

cardpayment.payment()
cashpayment.payment()
