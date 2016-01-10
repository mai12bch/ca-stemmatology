import time 

import progressive_multiple_alignment as pma 

#seq11 = ['Ich','bin','ein','Berliner', 'She', 'is', 'there', 'I', 'Berliner']
#seq21 = ['Ich','sind','Berliner','there', 'I']

s_1 = ['Whilom', 'ther', 'was', 'dwelling','something','-','-','AMEN'] 
s_2 = ['Whilom', 'ther', '-','dwellid','something','-','-','amen']
s_3 = ['Whilom', '-', 'was','dwellid','something','-','-','AMEN'] 

k_1 = ['Whilom', 'ther','was1', 'dwellddd', 'tehtänöhön']
k_2 = ['Whilom', '-', 'was', 'dwelling','tehtänöhön.'] 


# Create an empty matrix

def create_matrix(m, n):
    return [[0]*n for _ in range(m)]

def ngrams(input, n):

	input = list(input)
	output = []
	output = list(zip(*[input[i:] for i in range(n)]))
	return [''.join(x) for x in output]

def list_to_bigrams(seq): 

	s = "*" + str(seq) + "*"
	kl = "*"

	some_list = ngrams(s,2)

	return (some_list)


def d2(x,y): 

	sum_x_y = abs(len(x)+len(y))
	set_x_y = sorted(list(set(x).intersection(y)))
	result = sum_x_y - 2 * len(set_x_y)
	
	return(result, sum_x_y)

def sim_modified(a,b,i,j):

	list_a = a 
	list_b = b
	#print(i)  
	i = i-1 
	j = j-1

	#check if the a or b are lists 
	check_a = any( isinstance(e, list) for e in list_a)
	check_b = any( isinstance(e, list) for e in list_b)
	
#	print(len(list_b))
	#first case when both include lists 
	if check_a == True and check_b == True:  
		#print("True")

		sum_of = 0
		for k in range(len(list_a)): # sum over first pair 

			for l in range(len(list_b)): #sum over second pair 

				if list_a[k][i] == "-" or list_b[l][j] == "-":

					sum_of +=  0

				else:

#					sum_of += sim(list_to_bigrams(list_a[k][i]), list_to_bigrams(list_b[l][j]))		
					sim_val = sim(list_to_bigrams(list_a[k][i]), list_to_bigrams(list_b[l][j]))		
					# smooth the parameters
					if sim_val < -0.4:	
						sum_of += -1 
					elif sim_val > 0.4: 
						sum_of += 1  
					else: 
						sum_of += sim_val 

		return(sum_of) #/ (len(list_a) * len(list_b)))


	#list_a contains list and list_b does not	
	elif check_a == True and check_b == False: 

		sum_of = 0
		for k in range(len(list_a)): # sum over first pair 
				
				if list_a[k][i] == "-" or list_b[j] == "-":

					sum_of +=  0

				else:

					sim_val = sim(list_to_bigrams(list_a[k][i]), list_to_bigrams(list_b[j]))		

					if sim_val < -0.4:	
						sum_of += -1 
					elif k > 0.4: 
						sim_val += 1  
					else: 
						sim_val += k 
				
		return(sum_of) # / (len(list_a) + 1))

#		return(float("{0:.2f}".format(sum_of / (len(list_a) * 1))))

	elif check_a == False and check_b == True: 

		sum_of = 0

		for k in range(len(list_b)): # sum over first pair q
				
				if list_b[k][j] == "-" or list_a[i] == "-":

					sum_of +=  0

				else:

#					sum_of += sim(list_to_bigrams(list_a[i]),list_to_bigrams(list_b[k][j]))		
					k = sim(list_to_bigrams(list_a[i]),list_to_bigrams(list_b[k][j]))		

					if k < -0.4:	
						sum_of += -1 
					elif k > 0.4: 
						sum_of += 1  
					else: 
						sum_of += k 

		return (sum_of)			
		#return(float("{0:.2f}".format(sum_of / (len(list_a) * 1))))



def sim(x,y): 


	result, sum_x_y = d2(x,y)
	sim = 1 - 2 * (result / sum_x_y)

	return(sim)

#print(sim(list_to_bigrams('Caswoi'),list_to_bigrams('caswoi')))

