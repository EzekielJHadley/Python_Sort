# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14
Last update Fri Aug 15
@author: Thamor999
"""

###########################################
#this will utilize the Quick Sort algorithm
def quicksort(unsorted):
	size = len(unsorted)
	pivot = unsorted[-1]
	#print pivot
	mark = 0
	
	#now I want all the values < pivot to be to the left of pivot
	for i in range(size-1, -1, -1): #to -1 because ranges goes [begin, end)
		while (unsorted[i-1] != None) and (unsorted[i-1] < pivot) and mark != i:
			swap = unsorted[i-1]
			unsorted[i-1] = unsorted[mark]
			unsorted[mark] = swap
			mark += 1
			#print unsorted, mark
		
		#leave when the pivot is as far left as it can go
		if mark == i:
			break
		else:
			unsorted[i] = unsorted[i-1]
			unsorted[i-1] = pivot
	
	#now to recurs
	#check the left side
	if len(unsorted[0:mark]) > 1:
		unsorted[0:mark] = quicksort(unsorted[0:mark])
	#check the right side
	if len(unsorted[(mark+1):]) > 1:
		unsorted[(mark+1):] = quicksort(unsorted[(mark+1):])
		
	return unsorted

##############################################
#this will utilize the Merge Sort algorithm
#it uses the top-down implementation
def mergesort(unsorted):
	size = len(unsorted)
	sorted = unsorted[:] #initialize a sorted array, without making a reference
	split(unsorted, 0, size, sorted)
	return unsorted

#[begin, end), start splitting the list to later be merged
def split(unsorted, begin, end, sorted):
	midpoint = int((end + begin)/2)
	#print "working on these splits: ", begin, midpoint, end
	if (end - begin) == 1: #check if the size is 1, thus sorted
		return
	
	#if not divide more!
	split(unsorted, begin, midpoint, sorted)	#first half
	split(unsorted, midpoint, end, sorted)		#second half
	#print begin, midpoint, end
	
	#now sort and merge
	merge(unsorted, begin, midpoint, end, sorted)
	#now just copy the more sorted list back over
	unsorted[begin:end] = sorted[begin:end]
	#print "We no have: ", unsorted

#here I will merge the left and right portions of the list
def merge(unsorted, begin, middle, end, sorted):
	lMark = begin
	rMark = middle
	#now go through each element of Left and Right
	#put them in order
	#print "Begin merging: ", unsorted[begin:middle], "with", unsorted[middle:end]
	#print "of points: ", begin, middle, end
	for i in range(begin, end):
		if (lMark < middle) and (rMark >= end or unsorted[lMark] <= unsorted[rMark]):
			#print "location", i, "is now", unsorted[lMark]
			sorted[i] = unsorted[lMark]
			lMark += 1
		else:
			#print "location", i, "is now", unsorted[rMark]
			sorted[i] = unsorted[rMark]
			rMark += 1
	#print sorted[begin:end]

##############################################
#This will utilize the Heap Sort algorithm
def heapsort(unsorted):
	size = len(unsorted)
	sorted = []
	while len(sorted) < size:
		createHeap(unsorted)
		sorted.append(unsorted.pop(0))
	return sorted
	
		

#this function will create a heap out of a list
#it will use the list to store the heap
#using the findChildren, findParent functions to traverse it
def createHeap(unheaped):
	size = len(unheaped)
	for i in range(size-1, -1, -1):	#start at the end and go to the begining [size-1, 0]
		parent = findParent(i)
		#print size, i, parent
		if unheaped[i] > unheaped[parent]:
			swap = unheaped[i]
			unheaped[i] = unheaped[parent]
			unheaped[parent] = swap
			#every time a swap is made make sure it all sifts down
			#i can be more clever in the futur though
			createHeap(unheaped)

#find the index of the either, or both, children for a given parent
def findChildren(parentIndex, which = 0):
	if which == 1:		#first child
		return (2*parentIndex + 1)
	elif which == 2:	#second child
		return (2*parentIndex + 2)
	else:				#both children
		return [(2*parentIndex + 1), (2*parentIndex + 2)]

#find the index of the parent for a given child
def findParent(childIndex):
	if childIndex != 0:
		return (childIndex - 1)//2	#floor division
	else:
		return 0




values = [345, 168, 785, 124, 693, 234, 201, 034, 000, 953, 023, 978, 555, 364, 784]
print values, "\n"
sorted = heapsort(values)
print sorted