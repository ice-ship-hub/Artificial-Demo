import pandas as pd

data = {
"Name": ["Alice", "Bob", "Jack", "Jane"],
"Age": [23, 14, 15, 25],
"City":["Nairobi", "Kisumu", "Nakuru", "Eldoret"],
}
df =  pd.DataFrame(data)
print(df)
