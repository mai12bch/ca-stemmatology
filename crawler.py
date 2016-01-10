# the crawler function 
import os 
import codecs 
import re 

# Returns a list of words and saves them into n- arrays 
# Input: Path to the files 
# Output: matrix nm - n (rows - number of files) (m-number of words per/file)

def substitute(path,punct): 

    for path, subdirs, files in os.walk(path):

        attr = [] 

        #matrix arrays of words 
        matrix = [[] for i in range(len(files))]
        
        #arrays of keys - from dictionary 
        values = [[] for i in range(len(files))]

        #Sort the files 
        files = sorted(files)

        words_dictionary = [] 
        
        j = 0 

        for filename in files:
            
            f = os.path.join(path, filename)

            file_name = os.path.join(path + "/" + filename)
            
            attrs = [] 

            #Encoding need e.g. for german, finish
            with codecs.open(file_name, "r", encoding='ISO-8859-1') as csv_file: 

                list_words = []
                words_lines_matrix = []

                for line in csv_file:

                        new_line = []
                        new_line = line.split()
                        for i in range(len(new_line)):
                            
                            list_words.append(new_line[i])
                
                values = [] 
                for m in range(len(list_words)):

                         if punct == 1:

                          out = "".join(c for c in list_words[m] if c not in ('!','.',':','"',',',';','?',"'"))
                          matrix[j].append(out)
                         
                         elif punct == 0:
                         
                          matrix[j].append(list_words[m])
                j+=1 
        
        return(matrix,files)



# Input: file path 
# Output: all the words in the texts sorted 

def crawler_words(path):  

    words = [] 
    files_crawled = [] 

    for path, subdirs, files in os.walk(path):

        i = 1 
        files = sorted(files)

        for filename in files:
            
            f = os.path.join(path, filename)

            file_name = os.path.join(path + "/" + filename)
            
            with codecs.open(file_name, "r", encoding='ISO-8859-1') as csv_file: 

                for line in csv_file:

                    list_new = [] 
                    list_new.append(re.split('(\ |\\n)+', line))
                
                    for j in range(len(list_new)):

                     for k in range(len(list_new[j])):

                        words.append(list_new[j][k])

    words_new = sorted(set(words))
    words_new = sorted(words_new)

    return (words_new)

# From list to dictionary  
# Input: words 
# Output: dictionary 

def get_words_dictionary(words):

    words_dictionary = {} 
    k = 1
    for l in range(1,len(words)): 
        if words[l] not in " ":  
            words_dictionary[k]= words[l]
            k+=1

    return words_dictionary
