# ca-stemmatology

This repository contains computer-assisted stemmatology programs

1. Crawler ("crawler.py")  

   1.1 crawler_words(path) - returns all the words in a list 
   1.2. substitute(path, punct). Every text is splitted into words and saved in a row in a matrix. If punct = 0 - with punctuation, punct = 1 without punctuation. Punctuation removed [punct: - ('!','.',':','"',',',';','?',"'")]

2. Pairwise-Alignment (Needleman-Wunsh algorithm) ("progressive_multiple_alignment.py")

   2.1 Alignment(seq1, seq2) - returns the aligned sequences (AlignmentA, AlignmentB) 
   2.2 Hx (AlignmentA, AlignmentB) - returns a value which measures the similiarity between the aligned sequences (Estimating Distances between Manuscripts based on copying errors, Matthew Spencer and Christopher Howe 2001)
   2.3 create_hw_matrix(matrix,name) - returns a distance matrix between the sequences(texts), diagonal = 0 

3. Neighbour-joining algorithm (NJ) + Guide Tree for alignment  ("nj.py")
Note: the NJ algorithm uses the numpy package 

   3.1 doNeiJo(distance_matrix, taxaList(in this case file names)) - computing the distances between the txts 
   3.2 guide_tree_func(dist_nodes) - generates a guide tree for a multiple alignment 

4. D3 Json file ("guide_tree_D3.py")
   
   4.1 d3_json(guide_tree, name) - generates a json file for import to D3, visualization 

5. Hierarchical clustering - Dendogram (based on the distance matrix from the pairwise-alignment) ("hc.py")
   
   5.1 dendro_draw(distance_matrix, taxaList(file_names)) - draws a hierarchical cluster bases on the distances between txts 


6. Alignment according Guide Tree (GTA): Modified Needleman-Wunsch Algorithm  ("guide_tree_alignment.py")
   
   6.1 gt_alignment(guide_tree, matrix, files, option). Option (r - row, c - column) 
   6.2 realignment(option, matrix, files). Option: 1 oder 2, two different methods 

7. Create ARFF file ("create_arff.py")
   
   7.1 arff(file, matrix, files, name) - creates an ARFF file for WEKA input 
   7.2 max_parsimony(file, matrix, files, name) - creates a maximum parsimony file 
