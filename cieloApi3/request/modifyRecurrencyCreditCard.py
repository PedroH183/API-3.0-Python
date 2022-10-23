
from .base import Base


class ModifyRecurrencyCreditCard(Base):

    def __init__(self, merchant, environment):

        super(ModifyRecurrencyCreditCard, self).__init__(merchant)

        self.environment = environment

    def execute(self, payment, recurrent_payment_id):

        uri = '%s1/RecurrentPayment/%s/Payment' % (self.environment.api, recurrent_payment_id)

        return self.send_request("PUT", uri, payment)