# simple similiarity function 
'''
def sim_func(x,y): 

	if x == y: 
		j = 1 
	elif x != y: 
		j = -1
	return (j)	
'''

# i ist list_a
def gap_i(seq1,seq2,i,j):

	i=i-1
	j=j-1
	list_a = seq1
	list_b = seq2 

	for k in range(len(list_a)): # sum over first pair 
		if list_a[k][i] == "-":
			result = 0
		else: 
			result = -1
			
#		print(k,list_a[k][i],result)

#	time.sleep(10)
	return(result)


# j over list_b
def gap_j(seq1,seq2,i,j):

	i=i-1
	j=j-1

	list_a = seq1
	list_b = seq2 

	# list or not neccessary !!! 
	# now a faster method to implement 

#	print(len(list_b))
#	for l in range(len(list_b)): # sum over first pair 

	if list_b[j] == "-":
		return (0)
	else: 
		return(-1)
#		if list_b[l][j] == "-": 
			
#			return(0)
#		else: 
#			return(-1)

def needleman_wunsch_modified(seq1, seq2, sim_modified, pen):
    
    check_a = any( isinstance(e, list) for e in seq1)
    check_b = any( isinstance(e, list) for e in seq2)
    
    m = 0 
    n = 0
#    print(check_a,check_b)

    if check_a == True and check_b == False:

	    m = len(seq1[0])+1 # Rows
	    n = len(seq2)+1 # Columns

    elif check_a == False and check_b == True:

        m = len(seq1)   +1   #Rows 
        n = len(seq2[0])+1 #Columns
        

    elif check_a == True and check_b == True: 

        m = len(seq1[0]) +1 #Rows  
        n = len(seq2[0]) +1 #Columns 
 #   m = m 
 #   n = n
#    print(m,n)


    M = create_matrix(m, n)

    for i in range(0, m):
        M[i][0] = i * pen
    for j in range(0, n):
        M[0][j] = j * pen

    for i in range(1, m):

        for j in range(1, n):
     #       match = M[i-1][j-1] + sim_func(seq1[i-1], seq2[j-1])
            match = M[i-1][j-1] + sim_modified(seq1,seq2,i,j)
            #print(match,i-1,j-1)
            #match = float("{0:.2f}".format(match))
            delete = M[i-1][j] -1 #gap_i(seq1,seq2,i,j) 
            #delete = float("{0:.2f}".format(delete))
            insert = M[i][j-1] -1 #gap_j(seq1,seq2,i,j)
            #insert = float("{0:.2f}".format(insert))
            #if match == delete or match == insert 

            M[i][j] = max(match, delete, insert)
            #M[i][j] = float("{0:.2f}".format(max(match, delete, insert)))
    #print("I,j", i,j," Match ", match, "Delete ", delete, "Insert", insert, "Sim_modified", sim_modified(seq1,seq2,i,j))
           	
#            time.sleep(0.5)
  #          if match == delete or match == insert:  

             #print("Match ", match, "Delete ", delete, "Inserte", insert, "I,j", i,j)
             #print(seq1[0][i],seq1[1][i],seq2[j])
             
#    time.sleep(1000)
    #print("Sim_modified", sim_modified(seq1,seq2,i,j))
    #print(M[i][j])
#    time.sleep(10)
    return M


# Or gap 
#pen = -3  

# Traceback


def traceback_modified(seq1, seq2, sim_func, pen, M):

	sim = sim_func

	check_a = any( isinstance(e, list) for e in seq1)
	check_b = any( isinstance(e, list) for e in seq2)

	# seq1 is a multilist, seq2 is not  
	if check_a == True and check_b == False:

		AlignmentA = [[] for x in range(len(seq1))]
		AlignmentB = []

	# seq1 is a list, seq2 is a multilist
	elif check_a == False and check_b == True:

		AlignmentA = []
		AlignmentB = [[] for x in range(len(seq2))]

	# both lists are multilists
	elif check_a == True and check_b == True: 

		AlignmentA = [[] for x in range(len(seq1))]
		AlignmentB = [[] for x in range(len(seq2))]

