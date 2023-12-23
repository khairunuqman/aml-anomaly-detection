class User:
    def __init__(self,
                 id:str) -> None:
        self.id = id
        self.nb_as_sender = 0
        self.nb_as_receiver = 0
        self.nb_flagged_sent_anomaly = 0
        self.nb_flagged_received_anomaly = 0
        self.list_tx_id_as_sender = []
        self.list_tx_id_as_receiver = []

    def get_id(self):
        return self.id

    def add_tx_as_sender(self, tx_id:str):
        self.nb_as_sender += 1
        self.list_tx_id_as_sender.append(tx_id)

    def add_tx_as_receiver(self, tx_id:str):
        self.nb_as_receiver += 1
        self.list_tx_id_as_receiver.append(tx_id)

    def add_nb_flagged_sent_anomaly(self):
        self.nb_flagged_sent_anomaly += 1

    def add_nb_flagged_received_anomaly(self):
        self.nb_flagged_received_anomaly += 1