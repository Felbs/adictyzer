
  -->>> adictyzer - a python data tool <<<--

  Hey Github, 


  this script turns an csv file into a python dictionary. A simple but nice algorithm.



  -- Quick review --


>>> from adictyzer import *

>>> dt = read_csv('example.csv' sep=",")

>>> dt
{'name':['alfred', 'caroline', 'ana', 'jeffrey', 'bill'], 'age': ['74', '32', '24', '35', '49']}

>>> gind(1, dt)
['caroline', '32']

>>> sum(dt['age'])
'214.00'
