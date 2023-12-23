from data_preprocessor import PreProcessor
from data_model import DataModel

data_preprocessor = PreProcessor()
data_model = DataModel()
data_model.set_df_transaction(data_preprocessor.df_transaction)
data_model.initialize()
pass