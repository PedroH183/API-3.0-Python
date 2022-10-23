
from .base import Base


class ModifyRecurrencyDay(Base):

    def __init__(self, merchant, environment):

        super(ModifyRecurrencyDay, self).__init__(merchant)

        self.environment = environment

    def execute(self, recurrent_payment_id, day):

        uri = '%s1/RecurrentPayment/%s/RecurrencyDay' % (self.environment.api, recurrent_payment_id)

        return self.send_request("PUT", uri, day)
