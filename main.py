import time
import crawler as cw 
import csv  
import json 

from save import save_to_file 
from save import save_hw
from save import save_alignments

import progressive_multiple_alignment as pma
import pma_modified as pma_mod
from collections import defaultdict 


#Path to the files 
path = "/home/assen/Development/stemmatology/DataSet1-Heinrichi/DataSet/heinrichi"

#words in the txts 
words = []
words = cw.crawler_words(path)

#substitute path (matrix, row (words)/txt)
# if 1 = without punct; 0 with punctuation [punct: - ('!','.',':','"',',',';','?',"'")]
matrix,files =  cw.substitute(path,1)

for l in range(len(matrix)): 

    print(str(l) + " The length of the {}: ".format(files[l]) + str(len(matrix[l])))

print("Number of crawled files: " + str(len(matrix)))


###########################################################################
''' Words similiarity ''' #################################################
###########################################################################

# Not implemented 
# Maybe a precised method for aligning

###########################################################################
''' Pairwise alignment (Needleman–Wunsch algorithm) ''' ###################
# (Collating texts using Progressive Multiple Alignment)###################
###########################################################################

# hw_matrix - distance matrix between aligned sequences 
# Note: pairwise alignment is slow, use pypy3 for speedup

#save the matrix as a csv file with name 
name = 'hw_distance_matrix'
#pma.create_hw_matrix(matrix, name)


###########################################################################
'''Neighbour-joining algorithm + Guide Tree for Alignment'''###############
###########################################################################

#import nj as nj 
#import numpy as np  

# load Hw distance matrix 

#my_data = np.genfromtxt('hw_werte_check.csv', delimiter = ',')
taxaList = files

# Distances between nodes
#dist_nodes  = nj.doNeiJo(my_data, taxaList)

# Generate Guide tree for stepwise alignment
#guide_tree = nj.guide_tree_func(dist_nodes)

#print(guide_tree[0])
'''
matrix_test = [ [] for x in range(len(guide_tree))] 

for i in range(len(guide_tree)): 

    for j in range(len(guide_tree[i])):

     if isinstance(guide_tree[i][j], int):    
      
      matrix_test[i].append(guide_tree[i][j])
     
     elif isinstance(guide_tree[i][j], tuple):
      
      matrix_test[i].append(list(guide_tree[i][j]))   

save_hw(matrix_test,'guide_tree')
'''
################################################################
''' Generate json file for import to D3 '''##################### 
#################################################################

import guide_tree_D3 as gt

#Input: guide_tree - list, name- save to 
#Output: json, file 


#gt.d3_json(guide_tree,'d3_import')


#############################################################################
''' Hierarchical clustering - Dendogram (based on Distance Matrix) '''#######  
#############################################################################

#import hc as hc

#Input: Distance matrix
#TaxaList: Taxas

#hc.dendro_draw(my_data,taxaList)

#############################################################################
''' Alignment according Guide Tree              ''' #########################
''' Use the Modified Needleman–Wunsch Algorithm ''' #########################
#############################################################################


from guide_tree_alignment import gt_alignment 

#Input: guide_tree (list), matrix, files, option(save in rows or columns)
#Output: aligned files (guide_tree_{row/column}_alignment_{number})
# for speedup - pypy 

#OK! 
#option = 'r'
#gt_alignment(guide_tree, matrix, files, option)
option = 'c'
#gt_alignment(guide_tree, matrix, files, option)

#############################################################################
'''Realignment of the txts'''################################################
#############################################################################

from guide_tree_alignment import realignment 

#def realignment(method, matrix, files): 
#Input mathod(1 or 2), matrix, files, full_alignment 
#Output saved filed 

#realignment(1,matrix, files)
#realignment(2,matrix, files)

##########################################################
'''After Alignment transpose to a Matrix ''' 
###########################################################

'''
# Transpose the file so the texts will be in columns  
with open("complete_list.txt") as f: 

    reader = csv.reader(f, delimiter=",")

    complete_list = [] 
    for row in reader:
        complete_list.append(row)

for i in range(len(complete_list)): 

    print(i, len(complete_list[i]), len(list_full_alignment[i]))

transposed_complete_list = list(zip(*complete_list))

with open("transposed_complete_list.txt", "w") as write_file: 
       
    writer = csv.writer(write_file)
    writer.writerows(transposed_complete_list)


import numpy as np  

data = np.genfromtxt("complete_list.txt", dtype=str,  delimiter = ",")

print(data[0])
'''


#############################################################################
''' Create ARFF file                            ''' #########################
'''                                             ''' #########################
#############################################################################

import create_arff as carff

#Input: path_to_aligned filed, matrix, files, name of the arff file 

path = "/home/assen/Development/stemmatology/Python_Script/guide_tree_row_alignment_35.txt"
#carff.arff(path, matrix, files, 'heinrichi')

carff.max_parsimony(path, matrix, files, 'heinrichi_parsimony')

#############################################################################
''' Weka - classification                       ''' #########################
'''                                             ''' #########################
#############################################################################

#- opens with python2 

#############################################################################
''' Evaluation '''                                  #########################
#############################################################################


#####################################################################
# Some tests
########################################################################
'''
    #Guide_Tree
    #(DA matrix[17]- I matrix[22]) -> 0.node 
    #(J matrix[23] - 0) -> 1.node 
    #(Cc matrix[13] - Ce matrix[15]) -> 3.node 
    #(1 - 3) -> 5.node 

#align D-I 

node_0 = []
AlignmentA, AlignmentB = pma.alignment(matrix[17], matrix[22])
node_0.append(AlignmentA)
node_0.append(AlignmentB)
# functions 


node_1 = []
AlignmentA, AlignmentB = pma_mod.alignment(matrix[23], node_0)
node_1.insert(0,AlignmentA)
node_1.insert(1,AlignmentB[0])
node_1.insert(2,AlignmentB[1])

print("before node_3")
node_3 = []
AlignmentA, AlignmentB = pma.alignment(matrix[13], matrix[15])
node_3.append(AlignmentA)
node_3.append(AlignmentB)

print("final_node")
node_final = []
AlignmentA, AlignmentB = pma_mod.alignment(node_1, node_3)
node_final.insert(0,AlignmentA[0])
node_final.insert(1,AlignmentA[1])
node_final.insert(2,AlignmentA[2])
node_final.insert(3,AlignmentB[0])
node_final.insert(4,AlignmentB[1])  
#a = zip(*node_final)
with open("re_aligned.csv", "w") as write_file: 

    writer = csv.writer(write_file , delimiter = "\t", escapechar= ' ', quoting = csv.QUOTE_NONE)

    writer.writerows(zip(*node_final))
'''