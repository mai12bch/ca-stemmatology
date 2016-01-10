import numpy as np 
import time 

distances = [] 

'''# Test Example 
taxaList = ['Mensch', 'Maus', 'Rose', 'Tulpe']
a = len(taxaList)
mat = np.zeros((a,a), float)
mat[0][0] = 0
mat[0][1] = 3
mat[0][2] = 14
mat[0][3] = 12
mat[1][0] = 3
mat[1][1] = 0
mat[1][2] = 13
mat[1][3] = 11 
mat[2][0] = 14 
mat[2][1] = 13 
mat[2][2] = 0
mat[2][3] = 4
mat[3][0] = 12
mat[3][1] = 11 
mat[3][2] = 4 
mat[3][3] = 0 
'''

# Calculates the average distances from one taxon to the others
# Input: Matrix, TaxaList 

def r_avg_distances(mat, taxaList): 

	r = [] 

	for k in range(len(mat)):

		sum = 0
		for i in range(len(mat[k])):
			sum+= mat[k][i]
		sum = sum/(len(mat)-2)
		r.append(sum)

	return(r)


# Calculates the Q-Matrix 

def gen_q_matrix(mat,r): 

	a = len(r)
	q_mat = np.zeros((a,a), float)

	for i in range(a):
		for j in range(a): 

			if i == j: 
				q_mat[i][j] = 0
			else:	
				q_mat[i][j] = mat[i][j] - (r[i] + r[j])

	return(q_mat)

# Minimal value of Q-Matrix 

def minQVal(q):

   iMin = 0
   jMin = 0
   qMin = 0

   for i in range(len(q)):
      for j in range(len(q)):
         if min(qMin, q[i][j]) == q[i][j]:
            qMin = q[i][j]
            iMin = i
            jMin = j

   if i > j:
      i, j = j, i

   return qMin, iMin, jMin

# Main function, matrix, taxalist, i-number of nodes, nodes-list
# Recursive, the algorithm

def main(mat, taxaList,i,nodes): 

	r = r_avg_distances(mat, taxaList)
	q_mat = gen_q_matrix(mat, r)
	qmin, imin, jmin = minQVal(q_mat)

	viu = (mat[imin][jmin] + r[imin] - r[jmin]) / 2 
	vju = mat[imin][jmin] - viu

	list_nodes = taxaList
	
	if imin < jmin: 

		imin, jmin = jmin, imin

	new_mat = mat 

	#delete last column 
	new_mat = np.delete(new_mat, imin,0)
	new_mat = np.delete(new_mat, jmin,0)

	#delete last row 
	new_mat = np.delete(new_mat, imin,1)
	new_mat = np.delete(new_mat, jmin,1)	
	# insert new row, column
	new_mat = np.insert(new_mat, len(new_mat[0]) ,0, axis=1)
	new_mat = np.insert(new_mat, len(new_mat), 0, axis=0)

	#new matrix 
	index_taxa = [k for k in range(len(taxaList))]

	index_taxa.remove(imin)
	index_taxa.remove(jmin)


	for l,k in enumerate(index_taxa): 
		
		
		new_mat[l][-1] = 0.5*(mat[imin][k] + mat[jmin][k] - mat[imin][jmin])
		new_mat[-1][l] = 0.5*(mat[imin][k] + mat[jmin][k] - mat[imin][jmin])

	oldTaxaList = taxaList[:]
	oldTaxaList.remove(taxaList[imin])
	oldTaxaList.remove(taxaList[jmin])
	newTaxaList = oldTaxaList + [[taxaList[imin], taxaList[jmin]]] #+ oldTaxaList
#	newTaxaList =  [[taxaList[imin], taxaList[jmin]]] + oldTaxaList

	nodes.append([taxaList[imin], taxaList[jmin]])

	distances.append(((taxaList[imin],viu,i)))
	distances.append(((taxaList[jmin],vju,i)))

	return(new_mat,newTaxaList,nodes)

# The neighbour Joining algorithm 
# Input: Distance Matrix, TaxaList 
# Output: Distances (from_node, weight, to_node)

