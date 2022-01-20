import pandas as pd


class Data:

    @staticmethod
    def getdata():
        return pd.read_csv("res/50_Startups.csv")
