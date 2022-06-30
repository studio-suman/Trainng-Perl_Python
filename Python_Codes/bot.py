# fun_list1 = []
# for i in range(5):
# def fun1(e):
# return e+i
# fun_list1.append(fun1)

# fun_list2 = []
# for i in range(5):
# def fun2(e,iv=i):
# return e+iv
# fun_list2.append(fun2)

# fun_list3 = [lambda e: e+i for i in range(5)]

# fun_list4 = [lambda e,iv=i: e+iv for i in range(5)]

# i=56
# # in Shell do
# ## ipython -i pythonDemo.py
# # Try these (copy text after the comment symbol and paste in the Python prompt):
# # print([f(10) for f in fun_list1])
# # print([f(10) for f in fun_list2])
# # print([f(10) for f in fun_list3])
# # print([f(10) for f in fun_list4])

import matplotlib.pyplot as plt
from pythonDemo import myplot, slin, sqfun
import matplotlib.pyplot as plt
import math

def myplot(min,max,step,fun1,fun2):
	plt.ion() # make it interactive
	plt.xlabel("The x axis")
	plt.ylabel("The y axis")
	plt.xscale('linear') # Makes a 'log' or 'linear' scale
	values = range(min,max,step)
	plt.plot(xvalues,[fun1(x) for x in xvalues],
		label="The first fun")
	plt.plot(xvalues,[fun2(x) for x in xvalues], linestyle='--',color='k',
		label=fun2.__doc__) # use the doc string of the function
	plt.legend(loc="upper right") # display the legend

def slin(x):
	"""y=2x+7"""
	return 2*x+7
def sqfun(x):
	"""y=(x-40)ˆ2/10-20"""
	return (x-40)**2/10-20

# Try the following:

# myplot(0,100,1,slin,sqfun)
# plt.legend(loc="best")
# import math
# plt.plot([41+40*math.cos(th/10) for th in range(50)],
# [100+100*math.sin(th/10) for th in range(50)])
# plt.text(40,100,"ellipse?")
# plt.xscale('log')
