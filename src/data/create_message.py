import pandas as pd 
df = pd.read_csv("fake_data.csv")
names = df.columns


for name in names:
    df[name] = df[name].astype("str")


data = []
for r in range(len(df)):
    data_row = []
    for i in range(len(names)):
        data_row.append(df.iloc[r,:][i])
    data.append(data_row)

tests = []
for ele in data:
        txt = ','.join(ele)
        tests.append(txt)

dic = {"row_data" :tests}
fake_data = pd.DataFrame(dic)
dic = {"row_data" :tests}
fake_data = pd.DataFrame(dic)
# reomve the label from message 
fake_data = fake_data.iloc[:-1]
fake_data.to_csv("traffic.csv")