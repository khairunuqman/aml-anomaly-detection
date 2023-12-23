from data_model.user import User
from datetime import datetime,time
class Transaction:
    def __init__(self,
                 id:str,
                 time:time,
                 date:datetime,
                 sender_id:User,
                 receiver_id:User,
                 amount:float,
                 payment_currency:str,
                 received_currency:str) -> None:
        self.id = id
        self.time = time
        self.date = date
        self.sender = sender_id
        self.receiver = receiver_id
        self.amount = amount
        self.payment_currency = payment_currency
        self.received_currency = received_currency
        self.z_score = 0
        self.is_anomaly = False

    def get_id(self):
        return self.id

    def set_z_score(self, z_score):
        self.z_score = z_score

    def set_anomaly_to_true(self):
        self.is_anomaly = True
        self.sender.add_nb_flagged_sent_anomaly()
        self.receiver.add_nb_flagged_received_anomaly()