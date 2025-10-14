#practice for pandas (a python library)
import pandas as pd
data = {
    "Name":["Divya","Heeya","Lekikha","Rakul"],
    "Age":["20","24","21","30"],
    "City":["Jaipur","Bhopal","Udaipur","Mumbai"]
}
df=pd.DataFrame(data)
print(df)
# df.to_csv("Output.csv",index= False)
# df.to_excel("Output.xlsx",index=False)
df.to_json("Output.json",index=False)