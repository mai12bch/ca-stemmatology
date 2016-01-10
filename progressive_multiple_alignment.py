import time 


#seq11 = ['Ich','bin','ein','Berliner', 'She', 'is', 'there', 'I', 'Berliner']
#seq21 = ['Ich','sind','Berliner','there', 'I']

seq11 = ['Whilom', 'ther', 'was', 'dwelling'] 
seq21 = ['Whilom', 'ther', 'dwellid']


# Function generating n-grams
# input: string 
# n - number of n-grams

def ngrams(input, n):

	input = list(input)
	output = []
#	[input[i:i+n] for i in range]
#	for i in range(len(input)- n+1):
#		output.append(input[i:i+n])
#	print(output)
	output = list(zip(*[input[i:] for i in range(n)]))
	return [''.join(x) for x in output]
	#return [''.join(x) for x in output]

#print(ngrams(seq11[0],2))

#print("----------------")
#time.sleep(100)
# input - string sequence 
# adding "*" before and after the words 
# generating bigrams 

def list_to_bigrams(seq): 

#	some_list = []
	s = "*" + str(seq) + "*"
	kl = "*"
#	s =  '{}{}{}'.format(kl,seq,kl)  

#	for i in range(len(seq)): 
#		value = '*'+seq[i]+'*' 
#		value = "%(*)sseq[i]%(*)%s" 
#		some_list.append(ngrams(value,2))
#	print("List to bigrams function")
#	print(some_list, seq)
#	time.sleep(10)

	some_list = ngrams(s,2)

	return (some_list)


# function D2 -> according to the paper of Howe and Spencer
# D2(x,y) = |G(x) + G(y)| - 2|G(x) intersection G(y)| 
def d2(x,y): 

	sum_x_y = abs(len(x)+len(y))
	set_x_y = sorted(list(set(x).intersection(y)))
	result = sum_x_y - 2 * len(set_x_y)
	
	return(result, sum_x_y)

# similiarity function between [-1, +1]
# if -1 words are very different 
# if +1 words are exactly the same  
# s(x,y) = 1 - 2 * (D2(x,y) / |G(x) + G(y)|) 

def sim(x,y): 

	sim_return = 0
	result, sum_x_y = d2(x,y)
	sim = 1 -2 * (result / sum_x_y)

# smooth parameters 
	if sim < -0.4:	
		sim_return = -1 
	elif sim > 0.4: 
		sim_return = 1  
	else: 
		sim_return = sim 

#	return(sim)
	return (sim_return) 

# simple similiarity function 
def sim_func(x,y): 

	if x == y: 
		j = 1 
	elif x != y: 
		j = -1
	return (j)	

#collating algorithm 
#
#cij = max{ 
#			- ci-1,j-1 + s(x,y)
#			- ci, j-1 - g 
#			- ci-1, j - g 
#			}

def needleman_wunsch(seq1, seq2, sim_func, pen):
 	

    m = len(seq1)+1 # Rows
    n = len(seq2)+1 # Columns
 
    M = create_matrix(m, n)

    for i in range(0, m):
        M[i][0] = i * pen
    for j in range(0, n):
        M[0][j] = j * pen

    for i in range(1, m):

        for j in range(1, n):
     #       match = M[i-1][j-1] + sim_func(seq1[i-1], seq2[j-1])
            match = M[i-1][j-1] + sim(list_to_bigrams(seq1[i-1]), list_to_bigrams(seq2[j-1]))
            delete = M[i-1][j] + pen
            insert = M[i][j-1] + pen
            M[i][j] = max(match, delete, insert)

    return M

# Create an empty matrix
def create_matrix(m, n):
    return [[0]*n for _ in range(m)]


# Or gap 
#pen = -3  

# Traceback
 
def traceback(seq1, seq2, sim_func, pen, M):
	
	sim = sim_func
	AlignmentA = []
	AlignmentB = []
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

	        if (Score == ScoreDiag + sim(list_to_bigrams(seq1[i-1]), list_to_bigrams(seq2[j-1]))):
#	        if (Score == ScoreDiag + sim_func(seq1[i-1], seq2[j-1])):

	        	AlignmentA.append(seq1[i-1])
	        	AlignmentB.append(seq2[j-1])

	#        	AlignmentA = seq1[i] + AlignmentA
	#       	AlignmentB = seq2[j] + AlignmentB

	        	i -= 1
	        	j -= 1


	        elif (Score == ScoreLeft + d):

	        	AlignmentA.append(seq1[i-1])
	        	AlignmentB.append("-")
	        	i -= 1
#	            AlignmentA = seq1[i] + AlignmentA
#	            AlignmentB = "-" + AlignmentB

	        elif (Score == ScoreUp + d):

	        	AlignmentA.append("-")
	        	AlignmentB.append(seq2[j-1])
	        	j -= 1
#	            AlignmentB = seq2[j] + AlignmentB
#	            AlignmentA = "-" + AlignmentA

	        else:
	                print("algorithm error?")

	while (i > 0):

			AlignmentA.append(seq1[i-1])
			AlignmentB.append("-")
			i -= 1
#	        AlignmentA = seq1[i] + AlignmentA
#	        AlignmentB = "-" + AlignmentB

	while (j > 0):

			AlignmentA.append("-")
			AlignmentB.append(seq2[j-1])
			j -= 1
#	        AlignmentA = "-" + AlignmentA
#	        AlignmentB = seq2[j] + AlignmentB

	
	return(AlignmentA,AlignmentB)


def alignment(listA, listB):


	seq1 = listA
	seq2 = listB

	pen = -1  

	M = needleman_wunsch(seq1,seq2, sim_func, pen)

	#print(M)
	AlignmentA, AlignmentB = traceback(seq1,seq2,sim,pen,M)
	
	AlignmentA = list(reversed(AlignmentA))
	AlignmentB = list(reversed(AlignmentB))

		
	return(AlignmentA, AlignmentB)


def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)



def Hx(AlignmentA, AlignmentB): 

	perfect_match = sorted(list(set(AlignmentA).intersection(AlignmentB)))
	len_perfect_match = len(perfect_match)

	col_without_gaps = 0  

	for i in range(len(AlignmentA)):

		if AlignmentA[i] != '-' and AlignmentB[i] != '-': 
			col_without_gaps +=1 

	return -ln(len_perfect_match/col_without_gaps)

################################################### 



def create_hw_matrix(matrix,name): 



 hw_matrix = [ [] for x in range(len(matrix))] 

 for i in range(len(matrix)): 

    hw_matrix[i].append(0)  #diagonal - 0   
    for j in range(i+1,len(matrix)):
        print(i,j)
        AlignmentA,AlignmentB = alignment(matrix[i],matrix[j])

        # Hx similiarity measure (Hxy = -ln (#perfect match/#columns without gaps))
        wert = Hx(AlignmentA,AlignmentB)
        hw_matrix[i].append(round(wert,2))
        hw_matrix[j].insert(i,round(wert,2))

 save_hw(hw_matrix, name)





'''
AlignmentA, AlignmentB = alignment(seq11,seq21)
print(AlignmentA)
print(AlignmentB)
print(Hx(AlignmentA,AlignmentB))
'''