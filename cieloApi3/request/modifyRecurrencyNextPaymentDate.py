
from .base import Base


class ModifyRecurrencyNextPaymentDate(Base):

    def __init__(self, merchant, environment):

        super(ModifyRecurrencyNextPaymentDate, self).__init__(merchant)

        self.environment = environment

    def execute(self, recurrent_payment_id, string_date):

        uri = '%s1/RecurrentPayment/%s/NextPaymentDate' % (self.environment.api, recurrent_payment_id)

        return self.send_request("PUT", uri, string_date)
