
from .base import Base


class ModifyRecurrencyAmount(Base):

    def __init__(self, merchant, environment):

        super(ModifyRecurrencyAmount, self).__init__(merchant)

        self.environment = environment

    def execute(self, recurrent_payment_id, amount):

        uri = '%s1/RecurrentPayment/%s/Amount' % (self.environment.api, recurrent_payment_id)

        return self.send_request("PUT", uri, amount)
