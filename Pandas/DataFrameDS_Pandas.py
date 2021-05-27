import pandas

df1 = pandas.DataFrame([[1,2,3],[4,5,6]],columns=["Price","Value","Age"],index=["First","Second"]) 

print(df1)

df2 = pandas.DataFrame([{"Name":"Chaitanya"},{"Name":"Parismita"}])

print(df2)