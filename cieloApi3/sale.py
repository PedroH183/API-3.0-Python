from .objectJSON import ObjectJSON


class Sale(ObjectJSON):

    def __init__(self, merchant_order_id):

        self.merchant_order_id = merchant_order_id
        self.customer = None
        self.payment = None

    def update_return(self, r):

        payment = r.get('Payment') or {}
        self.payment.payment_id = payment.get('PaymentId')
        self.payment.url = payment.get('Url')
        self.payment.tid = payment.get('Tid')
        self.payment.installments = payment.get('Installments')
        self.payment.status = payment.get('Status')
        self.payment.return_message = payment.get('ReturnMessage')
        self.payment.received_date = payment.get('ReceivedDate')

        if self.payment.recurrent_payment:
            recurrent = payment.get('RecurrentPayment') or {}
            self.payment.recurrent_payment.recurrent_payment_id = recurrent.get('RecurrentPaymentId')
            self.payment.recurrent_payment.next_recurrency = recurrent.get('NextRecurrency')
            self.payment.recurrent_payment.interval = recurrent.get('Interval')
