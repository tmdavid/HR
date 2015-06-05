__author__ = 'dtorrejon'

def init():
    graph = {'A':{'B':5,'C':5, 'D':1, 'E':1},'B':{'E':5,'C':1,'F':15},'C':{'G':2,'D':8},'D':{'B':1,'H':30},'E':{'F':1,'G':2},'F':{'G':4},'G':{'C':4,'H':1},'H':{'C':4,'E':4,'D':4,'B':4,'A':4}}
    D = {}
    for element in graph:
        D[element] = float("inf")                          # Distances

    V = []                          # Visited
    NV = {}                          #Predecesors
    return (D, V, NV,graph)

def dijkstra(graph, O, E, V, D, NV): #gets the graph, origin and end, O-> E

    NV = dict(D)
    D[O] = 0
    current = graph.get(O)
    path = []
    currentkey = O
    print currentkey
    while (currentkey != E):
        for node in current:
            if(D[node]>D[currentkey]+abs(D[currentkey]-current[node])): #5>1+abs(1-2)
                D[node] = D[currentkey]+abs(current[node])
                NV[node] = D[currentkey]+abs(current[node])
        NV.pop(currentkey)
        currentkey = min(NV, key=NV.get)
        current = graph.get(currentkey)
        print currentkey
    return path, D
def main():
    D, V, NV, graph = init()
    origin = 'A'
    end = 'C'
    print "Computing distance between %s (origin) and %s (end)" % (origin, end)
    output, distance = dijkstra(graph,origin, end, V, D, NV)
    print "The path is %s with distance %d" %(output, distance[end])
    print "The path should be A D B C"
    print distance

if __name__ == "__main__":
    main()
