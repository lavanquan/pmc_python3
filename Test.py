import random
import pandas as pd


nb = 10
delta = 1000.0 / (nb + 1)
file_name = "thaydoisodiemsac" + str(nb) + ".csv"
df = pd.read_csv(file_name)
for nb_run in range(10):
    temp = ""
    for i in range(nb):
        for j in range(nb):
            x = int(delta * (i + random.random()))
            y = int(delta * (j + random.random()))
            if temp == "":
                temp = temp + "(" + str(x) + "," + str(y) + ")"
            else:
                temp = temp + ",(" + str(x) + "," + str(y) + ")"
    print(temp)
    df["charge_pos"][nb_run] = temp
df.to_csv(file_name)
