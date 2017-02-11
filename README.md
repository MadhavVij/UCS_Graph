# UCS_Graph
Graph Search using- Uniform Cost Search (Using input file)
Programming Lang: Python 3.6 (for python 2.4 un-comment the PriorityQueue defination and change print() syntax) 

*********

-----INSTRUCTIONS-----
## Download find_route.py (an example graph is present in input.txt)
## open terminal
## Navigate to the directory
## Enter a command in following manner:
	>>	python find_route.py <Input_File_Name> <Start_City> <Destination_City>
##An Example:
	>>   	 python find_route.py input1.txt Bremen Frankfurt

*********



*********
CODE_STRUCTURE

File: find_route.py
# required imports
# A class managing priority Queue

#Main function handles all the operations by calling specific functions
#Main function accepts all the arguments passed and stores them in variables
#Main Function calls create_graph()
##		create_graph() generates a graph from input_file of the form:
##			>>		{Karlsruhe': [('Saarbruecken', '143'), ('Stuttgart', '71')], 'Saarbruecken': [('Dortmund', '350'),          					 ('Frankfurt', '177'), ('Karlsruhe', '143')], 'Duesseldorf': [('Dortmund', '69')], ....}
#Main Function Then Class the uniformed_cost_search() which return a path and total cost as a list
##		uniformed_cost_search() stores value in visited set() which maintains all the visited nodes in it
##		uniformed_cost_search() also maintains all the neighbors from visited nodes in a PriorityQueue
##		As PriorityQueue is already sorted on element[0] which is cost, it will always have node with lowest cost for expansion
##		uniformed_cost_search() returns path (if found) as:
##		a list with total_cost appended at the end. Eg: ['Bremen', 'Dortmund', 'Frankfurt', 455]
#Main function then calls the display_path() to display the result in the correct in proper format
*********


Please Note, You have to be within the directory where the code is.
