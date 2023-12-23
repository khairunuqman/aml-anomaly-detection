import pandas as pd
from data_model.user import User
from data_model.transaction import Transaction
from scipy.stats import median_abs_deviation
import numpy as np
class DataModel:
    def __init__(self) -> None:
        self.df_transaction = pd.DataFrame()
        self.users = {}
        self.transactions = {}
        self.MAD = 0
        self.MEDIAN = 0

    def set_df_transaction(self, df):
        self.df_transaction = df
        self.MAD = median_abs_deviation(df['amount'])
        self.MEDIAN = np.median(df['amount'])

    def initialize(self):
        self.fill_data_objects()
        self.evaluate_anomaly()

    def fill_data_objects(self):
        for _,data in self.df_transaction.iterrows():
            if data.sender_account not in self.users:
                self.create_new_user(data.sender_account)
            if data.receiver_account not in self.users:
                self.create_new_user(data.receiver_account)
            self.create_new_transaction(data)

    def evaluate_anomaly(self):
        for tx_id in self.transactions:
            lb_z_score_cond = self.transactions[tx_id].z_score <= -3.5
            ub_z_score_cond = self.transactions[tx_id].z_score >= 3.5
            if lb_z_score_cond or ub_z_score_cond:
                self.transactions[tx_id].set_anomaly_to_true()

    def create_new_user(self, account):
        user = User(account)
        self.users[user.get_id()] = user

    def create_new_transaction(self, data):
        sender = self.users[data.sender_account]
        receiver = self.users[data.receiver_account]
        transaction = Transaction(data.id, data.time, data.date, sender, receiver, data.amount,data.payment_currency, data.received_currency)
        transaction.set_z_score(self.compute_robust_z_score(data.amount))
        self.transactions[transaction.get_id()] = transaction
        sender.add_tx_as_sender(transaction)
        receiver.add_tx_as_receiver(transaction)

    def compute_robust_z_score(self, X:float):
        return (0.6745 * (X - self.MEDIAN)) / self.MAD