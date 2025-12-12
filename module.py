
from function import add
result = int(add(45,45))
print('result: ',result)

from kargs_multiple import famous_name as fn
f_name = fn(first = 'harami',last = 'chorami', original = 'aksh')
print('Name from module: ',f_name)

from scope import *
