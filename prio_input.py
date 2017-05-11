#!user/bin/python

print (" welcome Here is First Come First Serve ")
#p={1 : [0,5] , 2 : [3,6],3 : [4,7]}   # Dictionry save
p ={}
total=0
b_time=[]
a_time=[]
pr = []
#atime=[0],b_time=[0]
n= input(" enter process number: ") 
for index in range (0,n):
	print "Process" ,index 
	num= input(" enter arrival time ")
	
	a_time.append(num)
	num1 = input(" enter burst time ")
	b_time.append(num1)
	order = input(" enter prority: ")
	pr.append(order)
	p[pr[index]] = [a_time[index],index+1,b_time[index]]

	#b_time[i]= input(" enter bus time")
pr.sort()
#for i in range (1,n):
	#print a_time[i] , "  "


for index in range (0,n):
	
	total = total+ p.get(pr[index])[1]
	
 	print  "Complete time in " , p.get(pr[index])[2]

	
