import os 
import csv 

# Save functions, to files

def save_to_file(list_im,name): 
    
    name = str(name)
    files = list_im
    with open("{}".format(name) + '.txt', "w") as write_file: 
       
        for l in range(len(files)):

        	write_file.writelines("{},{},{}".format(files[l][0],files[l][1],files[l][2])+"\n")

    return(print("Saved " + name + ".txt file"))

def save_words_to_file(words,name): 
    
    name = str(name)

    with open("{}".format(name) + '.txt', "w") as write_file: 
       
        k = 1
        for l in range(1,len(words_new)): 
            if words_new[l] not in " ":  
                write_file.writelines("{},{}".format(k,words_new[l])+"\n")
                k+=1

    return(print("Saved " + name + ".txt file"))
               
def save_hw(hw_werte,name): 
    
    name = str(name)

    with open("{}".format(name) + '.csv', "w") as write_file: 
       
     writer = csv.writer(write_file)
     writer.writerows(hw_werte)

    return(print("Saved " + name + ".txt file"))

'''
    with open("{}".format(name) + '.txt', "w") as write_file: 
       
        for l in range(len(hw_werte)): 

            write_file.writelines("{}".format(hw_werte[l])  +"\n")
'''
    


def save_distances(hw_werte,name): 
    
    name = str(name)

    with open("{}".format(name) + '.txt', "w") as write_file: 
       
        for l in range(len(hw_werte)): 

            write_file.writelines("{}".format(hw_werte[l])  +"\n")
               
    return(print("Saved " + name + ".txt file"))


def save_alignments(reordered_list, name): 

    with open("{}".format(name) + '.txt', "w") as write_file: 
           
        writer = csv.writer(write_file)
        writer.writerows(reordered_list)
