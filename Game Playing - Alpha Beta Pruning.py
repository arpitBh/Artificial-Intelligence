import time
start=time.time()
def evalBoard(board):
    o = 0
    x = 0
    for row in range (0,n):
        for element in range (0,n):
            if board[row][element] == 'X':
                x+=value[row][element]
            if board[row][element] == 'O':
                o+=value[row][element]
    if move=='X':
        return x-o
    else:
        return o-x
def adjacent(board,row,col):
    ans=set()
    if row==0 and col==0:
        if board[row+1][col]=='O' or board[row][col+1]=='O':
            ans.add('O')
        if board[row+1][col]=='X' or board[row][col+1]=='X':
            ans.add('X')
    elif row==0 and col==n-1:
        if board[row+1][col]=='O' or board[row][col-1]=='O':
            ans.add('O')
        if board[row+1][col]=='X' or board[row][col-1]=='X':
            ans.add('X')
    elif row==n-1 and col==0:
        if board[row-1][col]=='O' or board[row][col+1]=='O':
            ans.add('O')
        if board[row-1][col]=='X' or board[row][col+1]=='X':
            ans.add('X')
    elif row==n-1 and col==n-1:
        if board[row-1][col]=='O' or board[row][col-1]=='O':
            ans.add('O')
        if board[row-1][col]=='X' or board[row][col-1]=='X':
            ans.add('X')
    elif row==0:
        if board[row+1][col]=='O' or board[row][col+1]=='O' or board[row][col-1]=='O':
            ans.add('O')
        if board[row+1][col]=='X' or board[row][col+1]=='X' or board[row][col-1]=='X':
            ans.add('X')
    elif row==n-1:
        if board[row-1][col]=='O' or board[row][col+1]=='O' or board[row][col-1]=='O':
            ans.add('O')
        if board[row-1][col]=='X' or board[row][col+1]=='X' or board[row][col-1]=='X':
            ans.add('X')
    elif col==0:
        if board[row-1][col]=='O' or board[row+1][col]=='O' or board[row][col+1]=='O':
            ans.add('O')
        if board[row-1][col]=='X' or board[row+1][col]=='X' or board[row][col+1]=='X':
            ans.add('X')
    elif col==n-1:
        if board[row-1][col]=='O' or board[row+1][col]=='O' or board[row][col-1]=='O':
            ans.add('O')
        if board[row-1][col]=='X' or board[row+1][col]=='X' or board[row][col-1]=='X':
            ans.add('X')
    else:
        if board[row-1][col]=='O' or board[row+1][col]=='O' or board[row][col+1]=='O' or board[row][col-1]=='O':
            ans.add('O')
        if board[row-1][col]=='X' or board[row+1][col]=='X' or board[row][col+1]=='X' or board[row][col-1]=='X':
            ans.add('X')
    return ans
inputFile = open ("input.txt", "r+")
lines = inputFile.readlines()
lines = [line.rstrip('\n') for line in lines]
outputFile = open('output.txt', 'w+')
n = int(lines[0])
method = lines[1]
move = lines[2]
choice=['X','O']
alph=list(map(chr, range(65, 91)))
num=list(range(1,27))
depth = int(lines[3])
value = []
board = []
for row in range(0,n):
    temp=lines[row+4].split()
    temp = [int(x) for x in temp]
    value.append(temp)
for row in range(0,n):
    temp=lines[row+n+4]
    board.append(list(temp))    
def stakeBoard(current,row,col,chance):
    tempBoard=[]
    for row1 in current:
        tempBoard.append(row1[:])
    tempBoard[row][col]=chance
    return tempBoard
def raidBoard(current,row,col,chance):    
    raidBoard=[]
    for row1 in current:
        raidBoard.append(row1[:])
    raidBoard[row][col]=chance
    opp=choice[(choice.index(chance)+1)%2]
    if row!=0:
        if raidBoard[row-1][col]==opp:
            raidBoard[row-1][col]=chance
    if row!=n-1: 
        if raidBoard[row+1][col]==opp:
            raidBoard[row+1][col]=chance
    if col!=0:
        if raidBoard[row][col-1]==opp:
            raidBoard[row][col-1]=chance
    if col!=n-1:
        if raidBoard[row][col+1]==opp:
            raidBoard[row][col+1]=chance
    return raidBoard
