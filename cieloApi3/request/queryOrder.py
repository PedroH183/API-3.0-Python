from .base import Base


class QueryOrder(Base):

    def __init__(self, merchant, environment):

        super(QueryOrder, self).__init__(merchant)

        self.environment = environment

    def execute(self, order_id):

        uri = '%s1/sales?merchantOrderId=%s' % (self.environment.api_query, order_id)

        return self.send_request("GET", uri)
