#!user/bin/python

print (" welcome Here is First Come First Serve ")
p={1 : [0,5] , 2 : [3,6],3 : [4,7]}   # Dictionry save

total=0
b_time=[]
a_time=[]


for index in range (1,4):
	
	print (" time of process " ) , index 
	print total, "-----"
	b_time=p.get(index)[1]
	total=total+b_time

print total
	
