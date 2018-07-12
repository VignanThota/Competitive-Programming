def arrange(l):
    l=sorted(l)
    l.reverse()
    for i in range(len(l)-1):
        if(l[i][0]==l[i+1][0]):
            if(l[i][1]>l[i+1][1]):
                l[i],l[i+1]=l[i+1],l[i]
                i=0
    nl = []
    for people in l:
        nl.insert(people[1], people)
    print(nl,"\n")


    pass

arrange([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
arrange([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]])
arrange([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]])