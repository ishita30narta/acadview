#1
import pandas as pd

d = {'Name':pd.Series(['Ishita Narta','abc']),
     'Age':pd.Series([21,33]),
     'Mail_id':pd.Series(['ishitanarta30@gmail.com','abc@gmail.com']),
     'Phone_no':pd.Series([7807841555,981457268])}
df = pd.DataFrame(d)
print(df)

#2
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/Shreyas3108/Weather/master/weather.csv")
a = df.head(5)
print(a)

b = df.head(10)
print(b)

c = df.describe()
print(c)

d = df.tail(5)
print(d)

second_col = df.iloc[:,2]
e = second_col.describe()
print(e)



