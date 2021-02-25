-->>> adictyzer - a python data tool <<<--

  Hey Github, 


  this script turns an csv file into a python dictionary. A simple but nice algorithm.

  V1.0 - initial version

  V2.0 - changed to object oriented style

    -> two new classes: Adict(dict), AdictList(list) 

    -> Functions like sum, mean, med are now object methods

    -> Also, a method called cols() from Adict class that prints columns

  -- Quick review --


>>> from adictyzer import *

>>> dt = read_csv('example.csv', sep=",")

>>> dt
{'name':['alfred', 'caroline', 'ana', 'jeffrey', 'bill'], 'age': ['74', '32', '24', '35', '49']}

>>> dt.gind(1)
['caroline', '32']

>>> dt['age'].sum()
'214.00'

