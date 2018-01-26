def createDict():
    global nodes    
    pathList = lines[4:paths+4]
    for path in pathList:
        temp=path.split()
        if temp[0] not in nodes:
            nodes.append(temp[0])
        if temp[1] not in nodes:
            nodes.append(temp[1])
    adj = {}
    for node in nodes :
        adj[node]=[]
    Matrix = [[0 for x in range(3)] for y in range(paths)]
    count = 0
    for path in pathList:
        Matrix[count]=path.split()
        count+=1
    count=0
    while count < paths:
        if Matrix[count][0] in adj:
            adj[Matrix[count][0]].append(Matrix[count][1])
        else:
            adj.update({Matrix[count][0]:[]})
            adj[Matrix[count][0]].append(Matrix[count][1])
        count+=1
    return adj
def createDictUCS():
    global nodes
    adj = {}
    pathList = lines[4:paths+4]
    for path in pathList:
        temp=path.split()
        if temp[0] not in nodes:
            nodes.append(temp[0])
        if temp[1] not in nodes:
            nodes.append(temp[1])
    for node in nodes:
        adj[node]=[]
    Matrix = [[0 for x in range(3)] for y in range(paths)]
    count = 0
    for path in pathList:
        Matrix[count]=path.split()
        count+=1
    count=0
    while count < paths:
        if Matrix[count][0] in adj:
            adj[Matrix[count][0]].append([Matrix[count][1],int(Matrix[count][2])])
        else:
            adj.update({Matrix[count][0]:[]})
            adj[Matrix[count][0]].append([Matrix[count][1],int(Matrix[count][2])])
        count+=1
    return adj

inputFile = open ("input.txt", "r+")
lines = inputFile.readlines()
lines = [line.rstrip('\n') for line in lines]
outputFile = open('output.txt', 'w+')
start = lines[1]
goal = lines[2]
paths = int(lines[3])
sun = int(lines[4+paths])
ListOfNodes = lines[paths+5:paths+sun+5]

if lines[0] == 'BFS':
    queue= [[start]]
    def output():
        for i in range (0,len(path)):
            outputFile.write(path[i]+' '+str(i)+'\n')
            print(path[i]+' '+str(i)+'\n')
    nodes=[]
    adj = createDict()
    while queue:
        path = queue.pop(0)
        n = path[-1]
        if n == goal:
            output()
            break
        for adjacent in adj.get(n, []):
            Path = list(path)
            Path.append(adjacent)
            queue.append(Path)
        if n == goal:
            output()
            break
        
if lines[0] == 'DFS':
    def enqueue(parent):
        explored.append(parent)
        rev=adj[parent][::-1]
        length=len(queue)
        count=0
        for a in adj[parent]:
            if a in queue or a in explored:
                count+=1
        if count==len(adj[parent]) or len(adj[parent])==0:
            flag=1
            while set(c[parent]).issubset(set(explored)):
                parent=solution.pop()
                flag=0
            if flag==0:
                solution.append(parent)
        for a in rev:
            if a not in queue and a not in explored:
                queue.append(a)
                p[a]=parent
                c[parent].append(a)
        if len(queue)!=length:
            solution.append(parent)
    def output():
        for i in range (0,len(solution)):
            outputFile.write(solution[i]+' '+str(i)+'\n')
            print(solution[i]+' '+str(i))
    nodes=[]
    adj = createDict()
    solution=[]
    explored=[]
    queue=[start]
    current = start
    p={}
    c={}
    for node in nodes:
        p[node]=None
        c[node]=[]
    while queue:
        current = queue.pop()
        if current==goal:
            solution.append(current)
            break
        if current not in explored:
            enqueue(current) 
    output()       

if lines[0]=='UCS':
    def output():
        answer=[]
        node=goal
        while node is not None:
            answer.insert(0,node+" "+str(cost[node]))
            node=parent[node]
        for line in answer:
            outputFile.write(line+"\n")
            print (line)
    sun = int(lines[4+paths])
    nodes=[]
    cost={}
    parent={}
    explored=[]
    frontier=[start]
    adj=createDictUCS()
    for node in nodes:
        cost[node]=float('inf')
        parent[node]=None
    cost[start]=0
    while frontier:
        current=frontier.pop(0)
        explored.append(current)
        if current == goal:
            output()
            break
        for adjacent in adj[current]:
            if cost[current]+adjacent[1]<cost[adjacent[0]]:
                parent[adjacent[0]]=current
                cost[adjacent[0]]=cost[parent[adjacent[0]]]+adjacent[1]
                if adjacent[0] in frontier:               
                    frontier.remove(adjacent[0])
            i=0
            if adjacent[0] not in frontier and adjacent[0] not in explored:
                if frontier:
                    while cost[adjacent[0]]>=cost[frontier[i]]:
                        i+=1
                        if i==len(frontier):
                            break
                frontier.insert(i,adjacent[0])
                
if lines[0]=='A*':
    def output():
        answer=[]
        node=goal
        while node is not None:
            answer.insert(0,node+" "+str(actualCost[node]))
            node=parent[node]
        for line in answer:
            outputFile.write(line+"\n")
            print (line)
    sun = int(lines[4+paths])
    h={}
    cost={}
    parent={}
    explored=[]
    nodes=[]
    adj=createDictUCS()
    ListOfNodes = lines[paths+5:paths+sun+5]
    for node in ListOfNodes:
        temp=node.split()
        h[temp[0]]=int(temp[1])
        cost[temp[0]]=float('inf')
        parent[temp[0]]=None
    cost[start]=h[start]
    actualCost={}
    frontier=[start]
    while frontier:
        current=frontier.pop(0)
        explored.append(current)
        actualCost[current]=cost[current]-h[current]
        temp=current
        current=temp
        if current == goal:
            output()
            break
        for adjacent in adj[current]:
            if adjacent[0] not in explored:
                if actualCost[current]+adjacent[1]+h[adjacent[0]]<cost[adjacent[0]]:
                    parent[adjacent[0]]=current
                    cost[adjacent[0]]=actualCost[parent[adjacent[0]]]+adjacent[1]+h[adjacent[0]]
                    if adjacent[0] in frontier:               
                        frontier.remove(adjacent[0])
            i=0
            if adjacent[0] not in frontier and adjacent[0] not in explored:
                if frontier:
                    while cost[adjacent[0]]>=cost[frontier[i]]:
                        i+=1
                        if i==len(frontier):
                            break
                frontier.insert(i,adjacent[0])
outputFile.close() 
inputFile.close()