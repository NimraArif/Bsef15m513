#!user/bin/python

print (" welcome Here is First Come First Serve ")
p={1 : [0,5] , 2 : [3,6],3 : [4,7]}   # Dictionry save
#p = []
total=0
b_time=[]
a_time=[]
#atime=[0],b_time=[0]
#n= input(" enter process number: ") 
#for index in range (1,n):
	#a_time= input(" enter arrival time ")
	#a_time.append(time)
	#time1 = input(" enter arrival time ")
	#b_time.append(time1)
	#p[index+1] = [a_time[index],b_time[index]]

	#b_time[i]= input(" enter bus time")
#a_time.sort()
#for i in range (1,n):
	#print a_time[i] , "  "


for index in range (1,4):
	
	print (" time of process " )
	print total, "-----"a
	b_time=p.get(index)[1]
	total=total+b_time

print total
	
