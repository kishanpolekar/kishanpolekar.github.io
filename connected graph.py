def is_connected(g,keys):
    visited=[]
    for key in keys:
        nodes=g.get(key)
        for i in nodes:
            if not i in visited:
                visited.append(i)
        if sorted(keys)==sorted(visited):
            return True
    return(sorted(keys)==sorted(visited))

def main():
    print('Connected Graph\n')
    g={'a':['d','f'], 'b':['c'], 'c':['b','e'], 'd':['a','f'], 'e':['c','f'], 'f':['a','d']}
    conn=is_connected(g,list(g.keys()))
    print('It is a connected graph!') if conn else print('The graph is not connected.')
main()
