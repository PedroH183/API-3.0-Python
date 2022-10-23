from .request.createSale import CreateSale
from .request.modifyRecurrencyAmount import ModifyRecurrencyAmount
from .request.modifyRecurrencyCreditCard import ModifyRecurrencyCreditCard
from .request.modifyRecurrencyDay import ModifyRecurrencyDay
from .request.modifyRecurrencyNextPaymentDate import ModifyRecurrencyNextPaymentDate
from .request.queryOrder import QueryOrder
from .request.querySale import QuerySale
from .request.updateSale import UpdateSale
from .request.createCardToken import CreateCardToken
from .request.queryRecorrency import QueryRecorrency
from .request.deactivateRecorrency import DeactivateRecorrency
from .request.reactivateRecorrency import ReactivateRecorrency
from .request.zeroAuth import ZeroAuth


class CieloEcommerce(object):

    def __init__(self, merchant, environment):

        self.environment = environment
        self.merchant = merchant

    def create_sale(self, sale):
        request = CreateSale(self.merchant, self.environment)
        return request.execute(sale)

    def capture_sale(self, payment_id, amount=None, service_tax_amount=None):
        request = UpdateSale('capture', self.merchant, self.environment)
        request.amount = amount
        request.service_tax_amount = service_tax_amount
        return request.execute(payment_id)

    def cancel_sale(self, payment_id, amount=None):
        request = UpdateSale('void', self.merchant, self.environment)
        request.amount = amount
        return request.execute(payment_id)

    def get_sale(self, payment_id):
        request = QuerySale(self.merchant, self.environment)
        return request.execute(payment_id)

    def create_card_token(self, credit_card):
        request = CreateCardToken(self.merchant, self.environment)
        return request.execute(credit_card)

    def get_recurrent_payment(self, recurrent_payment_id):
        request = QueryRecorrency(self.merchant, self.environment)
        return request.execute(recurrent_payment_id)

    def deactivate_recurrent_payment(self, recurrent_payment_id):
        request = DeactivateRecorrency(self.merchant, self.environment)
        return request.execute(recurrent_payment_id)

    def reactivate_recurrent_payment(self, recurrent_payment_id):
        request = ReactivateRecorrency(self.merchant, self.environment)
        return request.execute(recurrent_payment_id)

    def modify_recurrency_day(self, recurrent_payment_id, day):
        request = ModifyRecurrencyDay(self.merchant, self.environment)
        return request.execute(recurrent_payment_id, day)

    def modify_recurrency_next_payment_date(self, recurrent_payment_id, string_date):
        request = ModifyRecurrencyNextPaymentDate(self.merchant, self.environment)
        return request.execute(recurrent_payment_id, string_date)

    def modify_recurrency_amount(self, recurrent_payment_id, amount):
        request = ModifyRecurrencyAmount(self.merchant, self.environment)
        return request.execute(recurrent_payment_id, amount)

    def modify_recurrency_credit_card(self, payment, recurrent_payment_id):
        request = ModifyRecurrencyCreditCard(self.merchant, self.environment)
        return request.execute(payment, recurrent_payment_id)

    def get_order(self, order_id):
        request = QueryOrder(self.merchant, self.environment)
        return request.execute(order_id)

    def get_zero_auth(self, credit_card):
        request = ZeroAuth(self.merchant, self.environment)
        return request.execute(credit_card)
