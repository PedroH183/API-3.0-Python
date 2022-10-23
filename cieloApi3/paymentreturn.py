from datetime import datetime

from cieloApi3 import CreditCard


class PaymentReturn(object):
    def __init__(self):
        self.payment_id = None
        self.recurrent_payment_id = None
        self.id_ordem = None
        self.tid = None
        self.installments = None
        self.capture = None
        self.recurrent = None
        self.credit_card = None
        self.amount = None
        self.received_date = None
        self.status = None

    def update_return(self, r):
        self.id_ordem = r.get('MerchantOrderId')

        rp = r.get('Payment') or {}
        self.payment_id = rp.get('PaymentId')
        self.tid = rp.get('Tid')
        self.installments = rp.get('Installments')
        self.capture = rp.get('Capture')
        self.recurrent = rp.get('Recurrent')
        self.amount = rp.get('Amount')
        self.received_date = datetime.strptime(rp.get('ReceivedDate'), '%Y-%m-%d %H:%M:%S')
        self.status = rp.get('Status')

        cc = rp.get('CreditCard') or {}
        self.credit_card = CreditCard(None, None)
        self.credit_card.card_number = cc.get('CardNumber')
        self.credit_card.holder = cc.get('Holder')
        self.credit_card.expiration_date = cc.get('ExpirationDate')
        self.credit_card.brand = cc.get('Brand')

        recurrent_payment = rp.get('RecurrentPayment') or {}
        self.recurrent_payment_id = recurrent_payment.get('RecurrentPaymentId')
