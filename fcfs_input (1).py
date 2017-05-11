#!user/bin/python

print (" welcome Here is First Come First Serve ")
#p={1 : [0,5] , 2 : [3,6],3 : [4,7]}   # Dictionry save
p ={}
total=0
b_time=[]
a_time=[]
#atime=[0],b_time=[0]
n= input(" enter process number: ") 
for index in range (0,n):
	num= input(" enter arrival time ")
	a_time.append(num)
	num1 = input(" enter burst time ")
	b_time.append(num1)
	p[a_time[index]] = [index+1,b_time[index]]

	#b_time[i]= input(" enter bus time")
a_time.sort()
#for i in range (1,n):
	#print a_time[i] , "  "


for index in range (0,n):
	
	b_time = p.get(a_time[index])[1]
	total = total + b_time;
 	print  "Process " ,p.get(a_time[index])[0],"complete its time in :" ,total

	
