#import pandas as pd
#data = {'Name' :['Tom','Jack','Steve','Ricky'],'Age':[29,34,56,12]}
#df = pd.DataFrame(data)
#print(df)

#import pandas as pd
#data = {'Name' :['Tom','Jack','Steve','Ricky'],'Age':[12,45,23,44]}
#df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
#print(df)

'''import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','Jerry','Vikas','Mohan','Smith','Robin']),
     'Age':pd.Series([34,55,23,34,54,65]),
     'Ratind':pd.Series([4.23,3.45,3.76,2.67,4.09,3.3])}
df = pd.DataFrame(d)
print("Our Data Series is :")
print(df)

import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','Jerry','Vikas','Mohan','Smith','Robin']),
     'Age':pd.Series([34,55,23,34,54,65]),
     'Ratind':pd.Series([4.23,3.45,3.76,2.67,4.09,3.3])}
df = pd.DataFrame(d)
print("The Transpose of Data Series is :")
print(df.T)

import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','Jerry','Vikas','Mohan','Smith','Robin']),
     'Age':pd.Series([34,55,23,34,54,65]),
     'Ratind':pd.Series([4.23,3.45,3.76,2.67,4.09,3.3])}
df = pd.DataFrame(d)
print("Row axis label and column axis label are :")
print(df.axes)

import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','Jerry','Vikas','Mohan','Smith','Robin']),
     'Age':pd.Series([34,55,23,34,54,65]),
     'Ratind':pd.Series([4.23,3.45,3.76,2.67,4.09,3.3])}
df = pd.DataFrame(d)
print("Datatype of each column are :")
print(df.dtypes)


import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','Jerry','Vikas','Mohan','Smith','Robin']),
     'Age':pd.Series([34,55,23,34,54,65]),
     'Ratind':pd.Series([4.23,3.45,3.76,2.67,4.09,3.3])}
df = pd.DataFrame(d)
print(df)
print("The Shape of the Object is :")
print(df.shape)


import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','Jerry','Vikas','Mohan','Smith','Robin']),
     'Age':pd.Series([34,55,23,34,54,65]),
     'Ratind':pd.Series([4.23,3.45,3.76,2.67,4.09,3.3])}
df = pd.DataFrame(d)
print(df)
print("The Actual data in our dta frame is :")
print(df.values)


import pandas as pd
import numpy as np

d = {'Name':pd.Series(['Tom','Jerry','Vikas','Mohan','Smith','Robin']),
     'Age':pd.Series([34,55,23,34,54,65]),
     'Ratind':pd.Series([4.23,3.45,3.76,2.67,4.09,3.3])}
df = pd.DataFrame(d)
print(df)
print("The first two rows of head nd tail are :")
print(df.head(2))
print(df.tail(2))'''


#CREATING A SERIES

#import pandas as pd
#s = pd.Series()
#print(s)


#import pandas as pd
#import numpy as np
#data = np.array(['a','b','c','d'])
#s = pd.Series(data)
#print(s)


#create series from dictonary

import pandas as pd
import numpy as np
data = {'a':0,'b':7.8,'c':5,'d':3}
s = pd.Series(data)
print(s)
