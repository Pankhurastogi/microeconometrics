import pandas as pd 
import numpy as np 
import os

rel_path = os.path.relpath("~/Documents/microecon/dataset/", "~/Documents/microecon/utils/")
file_path_w1 = os.path.join(rel_path, "WV1.csv")
file_path_w2 = os.path.join(rel_path, "WV2.csv")
file_path_w3 = os.path.join(rel_path, "WV3.csv")
file_path_w5 = os.path.join(rel_path, "WV5.csv")

df = pd.read_csv(file_path_w1, dtype = str)
for index, row in df.iterrows():
    v237 = int(df.loc[index,'V237'])
    y002 = int(df.loc[index, 'Y002'])
    if not (y002 > 1980 and y002 < 2000):
        df.loc[index, 'Y002'] = v237

df.to_csv(os.path.join(rel_path, "WV1_fixed.csv"), index=False)

df2 = pd.read_csv(file_path_w3, dtype = str)
for index, row in df2.iterrows():
    s025 = int(df2.loc[index,'S025'])
    v238 = int(df2.loc[index, 'V238'])
    if not (v238 > 1990 and v238 < 2000):
        df2.loc[index, 'V238'] = s025

df2.to_csv(os.path.join(rel_path, "WV3_fixed.csv"), index=False)

df3 = pd.read_csv(file_path_w2, dtype = str)
for index, row in df3.iterrows():
    s025 = int(df3.loc[index,'S025'])
    v377 = int(df3.loc[index, 'V377'])
    if not (v377 > 1985 and v377 < 2000):
        df3.loc[index, 'V377'] = s025

df3.to_csv(os.path.join(rel_path, "WV2_fixed.csv"), index=False)

df4 = pd.read_csv(file_path_w5, dtype = str)
for index, row in df4.iterrows():
    V260 = df4.loc[index,'V260']
    V262 = df4.loc[index,'V262']
    V261 = df4.loc[index,'V261']
    if V260 == np.nan:
        V262 = int(V262)
        if V262 > 2000 and V262 < 2010:
            df4.loc[index, 'V260'] = V262
        else:
            pass
    else:
        V260 = float(V260)
        if V260 > 2000 and V260 < 2010:
            pass
        else:
            V262 = float(V262)
            if V262 > 2000 and V262 < 2010:
                df4.loc[index, 'V260'] = V262
            else:
                V261 = float(V261)
                if V261 > 2000 and V261 < 2010:
                    df4.loc[index, 'V260'] = V261
                else:
                    pass

df4.to_csv(os.path.join(rel_path, "WV5_fixed.csv"), index=False)