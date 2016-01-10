import pylab
import numpy as np  
from scipy.cluster.hierarchy import linkage, dendrogram


# Create an empty matrix
def create_matrix(m, n):
    return [[0]*n for _ in range(m)]

def scoring_distance_matrix(scoring_matrix,taxaList):
 
    scoring_distance_matrix = create_matrix(len(scoring_matrix[0]), len(scoring_matrix[0]))
    maxR = get_matrix_max(scoring_matrix)
 
    for i in range(0, len(taxaList)):
        for j in range(0, len(taxaList)):
            scoring_distance_matrix[i][j] = abs(scoring_matrix[i][j] - maxR)

    return scoring_distance_matrix

# Return the max value in a matrix, used in scoring_distance_matrix method
def get_matrix_max(matrix):
 
    max_value = None
 
    for i in range(0, len(matrix[0])):
        for j in range(0, len(matrix[0])):
            if(max_value == None):
                max_value = matrix[i][j]
            if(matrix[i][j] >= max_value):
                max_value = matrix[i][j]
 
    return max_value


def dendro_draw(sc_matrix, taxaList):


    scoring_distance_matrix1 = scoring_distance_matrix(sc_matrix,taxaList)
    average = linkage(scoring_distance_matrix1, "average")
    dendrogram(average, labels=taxaList, orientation="left", leaf_font_size=8)
    pylab.subplots_adjust(bottom=0.1, left=0.2, right=1.0, top=1.0)
   # for save (pdf, png)
   # pylab.savefig("dendro.pdf")
    pylab.show()

