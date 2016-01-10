import csv 
from collections import defaultdict 
import progressive_multiple_alignment as pma
import pma_modified as pma_mod


#############################################################################
''' Alignment according Guide Tree              ''' #########################
''' Use the Modified Needleman–Wunsch Algorithm ''' #########################
#############################################################################

#Input: guide_tree_list, matrix, r or c (save in row or columns)
#Output: aligned files according the guide tree in rows or oclumns 


d = defaultdict(list)
list_alignments = []

# guide_tree example 
#(0, ('V.txt', 0.1158940972222223, 26), ('Ba.txt', 0.1941059027777777, 26))
#(1, ('P.txt', 0.21434709821428574, 28), (26, 0.015652901785714268, 28))

def gt_alignment(guide_tree, matrix, files, option):


    for i in range(len(guide_tree)-1):

        #print(guide_tree[i])
        print(i,guide_tree[i][1][0] ,guide_tree[i][2][0],guide_tree[i][1][2])

        # if both files are texts - DO a pairwise alignment
        if type(guide_tree[i][1][0]) == str and type(guide_tree[i][2][0]) == str: 

            a = files.index(guide_tree[i][1][0]) 
            b = files.index(guide_tree[i][2][0]) 
            
            AlignmentA,AlignmentB = pma.alignment(matrix[a],matrix[b])
            check_a = any( isinstance(e, list) for e in AlignmentA)
            check_b = any( isinstance(e, list) for e in AlignmentB)

            print("Two files aligned: " + str(len(AlignmentA)) + "\t" + str(len(AlignmentB)))

            d[guide_tree[i][1][2]].append(AlignmentA)
            d[guide_tree[i][1][2]].append(AlignmentB)        
        
        # if the first file to align is a text and the second list of texts 
        # use the modified pairwise alignment
        elif type(guide_tree[i][1][0]) == str and guide_tree[i][2][0] in d.keys():

            a = files.index(guide_tree[i][1][0])

            AlignmentA,AlignmentB = pma_mod.alignment(matrix[a],d[guide_tree[i][2][0]])
            check_a = any( isinstance(e, list) for e in AlignmentA)
            check_b = any( isinstance(e, list) for e in AlignmentB)
            
            print("First str, second list: " + str(len(AlignmentA)) + "\t" + str(len(AlignmentB[-1])))

            d[guide_tree[i][1][2]].append(AlignmentA)

            if check_b == True: 

                for k in range(len(AlignmentB)):
                
                    d[guide_tree[i][1][2]].append(AlignmentB[k])        
        
        # if the list of texts and a text     
        elif guide_tree[i][1][0] in d.keys() and type(guide_tree[i][2][0]) == str: 

            a = files.index(guide_tree[i][2][0])

            AlignmentA, AlignmentB = pma_mod.alignment(d[guide_tree[i][1][0]],matrix[a])
            check_a = any( isinstance(e, list) for e in AlignmentA)
            check_b = any( isinstance(e, list) for e in AlignmentB)

            print("First list, second str: " + str(len(AlignmentA[-1])) + "\t" + str(len(AlignmentB)))
            
            if check_a == True: 

                for k in range(len(AlignmentA)):
                    d[guide_tree[i][1][2]].append(AlignmentA[k])
            d[guide_tree[i][1][2]].append(AlignmentB)        

        # if both are list of texts do a modified pairwise alignment    
        elif guide_tree[i][1][0] in d.keys() and guide_tree[i][2][0] in d.keys(): 
        
            AlignmentA, AlignmentB = pma_mod.alignment(d[guide_tree[i][1][0]],d[guide_tree[i][2][0]])
            check_a = any( isinstance(e, list) for e in AlignmentA)
            check_b = any( isinstance(e, list) for e in AlignmentB)

            print("Both lists: " + str(len(AlignmentA[-1])) + "\t" + str(len(AlignmentB[-1])))

            if check_a == True and check_b == True: 

                for k in range(len(AlignmentA)):

                    d[guide_tree[i][1][2]].append(AlignmentA[k])
            
                for k in range(len(AlignmentB)):    
            
                    d[guide_tree[i][1][2]].append(AlignmentB[k])        
                    

    print(guide_tree[-1][0], guide_tree[-1][1][0], guide_tree[-1][1][2])

    # Align the last item in the guided list 
    AlignmentA, AlignmentB = pma_mod.alignment( d[guide_tree[-1][1][0]], d[guide_tree[-1][1][2]] )

    check_a = any( isinstance(e, list) for e in AlignmentA) 
    check_b = any( isinstance(e, list) for e in AlignmentB)

    if check_a == True and check_b == True: 

        for k in range(len(AlignmentA)):

            d[guide_tree[-1][0]].append(AlignmentA[k])
            
        for k in range(len(AlignmentB)):    
            
            d[guide_tree[-1][0]].append(AlignmentB[k])        

    # Guide Tree alignment (save the full alignment)
    
    if option == "r": 

     name = 'row'

    elif option == "c":

     name = 'column'

    for i in d.keys(): 

      with open("guide_tree_{}_alignment_{}".format(name,i) + '.txt', "w") as write_file: 
           
            writer = csv.writer(write_file)
            if option == "r": 
    #save in rows
             writer.writerows(d[i])
            elif option == "c": 
    # save in columns 
             writer.writerows(zip(*d[i]))
            else: 
             print("No Option choosed!") 