ma=float('inf')
def minimax(current,d,chance):
    if d==depth:
        score=evalBoard(current)
        return score
    elif chance==move:
        score=-ma
        for row in range (0,n):
            for col in range (0,n):
                if current[row][col]=='.':
                    tempBoard=stakeBoard(current,row,col,chance)
                    score=max(score,minimax(tempBoard,d+1,choice[(choice.index(chance)+1)%2]))
        for row in range (0,n):
            for col in range (0,n):
                if current[row][col]=='.':
                    if adjacent(current,row,col)=={'O','X'}:
                        tempBoard = raidBoard(current,row,col,chance)
                        score=max(score, minimax(tempBoard,d+1,choice[(choice.index(chance)+1)%2]))   
        
        if score==-float("inf"):
            score=evalBoard(current)
        return score
    else:
        score=ma
        for row in range (0,n):
            for col in range (0,n):
                if current[row][col]=='.':
                    tempBoard=stakeBoard(current,row,col,chance)
                    score=min(score,minimax(tempBoard,d+1,choice[(choice.index(chance)+1)%2]))   
        for row in range (0,n):
            for col in range (0,n):
                if current[row][col]=='.':
                    if adjacent(current,row,col)=={'O','X'}:
                        tempBoard1 = raidBoard(current,row,col,chance)
                        score=min(score, minimax(tempBoard1,d+1,choice[(choice.index(chance)+1)%2]))
        if score==float("inf"):
            score=evalBoard(current)
        return score
def alphabeta(current,d,chance,a,b):
    if d==depth:
        score=evalBoard(current)
        return score
    elif chance==move:
        score=-ma
        for row in range (0,n):
            for col in range (0,n):
                if current[row][col]=='.':
                    tempBoard=stakeBoard(current,row,col,chance)
                    score=max(score,alphabeta(tempBoard,d+1,choice[(choice.index(chance)+1)%2],a,b))
                    if b<=a:
                        return score
        for row in range (0,n):
            for col in range (0,n):
                if current[row][col]=='.':
                    if adjacent(current,row,col)=={'O','X'}:
                        tempBoard = raidBoard(current,row,col,chance)
                        score=max(score, alphabeta(tempBoard,d+1,choice[(choice.index(chance)+1)%2],a,b))  
                        a=max(a,score)
                        if b<=a:
                            return score
        if score==-float("inf"):
            score=evalBoard(current)
    else:
        score=ma
        for row in range (0,n):
            for col in range (0,n):
                if current[row][col]=='.':
                    tempBoard=stakeBoard(current,row,col,chance)
                    score=min(score,alphabeta(tempBoard,d+1,choice[(choice.index(chance)+1)%2],a,b))  
                    b=min(b,score)
                    if b<=a:
                        return score
        for row in range (0,n):
            for col in range (0,n):
                if current[row][col]=='.':
                    if adjacent(current,row,col)=={'O','X'}:
                        tempBoard = raidBoard(current,row,col,chance)
                        score=min(score,alphabeta(tempBoard,d+1,choice[(choice.index(chance)+1)%2],a,b))                
                        b=min(b,score)
                        if b<=a:
                            return score
        if score==float("inf"):
            score=evalBoard(current)
    return score
score=[]
tempBoard=[]
text=[]
def output(board,t):
    print ()
    outputFile.write(t+"\n")
    print (t)
    for row in board:
        for element in row:
            outputFile.write(str(element))
            print(str(element), end="")
        outputFile.write("\n")
        print()
if method=="ALPHABETA":
    for row in range (0,n):
        for col in range (0,n):
            if board[row][col]=='.':
                tempBoard.append(stakeBoard(board,row,col,move))
                text.append(str(alph[col])+str(num[row])+" Stake")
                score.append(alphabeta(tempBoard[-1],1,choice[(choice.index(move)+1)%2],-ma,ma))
    for row in range (0,n):
        for col in range (0,n):
            if board[row][col]=='.':
                if adjacent(board,row,col)=={'O','X'}:
                    tempBoard.append(raidBoard(board,row,col,move))
                    text.append(str(alph[col])+str(num[row])+" Raid")
                    score.append(alphabeta(tempBoard[-1],1,choice[(choice.index(move)+1)%2],-ma,ma))
    output(tempBoard[score.index(max(score))],text[score.index(max(score))])
elif method=="MINIMAX":
    for row in range (0,n):
        for col in range (0,n):
            if board[row][col]=='.':
                tempBoard.append(stakeBoard(board,row,col,move))
                text.append(str(alph[col])+str(num[row])+" Stake")
                score.append(minimax(tempBoard[-1],1,choice[(choice.index(move)+1)%2]))
    for row in range (0,n):
        for col in range (0,n):
            if board[row][col]=='.':
                if adjacent(board,row,col)=={'O','X'}:
                    tempBoard.append(raidBoard(board,row,col,move))
                    text.append(str(alph[col])+str(num[row])+" Raid")
                    score.append(minimax(tempBoard[-1],1,choice[(choice.index(move)+1)%2]))
    output(tempBoard[score.index(max(score))],text[score.index(max(score))])

print("Time in seconds",time.time()-start)
outputFile.close() 
inputFile.close()