#	i = len(seq1) -1 
#	j = len(seq2) -1  

	M = M

	i = len(M) - 1 
	j = len(M[0]) - 1 
	d = -1

	while (i > 0 and j > 0):

	        Score = M[i][j]

	        ScoreDiag = M[i - 1][j - 1]
	        ScoreUp = M[i][j - 1]
	        ScoreLeft = M[i - 1][j]
	        
#	        time.sleep(2)

	        if (Score == ScoreDiag + sim_modified(seq1,seq2,i,j)):


#	        	AlignmentA[0].append(seq1[0][i-1])
#	        	AlignmentA[1].append(seq1[0][i-1])
#	        	AlignmentB.append(seq2[j-1])
	        	#print("Score: ", Score, "ScoreDiag", ScoreDiag, "SimModified",sim_modified(seq1,seq2,i,j))
	        	# seq1 is a multilist, seq2 list
	        	if check_a == True and check_b == False:

	        		for n in range(len(seq1)):
	        			AlignmentA[n].append(seq1[n][i-1])
	        			#print(seq1[n][i-1],seq2[j-1])
	        		AlignmentB.append(seq2[j-1])

	        	# seq1 is a list, seq2 is a multilist	
	        	elif check_a == False and check_b == True:

	        		AlignmentA.append(seq1[i-1])
	        		for n in range(len(seq2)):
	        			AlignmentB[n].append(seq2[n][j-1]) 
				# both lists are multilists
	        	elif check_a == True and check_b == True:  

	        		for n in range(len(seq1)):
	        			AlignmentA[n].append(seq1[n][i-1])
	        		for n in range(len(seq2)):
	        			AlignmentB[n].append(seq2[n][j-1]) 
	        			
	        	i -= 1
	        	j -= 1
#	        	time.sleep(10)

	        elif (Score == ScoreLeft +d ): #gap_i(seq1,seq2,i,j)):

#	        	AlignmentA[0].append(seq1[0][i-1])
#	        	AlignmentA[1].append(seq1[1][i-1])
#	        	AlignmentB.append("-")

	        	# seq1 is a multilist, seq2 list
	        	if check_a == True and check_b == False:

	        		for n in range(len(seq1)):
	        			AlignmentA[n].append(seq1[n][i-1])
	        		AlignmentB.append("-")					        		
	        	
	        	# seq1 is a list, seq2 is a multilist	
	        	elif check_a == False and check_b == True: 

	        		AlignmentA.append(seq1[i-1])
	        		for n in range(len(seq2)):
	        			AlignmentB[n].append("-")

	        	# both lists are multilists		
	        	elif check_a == True and check_b == True:  

	        		for n in range(len(seq1)):
	        			AlignmentA[n].append(seq1[n][i-1])
	        		for n in range(len(seq2)):
	        			AlignmentB[n].append("-") 

	        	i -= 1

	        elif (Score == ScoreUp +d ): #gap_j(seq1,seq2,i,j)):

