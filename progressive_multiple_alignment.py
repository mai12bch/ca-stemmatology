import time 


seq1 = ['Ich','bin','ein','Berliner', 'She', 'is', 'there', 'I', 'Berliner']
seq2 = ['Ich','sind','Berliner','there', 'I']

#seq1 = ['Whilom', 'ther', 'was', 'dwelling'] 
#seq2 = ['Whilom', 'ther', 'dwellid']


def ngrams(input, n):

	input = list(input)
	output = []
	for i in range(len(input)- n+1):
		output.append(input[i:i+n])
	return [''.join(x) for x in output]

def list_to_bigrams(seq): 

	some_list = []  
	for i in range(len(seq)): 
		value = '*'+seq[i]+'*'
		some_list.append(ngrams(value,2))

	return (some_list)


# D2(x,y) = |G(x) + G(y)| - 2|G(x) intersection G(y)| 
def d2(x,y): 

	sum_x_y = abs(len(x)+len(y))
	set_x_y = sorted(list(set(x).intersection(y)))
	result = sum_x_y - 2 * len(set_x_y)
	return(result, sum_x_y)

# s(x,y) = 1 - 2 * (D2(x,y) / |G(x) + G(y)|) 
def sim(x,y): 

	result, sum_x_y = d2(x,y)
	sim = 1 -2 * (result / sum_x_y)
	return(sim)

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
#            match = M[i-1][j-1] + sim_func(seq1[i-1], seq2[j-1])
            match = M[i-1][j-1] + sim(list_to_bigrams(seq1)[i-1], list_to_bigrams(seq2)[j-1])
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
	
	AlignmentA = []
	AlignmentB = []
	i = len(seq1) -1 
	j = len(seq2) -1  
	d = pen
	M = M

	while (i > 0 and j > 0):

	        Score = M[i][j]
	        ScoreDiag = M[i - 1][j - 1]
	        ScoreUp = M[i][j - 1]
	        ScoreLeft = M[i - 1][j]
	        
	        if (Score == ScoreDiag + sim(list_to_bigrams(seq1)[i-1], list_to_bigrams(seq2)[j-1])):

	#        	AlignmentA = seq1[i] + AlignmentA
	        	AlignmentA.append(seq1[i])
	        	AlignmentB.append(seq2[j])
	 #       	AlignmentB = seq2[j] + AlignmentB
	        	i -= 1
	        	j -= 1

	        elif (Score == ScoreLeft + d):

	        	AlignmentA.append(seq1[i])
	        	AlignmentB.append("-")
	        	i -= 1
#	                AlignmentA = seq1[i] + AlignmentA
#	                AlignmentB = "-" + AlignmentB

	        elif (Score == ScoreUp + d):

	        	AlignmentA.append("-")
	        	AlignmentB.append(seq2[j])
	        	j -= 1
#	                AlignmentB = seq2[j] + AlignmentB
#	                AlignmentA = "-" + AlignmentA

	        else:
	                print("algorithm error?")

	while (i > 0):

			AlignmentA.append(seq1[i])
			AlignmentB.append("-")
			i -= 1
#	        AlignmentA = seq1[i] + AlignmentA
#	        AlignmentB = "-" + AlignmentB

	while (j > 0):

			AlignmentA.append("-")
			AlignmentB.append(seq2[j])
			j -= 1
#	        AlignmentA = "-" + AlignmentA
#	        AlignmentB = seq2[j] + AlignmentB

	
	return(AlignmentA,AlignmentB)

print("------------------")

def alignment(listA, listB):


	seq1 = listA
	seq2 = listB

	seq1.insert(0,'')
	seq2.insert(0,'')

	pen = -1  

	M = needleman_wunsch(seq1,seq2, sim_func, pen)

	print(M)
	AlignmentA, AlignmentB = traceback(seq1,seq2,sim_func,pen,M)
	
	AlignmentA = list(reversed(AlignmentA))
	AlignmentB = list(reversed(AlignmentB))

		
	return(AlignmentA, AlignmentB)


AlignmentA, AlignmentB = alignment(seq1,seq2)

print(AlignmentA)
print(AlignmentB)
