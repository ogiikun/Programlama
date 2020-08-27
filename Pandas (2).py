import pandas as pd
soccer=pd.read_csv("C:\python\mls2017.csv")
soccer.head(n = 10) 
soccer[soccer["guaranteed_compensation"]==soccer["guaranteed_compensation"].max()]["last_name"]

def son_find(last_name):
    if "son" in last_name.lower() 
        return True
    return False
socccer[soccer["last_name"].apply]