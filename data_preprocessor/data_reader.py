import pandas as pd
class DataReader:
    def __init__(self) -> None:
        RELATIVE_PATH = "..\\data\\aml-anomaly-detection\\"
        self.df_transaction =\
            pd.read_csv(f"{RELATIVE_PATH}SAML-D.csv").head(100000)