######two methods######### 

# 1. Method (align to whole group guide_tree_alignment_35)  
# 2. Method (align and remove )


###################################################################
# 1.Method (easiest one - align matrix[i], to list_full_alignment
# disadvantage: gets different alignments of the texts not a perfect matrix 
###################################################################


def realignment(method, matrix, files): 

    # 35 is the final alignment in this case 

    with open("/home/assen/Development/stemmatology/Python_Script/guide_tree_row_alignment_35.txt") as f: 
    #with open("guide_tree_alignment_35.txt") as f: 

        reader = csv.reader(f, delimiter=",")

        list_full_alignment = [] 
        for row in reader:
            list_full_alignment.append(row)
    
    print(method)
    #print(list_full_alignment)
###################################################################
# 1.Method (easiest one - align matrix[i], to list_full_alignment
# disadvantage: gets different alignments of the texts not a perfect matrix 
###################################################################
    
    if method == 1:

        print("Before")
        method_1_alignment = []  

        for i in range(len(matrix)):
        #for i in range(1):
            print(i)
            AlignmentA, AlignmentB = pma_mod.alignment(matrix[i], list_full_alignment)
                
            method_1_alignment.append(AlignmentA)
            print(len(AlignmentA))

        #save to a file "method_1_alignment"
        save_alignments(method_1_alignment,'method_1_alignment')

#####################################################
# 2.Method (remove, align and add )##################
#####################################################
    
    elif method == 2: 

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

        list_indexes = sorted(list_indexes)


        d_complete = defaultdict(list)

        # Do realignment of all the sequences  

        def do_realignment(i, complete_list, list_indexes, list_full_alignment): 

                    #print(list_full_alignment[list_indexes[i][1]])
                    complete_list.remove(list_full_alignment[ list_indexes[i][1] ])

                    print("Before alignment - complete_list | removed index ", len(complete_list),i)
                    a = list_full_alignment[list_indexes[i][1]]
                    
                    print( "Before alignment - Text: ",list_indexes[i][0], "Length: ", len(a))

                    AlignmentA,AlignmentB = pma_mod.alignment(a, complete_list )

                    complete_list.insert(i, AlignmentA)

                    print("After Alignment - Text: ", list_indexes[i][0], "Length: ", len(AlignmentA))
                    print("Complete_List lenght ", len(complete_list))

                    return(complete_list)

        i = 0
        complete_list = list_full_alignment[:]
        while (i != len(list_full_alignment)):
        #while (i != 1):

            print(i)
            complete_list = do_realignment(i, complete_list, list_indexes, list_full_alignment)

            i+=1

        method_2_alignment = complete_list[:]

        save_alignments(method_2_alignment, "method_2_alignment")


   
