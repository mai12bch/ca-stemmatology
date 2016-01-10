import json


#################################################################
''' Generate json file for D3 '''################################ 
#################################################################


#Input: guide_tree - list (a like:) 
#(0, ('V.txt', 0.1158940972222223, 26), ('Ba.txt', 0.1941059027777777, 26))
#Output: saved file

def d3_json(guide_tree_list,name): 

    guide_tree = guide_tree_list
    
    nodes_list = []
    for i in range(len(guide_tree)-1): 
        nodes_list.append(guide_tree[i][1][0])
        nodes_list.append(guide_tree[i][2][0])

    nodes_list.append(guide_tree[-1][1][0])
    nodes_list.append(guide_tree[-1][1][2])


    nodes_list = ['{}.{}'.format(x,'txt') if type(x) == int else x for x in nodes_list] 
    nodes_list = [str(x) for x in nodes_list]
    nodes_list = sorted(nodes_list)
    d = {} 
    #(0, ('V.txt', 0.1158940972222223, 26), ('Ba.txt', 0.1941059027777777, 26))

    link_list = [] 
    for i in range(len(guide_tree) -1 ):

        link_list.append(((guide_tree[i][1][0],guide_tree[i][1][2],guide_tree[i][1][1])))
        link_list.append(((guide_tree[i][2][0],guide_tree[i][2][2],guide_tree[i][2][1])))


    link_list.append(((guide_tree[-1][1][0],guide_tree[-1][1][2],guide_tree[-1][1][1])))


    json_file = [] 

    #################
    # Append nodes###
    ################# 
    json_file.append('{')
    json_file.append('"nodes": [')
    for i in range(len(nodes_list)-1): 
        json_file.append('{{"id": "{}"}},'.format(nodes_list[i]))

    json_file.append('{{"id": "{}"}}'.format(nodes_list[-1]))
    json_file.append('],')

    #################
    # Append links ##
    #################

    json_file.append("   ")

    json_file.append(' "links":[ ')

    for i in range(len(link_list)-1):
        #{source: "Microsoft", target: "Amazon", type: "licensing", value: 60}
        if type(link_list[i][0]) == int and type(link_list[i][1]) == int:  

            json_file.append('{{"source": "{}.txt", "target": "{}.txt", "value": "{}"}},'.format(link_list[i][0],link_list[i][1],link_list[i][2]))

        elif type(link_list[i][0]) == int: 
            json_file.append('{{"source": "{}.txt", "target": "{}", "value": "{}"}},'.format(link_list[i][0],link_list[i][1],link_list[i][2]))

        elif type(link_list[i][1]) == int: 
            json_file.append('{{"source": "{}", "target": "{}.txt", "value": "{}"}},'.format(link_list[i][0],link_list[i][1],link_list[i][2]))

        else: 

            json_file.append('{{"source": "{}", "target": "{}", "value": "{}"}},'.format(link_list[i][0],link_list[i][1],link_list[i][2]))

    json_file.append('{{"source": "{}.txt", "target": "{}.txt", "value": "{}"}}'.format(link_list[-1][0],link_list[-1][1],link_list[-1][2])) 
    json_file.append(']')
    json_file.append('}')

    name = name

    with open('nodes_{}.json'.format(name), 'w') as outfile:
        #json.dump(json_file, outfile)
            
        for i in range(len(json_file)):
            outfile.writelines(json_file[i]+"\n")

