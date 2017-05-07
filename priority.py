#!user/bin/python

print (" welcome Here is Priority Based  ")
p={1 : [0,6,1] , 2 : [3,6,2],3 : [4,7,3]}   # Dictionry save
#p = []
total=0
b_time=[]
a_time=[]


for index in range (1,4):
	
	print (" time of process " ), index 
	print total, "-----"
	b_time=p.get(index)[1]
	#b_time[index+1] = p.get(index)[1]
	#if b_time[index] < b_time[index+1]:
	total=total+b_time

print total
	
