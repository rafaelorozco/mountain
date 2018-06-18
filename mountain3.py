from matplotlib import pyplot as plt
import numpy as np
import time
import copy

allTasks = ["nopp","medhof","cold","posture","ideas"]

### read in data format:
### each line is a day with a list of completed tasks

def readIn():
	fileT = open("realfile.txt","r")
 	
	fileLines = fileT.readlines()

	dataDict = {}
	dataDictBin = {}

	#initialize habit data structures
	for task in allTasks:
		dataDict[task] = [0]
		#dataDictBin[task] = [0]

	#iterateover lines in file
	for line in fileLines:
		currLine = line.split()

		allTasksTemp = copy.deepcopy(allTasks)

		#iterate over tasks completed in that day
		for taskIndex in xrange(1,len(currLine)):
			taskName = currLine[taskIndex]

			previousValue = dataDict[taskName][-1]
			dataDict[taskName].append(previousValue+1)
			#print taskName
			#print allTasksTemp
			allTasksTemp.remove(taskName)
			print dataDict

		#iterate over tasks that were NOT complete that day
		for taskIndex in xrange(0,len(allTasksTemp)):
			taskName = allTasksTemp[taskIndex]

			previousValue = dataDict[taskName][-1]
			dataDict[taskName].append(max(previousValue-1,0))











		#for taskKey in dataDict:
			#initialize habit quantities
			#dataDict[taskKey].append(0)
			#dataDictBin[taskKey].append(0)

			#if(len(dataDict[taskKey]) > 0):
				#dataDict[taskKey][-1] = dataDict[taskKey][-2]

				#if task was not completed then decrease that habit number by one
				#if(dataDictBin[taskKey][-2] == 0):
					#dataDict[taskKey][-1] = max(dataDict[taskKey][-1] - 1,0)

		#iterate over tasks completed in that day
		#for taskIndex in xrange(1,len(currLine)):
			#taskKey = currLine[taskIndex]
		
			#set habit as completed for that day
			#dataDictBin[taskKey][-1] = 1

			#if(len(dataDict[taskKey]) > 1):
				#if task was completed then increase that habit number by one
				#if(dataDictBin[taskKey][-2] == 1):
					#dataDict[taskKey][-1] += 1 
			#else:
				#dataDict[taskKey][-1] = 1

	fileT.close()
	return dataDict 

def get_cmap(n, name='ocean'):
    '''Returns a function that maps each index in 0, 1, ..., n-1 to a distinct 
    RGB color; the keyword argument name must be a standard mpl colormap name.'''
    return plt.cm.get_cmap(name, n)


def displayData():

	dataDict = readIn()

	displayData = []
	names = []
	colors = ['#dd6e42','#e8dab2', '#4f6d7a', '#c0d6df' , '#eaeaea']

	for key in dataDict:
		names.append(key)
		displayData.append(dataDict[key][1:])


	fig = plt.figure(figsize=(15,10))
	bottomData = np.array([0 for i in displayData[0]])

	N = len(displayData)
	cmap = get_cmap(N)
	for dataIndex in xrange(N):
		currData = displayData[dataIndex]
		currColor = colors[dataIndex]
		currName = names[dataIndex]
		
		plt.bar(range(len(currData)), currData, bottom=bottomData ,label=currName,color=cmap(dataIndex),alpha=0.9,width = 1)
		bottomData += np.array(currData)

	#fig.tight_layout(pad=0.5) 
	plt.xticks([i + 0.5 for i in range(len(displayData[0]))], range(len(displayData[0])))
	plt.legend(bbox_to_anchor=(1, 1), loc=2 ,borderaxespad=0)
	plt.show()

def endOfDay():
	#add accomplished tasks (comment out if not accomplished):
	accomTasks = []
	accomTasks.append("nopp")
	#accomTasks.append("medhof")
	#accomTasks.append("cold")
	#accomTasks.append("posture")
	#accomTasks.append("ideas")

	fileT = open("realfile.txt","a")
	fileT.write("\n"+ time.strftime("%d/%m/%Y") + " ")

	for task in accomTasks:
		fileT.write(task + " ") 

	fileT.close() 

	#displayData()

#displayData()
endOfDay()

#The reason why I dont listen to music is the same reason for which
#I waited to put the salsa on the sabritas. I wait for the greater pleasure. 


#todo:

#
# set up order by newnest (probability that it will be accomplished) point is that 
# the stronger ones are the base of the mountain

#Make shade color correspond to type of habit. Mental physical. carrer

#change y axis to make squares

#separate each habit block into units. 

#make mountain decrease not disapear. ##done

#automatically add zero at end of day






