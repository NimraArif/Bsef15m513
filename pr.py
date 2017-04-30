
#!user/bin/python

print (" welcome Here is SFJ based algo  ")
#p={1 : [0,9] , 2 : [1,6],3 : [2,7]}   # Dictionry save
b=[]
process =[]
total=0
burst=[]
arrival=[]
#atime=[0],b_time=[0]
n= input(" enter process number: ") 
for i in range (0,n):
	num = input("Enter arrival time:")
	if (i==0):
		min = num
	elif(min>num):
		min = num
	arrival.append(num)
	num1 = input("Enter burst time:")
	burst.append(num1)
	process[burst[i]]= [arrival[i],i+1]
print "A.t " ,  " " , " " ,"B.t "
for index in range (0,n):
	print arrival[index] ," "  , burst [index]
burst.sort()
total = min 
if ( total > 0 ):
	print " 0 ----------" , total, " Idle " 

for i in range (0,n):
	index= process.get(burst[i])[1]
	total = total+ burst[i]
	print min , " ____________________ " , total , "P " , index
	min = total











		




	
