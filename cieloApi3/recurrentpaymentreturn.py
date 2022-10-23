

class RecurrentPaymentReturn(object):
    def __init__(self):
        self.recurrent_payment_id = None
        self.start_date = None
        self.end_date = None
        self.next_recurrency = None
        self.interval = None
        self.amount = None
        self.create_date = None
        self.current_recurrency_try = None
        self.recurrency_day = None
        self.status = None

    def update_return(self, r):
        rp = r.get('RecurrentPayment') or {}
        self.recurrent_payment_id = rp.get('RecurrentPaymentId')
        self.start_date = rp.get('StartDate')
        self.end_date = rp.get('EndDate')
        self.next_recurrency = rp.get('NextRecurrency')
        self.interval = rp.get('Interval')
        self.amount = rp.get('Amount')
        self.create_date = rp.get('CreateDate')
        self.current_recurrency_try = rp.get('CurrentRecurrencyTry')
        self.recurrency_day = rp.get('RecurrencyDay')
        self.status = rp.get('Status')
