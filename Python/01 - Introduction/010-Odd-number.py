def numPlayers(k, scores):
    #total number of scores
    n=len(scores)
    #sort scores in descending order
    scores=sorted(scores,reverse=True)
    #create a list to store rank of players
    rank=[]
    #start with rank 1
    r=1
    #stores previous score initialized to -1
    prev=-1
    #for all players
    for i in range(n):
    #if current player is the first one
    if prev==-1:
    #append rank
    rank.append(r)
    #update previous
    prev=scores[i]
    #else if current player's score equals previous player's score then
    elif prev==scores[i]:
    #append same rank
    rank.append(r)
    #otherwise if different
    else:
    #update previous score
    prev=scores[i]
    #append rank
    rank.append(i+1)
    #update rank
    r=i+1
    #to count number of players which can level up
    count=0
    #iterate for all players
    for i in range(n):
    #if score is non-zero and rank is less than equal to k then count this player
    if scores[i]!=0 and rank[i]<=k:
    count+=1
    #return count
    return count