def doNeiJo(mat, taxaList):

	new_mat = mat
	newTaxaList = taxaList
	nodes = []
	i = 0 


	while len(new_mat) != 2: 

		new_mat, newTaxaList,nodes = main(new_mat,newTaxaList,i,nodes)
		i +=1

	distances.append(((newTaxaList[0],new_mat[0][1],len(nodes)-1))) 

	list_nodes = []

	for i in range(len(distances)):

		if distances[i][0] in nodes: 
			list_nodes.append(((nodes.index(distances[i][0]),distances[i][1],distances[i][2])))
		else: 
			list_nodes.append(distances[i])

	return(list_nodes)		

	''' for Save - Distances 
	with open('distances.txt', "w") as write_file:

			for i in list_nodes:

				#format ({from node}, {weight}, {to node})
				write_file.writelines("{}".format(i) +"\n")	
	
	return(list_nodes)	
	''' 


''' Build the Guide tree for Alignment ''' 

### Init - Guide Tree ### 

def func1 (a,b,l,dist_nodes,dist_nodes_new,guide_tree):

    #remove the used 
    dist_nodes_new = [ x for x in dist_nodes_new if x[0] != a[0]]    
    dist_nodes_new = [ x for x in dist_nodes_new if x[0] != b[0]]    


    #append the new node
    for i in range(len(dist_nodes)): 

        if a[2] == dist_nodes[i][0]:
            dist_nodes_new.append(dist_nodes[i])
            
    list_sum_it = [[],[],[]] 
    for i in range(len(dist_nodes_new)-1): 
        for j in range(len(dist_nodes_new)):
            if i != j:

                if dist_nodes_new[i][2] == dist_nodes_new[j][2]:

                    
                    sum_weight = dist_nodes_new[i][1] + dist_nodes_new[j][1]
                    list_sum_it[0].append(sum_weight)
                    list_sum_it[1].append(((dist_nodes_new[i][0],dist_nodes_new[i][1],dist_nodes_new[i][2])))
                    list_sum_it[2].append(((dist_nodes_new[j][0],dist_nodes_new[j][1],dist_nodes_new[j][2])))

    a = list_sum_it[1][list_sum_it[0].index(min(list_sum_it[0]))]
    b = list_sum_it[2][list_sum_it[0].index(min(list_sum_it[0]))]




    guide_tree.append(((l,a,b)))

    return(a,b,dist_nodes_new)

# (a,b,l,dist_nodes,dist_nodes_new)

def guide_tree_func(dist_nodes): 

	list_sum = [[],[],[]]
	guide_tree = []

	for i in range(len(dist_nodes)-1): 
	    for j in range(len(dist_nodes)):
	        if i != j: 
	            if dist_nodes[i][2] == dist_nodes[j][2] and dist_nodes[i][0] != dist_nodes[j][0]: 

	                if type(dist_nodes[i][0]) is str and type(dist_nodes[i][2]) is int:
	                
	                    if type(dist_nodes[j][0]) is str and type(dist_nodes[j][2]) is int:   
	                        
	                       sum_weight = dist_nodes[i][1] + dist_nodes[j][1]
	                       list_sum[0].append(sum_weight)
	                       list_sum[1].append(((dist_nodes[i][0],dist_nodes[i][1],dist_nodes[i][2])))
	                       list_sum[2].append(((dist_nodes[j][0],dist_nodes[j][1],dist_nodes[j][2])))


	a = list_sum[1][list_sum[0].index(min(list_sum[0]))]
	b = list_sum[2][list_sum[0].index(min(list_sum[0]))]
	guide_tree.append(((0,a,b)))

	dist_nodes_new = [x for x in dist_nodes if type(x[0]) == str] 

	l = 1
	while len(dist_nodes_new) > 2: 

	    a,b,dist_nodes_new = func1(a,b,l,dist_nodes,dist_nodes_new,guide_tree)
	    l+=1

	if len(dist_nodes) % 2 == 1:  

		list_filter = []
		for i in range(len(guide_tree)):
			for j in range(1,3):

				list_filter.append(guide_tree[i][j])

		a = list(set(dist_nodes) - set(list_filter))

		guide_tree.append((l,a[0]))

	return(guide_tree)


#######################################################################

# Test taken from wikipedia:  
# - https://de.wikipedia.org/wiki/Neighbor-Joining-Algorithmus 

'''
dist_nodes = doNeiJo(mat, taxaList)

guide_tree = guide_tree_func(dist_nodes)

for i in guide_tree:

	print(i)

'''