#	        	AlignmentA[0].append("-")
#	        	AlignmentA[1].append("-")
#	        	AlignmentB.append(seq2[j-1])

	        	# seq1 is a multilist, seq2 list
	        	if check_a == True and check_b == False:

	        		for n in range(len(seq1)):
	        			AlignmentA[n].append("-")
	        		AlignmentB.append(seq2[j-1])					        		
	      
	        	# seq1 is a list, seq2 is a multilist	
	        	elif check_a == False and check_b == True: 

	        		AlignmentA.append("-")
	        		for n in range(len(seq2)):
	        			AlignmentB[n].append(seq2[n][j-1])

	        	
	        	# both lists are multilists	
	        	elif check_a == True and check_b == True:  

	        		for n in range(len(seq1)):
	        			AlignmentA[n].append("-")
	        		for n in range(len(seq2)):
	        			AlignmentB[n].append(seq2[n][j-1]) 

	        	j -= 1

	        else:
	                print("algorithm error?")

	while (i > 0):
			
			#AlignmentA[0].append(seq1[0][i-1])
			#AlignmentA[1].append(seq1[1][i-1])
			#AlignmentB.append("-")

	        # seq1 is a multilist, seq2 list
	        if check_a == True and check_b == False:

	        	for n in range(len(seq1)):
	        		AlignmentA[n].append(seq1[n][i-1])
	        	AlignmentB.append("-")					        		
	        	
	        	# seq1 is a list, seq2 is a multilist	
	        elif check_a == False and check_b == True: 

	        	AlignmentA.append(seq1[i-1])
	        	for n in range(len(seq2)):
	        		AlignmentB[n].append("-")

	        # both lists are multilists		
	        elif check_a == True and check_b == True:  

	        	for n in range(len(seq1)):
	        		AlignmentA[n].append(seq1[n][i-1])
	        	for n in range(len(seq2)):
	        		AlignmentB[n].append("-") 
	        i -= 1

	while (j > 0):
			
	        # seq1 is a multilist, seq2 list
	        if check_a == True and check_b == False:

	        	for n in range(len(seq1)):
	        		AlignmentA[n].append("-")
	        	AlignmentB.append(seq2[j-1])					        		
	      
	        # seq1 is a list, seq2 is a multilist	
	        elif check_a == False and check_b == True: 

	        	AlignmentA.append("-")
	        	for n in range(len(seq2)):
	        		AlignmentB[n].append(seq2[n][j-1])

	        	
	        # both lists are multilists	
	        elif check_a == True and check_b == True:  

	        	for n in range(len(seq1)):
	        		AlignmentA[n].append("-")
	        	for n in range(len(seq2)):
	        		AlignmentB[n].append(seq2[n][j-1]) 
	        j -= 1		

			#AlignmentA[0].append("-")
			#AlignmentA[1].append("-")
			#AlignmentB.append(seq2[j-1])


	return(AlignmentA,AlignmentB)


import csv 

def alignment(listA, listB):


	seq1 = listA
	seq2 = listB

	pen = -1

	# Needleman-Wunsch Algorithm
	M = needleman_wunsch_modified(seq1,seq2, sim_modified, pen)

	
	with open("matrix_M.csv", "w") as write_file: 

	    writer = csv.writer(write_file , delimiter = "\t", escapechar= ' ', quoting = csv.QUOTE_NONE)

	    writer.writerows(M)    

	#Traceback Method 
	AlignmentA, AlignmentB = traceback_modified(seq1,seq2,sim,pen,M)

	check_a = any( isinstance(e, list) for e in AlignmentA)
	check_b = any( isinstance(e, list) for e in AlignmentB)


	# seq1 is a multilist, seq2 is not  
	if check_a == True and check_b == False:

		for i in range(len(AlignmentA)):

			AlignmentA[i] = list(reversed(AlignmentA[i]))
		AlignmentB = list(reversed(AlignmentB))

	# seq1 is a list, seq2 is a multilist
	elif check_a == False and check_b == True:

		AlignmentA = list(reversed(AlignmentA))
		for i in range(len(AlignmentB)):
			AlignmentB[i] = list(reversed(AlignmentB[i]))

	# both lists are multilists
	elif check_a == True and check_b == True: 

		for i in range(len(AlignmentA)):
			AlignmentA[i] = list(reversed(AlignmentA[i]))
		for i in range(len(AlignmentB)):
			AlignmentB[i] = list(reversed(AlignmentB[i]))


		
	return(AlignmentA, AlignmentB)

###################################################
################################################### 




list_test01 = []
#sequences s_1,s_2,s_3 ;  k_1,k_2
'''

list_a = [s_1,s_2,s_3]
list_b = [k_1,k_2]

####### modified function ############## 

#print(list_a)
#print(list_b)


from collections import defaultdict 

d = defaultdict(list)

AlignmentA, AlignmentB = alignment(list_a,list_b)

#print(len(AlignmentB))
#d[0].append(AlignmentA)
#d[0].append(AlignmentB[0])
#d[0].append(AlignmentB[1])
#print(len(d[0]))

for i in range(len(AlignmentA)): 

	print(AlignmentA[i])

for i in range(len(AlignmentB)): 

	print(AlignmentB[i])

#for i in range(len(d[0])): 

#	print(d[0][i])

name = 'test_dictionary'

with open("{}".format(name) + '.txt', "w") as write_file: 
       
    for l in range(len(d[0])): 

        write_file.writelines("{}".format(d[0][l])  +"\n")


'''