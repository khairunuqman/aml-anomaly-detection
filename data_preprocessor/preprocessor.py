from data_preprocessor.data_reader import  DataReader
import pandas as pd
import re
class PreProcessor(DataReader):
    def __init__(self) -> None:
        super().__init__()
        self.input_data_schema()
    

    def input_data_schema(self):
        self.df_transaction.columns = self.dataframe_col_rename_std(self.df_transaction)
        self.df_transaction['id'] = self.df_transaction['time']+'_'+self.df_transaction['date']+'_'+self.df_transaction['sender_account'].astype(str)
        self.df_transaction['date'] = pd.to_datetime(self.df_transaction['date'])
        self.df_transaction['time'] = pd.to_timedelta(self.df_transaction['time'])
        self.df_transaction['time'] = self.df_transaction['time'].dt.total_seconds().astype(int)
        self.df_transaction['time'] = pd.to_datetime(self.df_transaction['time'], unit='s').dt.time

    def dataframe_col_rename_std(self,df) -> pd.DataFrame:
        return [re.sub('[^a-zA-Z0-9_]', '_', col.lower().replace(' ', '_')) for col in df.columns]