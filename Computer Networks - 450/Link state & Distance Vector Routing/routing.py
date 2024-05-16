# Norman Cook
# 2/18/2024
# 102-45-233
# Description:

# ex terminal call
# python routing.py topology.csv
import sys
import csv

# main loop of program
def Main(file):
    reader = csv.reader(file)
    # create list of labels
    nodes = file
    #for col in file:
    #    nodes.append(col[''])
    print(nodes)

    print(reader)

    # read contents of file
    # read in columns and rows not starting at 0

    # ask for source node
    source_node = input('Please, provide the source node: ')
    isValid = False
    for node in nodes:
        if node == source_node:
            isValid = True
    if not isValid:
        print("wrong input!")
        sys.exit()

    # Dijkstra's Calculation ##################

    # initialization
    reader = csv.reader(file)
    for col in reader:
        print(col)
        # connection doesn't exist, cost = infinite
        if col[source] == 9999:
            print('infinite')
            return
        else:
            print(col+' not found')
        
    for f in file:
        print(file[0])
    #paths = calculatePath(file,source_node)
    #print(paths)

    # Bellman-Ford Calculations

# recursively scan through for path to each node
def calculatePath(list,source):
    print('here')
    for col in list:
        print(col)
        # connection doesn't exist, cost = infinite
        if col[source] == 9999:
            print('infinite')
            return
        else:
            path = 'u'+'w'+calculatePath(list,source)
            return path

def pathCost(headers, costs, x, y):
    for i in range(len(headers)):
        if headers[i] == x:
            ix = i
        if headers[i] == y:
            iy = i
    cost = costs[ix][iy]
    return cost

# python saves arguments passed in from command line
# access sys package for these arguments
file_location = sys.argv[1]
#if (True):
#    file = csv.DictReader(open(file_location, 'r'))
#else:
#    print('File not found.')
#    sys.exit()

#csvfile = open(file_location)
#reader = csv.reader(csvfile)

with open(file_location, 'r') as csvfile:
    content = csv.reader(csvfile)

    # parse data
    nodes = []
    rows = []
    first_pass = True
    for row in content:
        if first_pass:
            nodes = row[1:]
            first_pass = False
        else:
            rows.append(row[1:])

    # ask for source node
    source_node = input('Please, provide the source node: ')
    isValid = False
    for node in nodes:
        if node == source_node:
            isValid = True
    if not isValid:
        print("wrong input!")
        sys.exit()

    # parse
    fwd_table_nodes = []
    fwd_table_rows = []
    cur_node = source_node
    fwd_table_nodes.append(cur_node)
    for i in range(len(nodes)):
        if nodes[i] != source_node:
            cur_node += nodes[i]
            fwd_table_nodes.append(cur_node)
        fwd_table_rows.append(rows[i])
    print(fwd_table_nodes)
    print(fwd_table_rows)

    test = pathCost(nodes, fwd_table_rows, 'u', 'v')
    print(test)

    # shortest path tree
    paths=[]
    ignore=[source_node]
    for node in nodes:
        if node != source_node:
            cost = pathCost(nodes, fwd_table_rows, source_node, node)

            if cost == '9999':
                print('infinite')
                # go deeper
                recursiveTree(nodes, ignore)
            else:
                paths.append(source_node + node)
                ignore.append(node)
    print(paths)

    # generate trace table
    
    

#Main(reader)
