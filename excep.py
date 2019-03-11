try:
	list4=[1,2,3,5]
	print(list4[6])
except:
	print("Index is out of range")
else:
	print("Successfully executed")
finally:
	print("Completed")