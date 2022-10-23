from .base import Base


class ZeroAuth(Base):

    def __init__(self, merchant, environment):

        super(ZeroAuth, self).__init__(merchant)

        self.environment = environment

    def execute(self, credit_card):

        uri = '%s1/zeroauth' % self.environment.api

        response = self.send_request("POST", uri, credit_card)

        return response
