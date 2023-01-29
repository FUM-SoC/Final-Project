def fcfs(pd):
	
	avgwait, avgturntime = 0,0
	waitingtime, turntime,wallclock = {},{},[]
	readyqueue = [[v[0],k] for k,v in pd.items()]
	readyqueue.sort()
		#sorted by arrival time # [...,[arrival time,'proc name'] ,...]
	timer = readyqueue[0][0] # starting the clock from 0 or the first arrival time
	wallclock.append([timer])
	for i in readyqueue: # [[3,'1'],[9,'2']]
		timer += pd[i[1]][1] # burst time 

		turntime[i[1]] = timer - i[0]
		waitingtime[i[1]] = turntime[i[1]] - pd[i[1]][1]
		wallclock.append([i[1], timer])

		avgwait+= waitingtime[i[1]]
		avgturntime+= turntime[i[1]]
		# print("proc.name",i,"\n",)

	avgwait = avgwait/len(pd)
	avgturntime = avgturntime/len(pd)
	#print(waitingtime,turntime)


	combinedwaitturndict = {k:[waitingtime[k],turntime[k]] for k in waitingtime.keys()}
	return combinedwaitturndict, wallclock,avgwait,avgturntime

if __name__=='__main__':
	pd = {'1': [0, 5], '2': [3, 9], '3': [6, 6]} 
			#{'process name': [arrival time, burst time]}

	fcfs(pd)
