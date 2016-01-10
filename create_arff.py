import os 
import csv 
import time 

def arff(path_input, matrix,files, name_output): 

#	with open("/home/assen/Development/stemmatology/Python_Script/guide_tree_row_alignment_35.txt") as f: 
	with open("{}".format(path_input)) as f: 

	    reader = csv.reader(f, delimiter=",")

	    list_full_alignment = [] 
	    for row in reader:
	        list_full_alignment.append(row)

	        # filtered_list -> list withoutout gaps
	filtered_list = [[] for i in range(len(list_full_alignment))]

	for i in range(len(list_full_alignment)):

	    for j in range(len(list_full_alignment[i])):

	        if list_full_alignment[i][j] != "-":
	                     
	            filtered_list[i].append(list_full_alignment[i][j])

	        # get a list_indexes 
	list_indexes = [] 
	for i in range(len(filtered_list)):
	    for j in range(len(matrix)): 
	        if len(filtered_list[i]) == len(matrix[j]): 
	            if set(filtered_list[i]) == set(matrix[j]):
	                list_indexes.append(((files[j],i)))
	                #print(i, len(filtered_list[i]),files[j], len(matrix[j]))

	#list_indexes = sorted(list_indexes)

	#generate classes list  
	class_list = []
	for i in range(len(list_indexes)): 

	    class_list.append(list_indexes[i][0])

	class_list = sorted(class_list)

	# last column add classes 
	for i in range(len(list_full_alignment)):

	    list_full_alignment[i].append(list_indexes[i][0])

	# The name of the arff file and the relation in the arff file 

	name_output = name_output    

	with open("{}.arff".format(name_output), "w") as f: 


	    f.write('@relation {} \n\n'.format(name_output))

	    for i in range(len(list_full_alignment[0])-1): 

	        column_list = []
	        for j in range(len(list_full_alignment)): 

	             column_list.append(list_full_alignment[j][i])

	        #column_list = [w.replace('-', '?') for w in column_list]     
	        column_list = sorted(set(column_list))

	        f.write("@attribute 'column{}' {}{}{} \n".format(i,'{',", ".join("'{}'".format(e) for e in column_list),'}'))


	    f.write("@attribute 'class' {}{}{} \n".format('{',", ".join("'{}'".format(e) for e in class_list),'}'))
	    f.write("\n\n")
	    f.write("@data")
	    f.write("\n")
	    writer = csv.writer(f)

	    #change - with ? 
	    list_full = [ [] for x in range(len(list_full_alignment))] 
	    '''
	    for i in range(len(list_full_alignment)):

	        for j in range(len(list_full_alignment[i])):

	            if list_full_alignment[i][j] == "-": 
	                list_full[i].append('?')
	            else:
	                list_full[i].append(list_full_alignment[i][j])
	    '''
	    for i in range(len(list_full_alignment)):

	        f.write("{}".format(", ".join( "'{}'".format(e) for e in list_full_alignment[i]))+"\n")

	    print("File {}.arff saved ".format(name_output))    


def max_parsimony(path_input, matrix,files, name_output): 

#	with open("/home/assen/Development/stemmatology/Python_Script/guide_tree_row_alignment_35.txt") as f: 
	with open("{}".format(path_input)) as f: 

	    reader = csv.reader(f, delimiter=",")

	    list_full_alignment = [] 
	    for row in reader:
	        list_full_alignment.append(row)

	        # filtered_list -> list withoutout gaps
	filtered_list = [[] for i in range(len(list_full_alignment))]

	for i in range(len(list_full_alignment)):

	    for j in range(len(list_full_alignment[i])):

	        if list_full_alignment[i][j] != "-":
	                     
	            filtered_list[i].append(list_full_alignment[i][j])

	        # get a list_indexes 
	list_indexes = [] 
	for i in range(len(filtered_list)):
	    for j in range(len(matrix)): 
	        if len(filtered_list[i]) == len(matrix[j]): 
	            if set(filtered_list[i]) == set(matrix[j]):
	                list_indexes.append(((files[j],i)))
	                #print(i, len(filtered_list[i]),files[j], len(matrix[j]))

	#list_indexes = sorted(list_indexes)

	#generate classes list  
	class_list = []
	for i in range(len(list_indexes)): 

	    class_list.append(list_indexes[i][0])

	class_list = sorted(class_list)

	# last column add classes 
	for i in range(len(list_full_alignment)):

	    list_full_alignment[i].append(list_indexes[i][0])

	# The name of the arff file and the relation in the arff file 

	name_output = name_output    

	with open("{}.arff".format(name_output), "w") as f: 


	    f.write('# Maximum parsimony for Texts \n\n')

	    f.write('{} {} \n'.format(len(list_full_alignment),len(list_full_alignment[0])-1))

	    column_list = [[] for x in range(len(list_full_alignment[0])-1)]

	    for i in range(len(list_full_alignment[0])-1): 

#	        column_list = []
	        for j in range(len(list_full_alignment)): 

	             column_list[i].append(list_full_alignment[j][i])
	             column_list[i] = sorted(set(column_list[i]))

	        print(i,len(column_list[i]),column_list[i])
	        time.sleep(2)


	    nexus_file = [ [] for x in range(len(list_full_alignment))] 

	    for k in range(len(list_full_alignment)):

	    	for j in range(len(list_full_alignment[0])-1):

		        if list_full_alignment[k][j] in column_list[j]:

		        	nexus_file[k].append(column_list[j].index(list_full_alignment[k][j]))

		        	#print(list_full_alignment[k][j], column_list[j], column_list[j].index(list_full_alignment[k][j]))

	    for i in range(len(nexus_file)): 

	    	f.write('{}'.format(list_full_alignment[i][-1]) + '\t')

	    	#print(len(nexus_file[i]))

	    	for j in range(len(nexus_file[0])):


	    		f.write('{}'.format(nexus_file[i][j]))

	    	
	    	f.write('\n')
		        #if list_full_alignment[k][j] in column_list[k]:

#		        	print(list_full_alignment[k][j])
		        #	time.sleep(2)




'''
	        f.write("@attribute 'column{}' {}{}{} \n".format(i,'{',", ".join("'{}'".format(e) for e in column_list),'}'))


	    f.write("@attribute 'class' {}{}{} \n".format('{',", ".join("'{}'".format(e) for e in class_list),'}'))
	    f.write("\n\n")
	    f.write("@data")
	    f.write("\n")
	    writer = csv.writer(f)

	    #change - with ? 
	    list_full = [ [] for x in range(len(list_full_alignment))] 

	    for i in range(len(list_full_alignment)):

	        for j in range(len(list_full_alignment[i])):

	            if list_full_alignment[i][j] == "-": 
	                list_full[i].append('?')
	            else:
	                list_full[i].append(list_full_alignment[i][j])
	    
	    for i in range(len(list_full_alignment)):

	        f.write("{}".format(", ".join( "'{}'".format(e) for e in list_full_alignment[i]))+"\n")

	    print("File {}.arff saved ".format(name_output))    
'''