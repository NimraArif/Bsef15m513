#!user/bin/python

process={}
burst_time=[]
arrival_time=[]
ready_queue=[]
ts = 0
wait=0
turn_around=0
x=0

def input( ts ):
	ts = input ("Enter time slice for process:")
	
	n=input ( "Enter total number of processes: ")
	for i in range (0,n): 
		arrival= input(" enter arrival time ")
	
		arrival_time.append(arrival)
		burst = input(" enter burst time ")
		burst_time.append(burst)
		process[i+1] = [burst_time[i]]

def sorting(arrival_time , burst_time):
	for i in range (0,n):
		for j in range (0,n):
			if ( arrival_time[i] < arrival_time[j]):
				temp = arrival_time[i]
				arrival_time[i]=arrival_time[j]
				arrival_time[j]=temp
				burst_time[i] = burst_time[j]
				burst_time[j]=temp2

input(ts)
sorting(arrival_time , burst_time)
print ( " process time and burst time : " )
for i in range (0,n):
	while ( arrival_time[x] < wait):
		ready_queue.append(burst_time[x])
		x=x+1
	print i , " Arrival time : ", arrival_time[i] , wait
	wait += turn_arround 
	ready_queue[i] -=ts


