
#!user/bin/python

print (" welcome Here is SFJ based algo  ")
p={1 : [0,4] , 2 : [1,6],3 : [2,7]}   # Dictionry save
b=[]
process ={}
total=0
burst=[]
arrival=[]
#atime=[0],b_time=[0]
n= input(" enter process number: ") 
for i in range (0,n):
	a = input("Enter arrival time:")
	arrival.append(a)
	a1 = input("Enter burst time:")
	burst.append(a1)
	process[burst[i]]= [arrival[i],i+1]
#print "A.t " ,  " " , " " ,"B.t "
#for index in range (0,n):
	#print arrival[index] ," "  , burst [index]
	#process[burst[i]]= [arrival[i]]
burst.sort()

if ( total > 0 ):
	print " 0 ----------" , total, " Idle " 

for i in range (1,4):
	print (" time of process " ) , i 
	print total, "-----"
	b_time=p.get(index)[1]
	total=total+b_time
	

print total 









		




	
