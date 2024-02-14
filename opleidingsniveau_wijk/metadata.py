import pandas as pd

wijkcodes = pd.read_csv(r"C:\Users\SMR\data_analysis\opleidingsniveau_wijk\85740NED_metadata_wkbu.csv", delimiter=";")
opleidingcodes = pd.read_csv(r"C:\Users\SMR\data_analysis\opleidingsniveau_wijk\85740NED_metadata_opl.csv", delimiter=";")

wijkcodes.to_csv(r"C:\Users\SMR\data_analysis\opleidingsniveau_wijk\wijkcodes.csv")
opleidingcodes.to_csv(r"C:\Users\SMR\data_analysis\opleidingsniveau_wijk\opleidingcodes.csv")
