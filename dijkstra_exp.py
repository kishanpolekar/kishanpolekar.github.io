def dijkstra(g,start,end):
    path,total,s=[start],0,{}
    for curr in g.get(start).keys():
        while curr!=end:
            temp,m=[],[]
            curr_values=sorted(list(g.get(curr).values()))
            if len(curr_values)>=1:
                for key,value in g.get(curr).items():
                    if value==curr_values[0]:
                        temp.append(key)
                if len(temp)==1:
                    path.append(temp[0])
                    total+=curr_values[0]
                    curr=temp[0]
                else:
                    for i in temp:
                        m.append(sorted(list(g.get(i).values()))[0])
                    m.sort()
                    for i in temp:
                        if curr in temp:break
                        for k,v in g.get(i).items():
                            if v==m[0]:
                                path.append(i)
                                total+=curr_values[0]
                                curr=i
                                break
            else:
                return(path,0)
            for i in range(len(path)-2):
                if (curr in list(g.get(path[i]).keys())) and (total>=g.get(path[i]).get(curr)):
                    del path[i+1:]
                    path.append(curr)
                    total=g.get(path[i]).get(curr)
            s[total]=path
    return (s)

def main():
    print('Dijkstra\'s algorithm\n')
    n,g=int(input('Enter the number of nodes: ')),{}
    for i in range(n):
        g.update({input('Enter the name of node {}: '.format(i+1)):{}})
    for node in list(g.keys()):
        x=''
        while(x.lower()!='end'):
            x=input('Enter the next connection of \'{}\' as "node:weight". Enter "end" when no other connection is available: '.format(node))
            x1=x.split(':')
            if x1[0].lower()!='end':
                g[node][x1[0]]=int(x1[1])
    start,end,s,t,m,path,total=input('Enter the start node: '),input('Enter the end node: '),{},{},[],[],0
    for key1,value1 in g.items():
        s=dijkstra(g,key1,end)
        t.update(s)
    m=sorted(t.keys())
    print(t,m)
    m[:]=(val for val in m if val!=0)
    for v,k in t.items():
        if v==m[0]:
            path=k
            total=v
    print('The shortest path from \'{}\' to \'{}\' is {}. The total weight of the shortest path is {}.'.format(start,end,path,total))
main()
