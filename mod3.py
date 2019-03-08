def func1():
	print("Hey")
	print("sup")
func1()

def func2(b):
	print("Hey",b)
func2(3)

def func3(a,b,c):
	r=a+b+c
	print(a,b,c,r)
func3(2,5,6)

def func4(University="CMR"):
	print("I am in"+"\t"+University)
func4("IITM")
func4("IITB")
func4()

def func5(a,b,c):
	d=a+b+c
	return d
e=func5(1,2,6)
print(e)


def func6(a,b):
	print(" the other function")
	c=a+b
	return(c)

def func7():	
	print("calling the other function")
	s=func6(3,5)
	print("addition is",s)
func7()











