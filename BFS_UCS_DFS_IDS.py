found = False;
dfs = []


class Graph:

    def __init__(self):
        self.blocked = ['6,2', '8,2', '9,2', '10,2', '13,1', '13,2', '14,2', '8,3', '9,3', '10,3', '3,4', '4,4', '3,5',
                        '4,5', '6,5', '7,5', '8,5', '11,5', '13,5', '6,6', '7,6', '8,6', '11,6', '13,6', '6,7', 7, 7,
                        '8,7', '9,7', '11,7', '1,8', '2,8', '6,8', '7,8', '8,8', '9,8', '11,8', '6,9', '7,9', '8,9',
                        '11,9', '13,9', '14,9', '11,10', '13,10', '14,10', '1,11', '2,11', '3,11', '6,11', '7,11',
                        '8,11', '9,11', '1,12', '2,12', '3,12', '6,12', '7,12', '8,12', '9,12', '10,14', '11,14',
                        '13,14', '1,15', '2,15', '3,15', '4,15', '5,15', '6,15', '10,15', '11,15', '13,15']
        self.graph = {}
        self.NoOfVertices = 0

    def isComplete(self):
        for n in self.graph:
            if self.graph.get(n) != self.graph.keys():
                print("incomplete Graph")
                return 0
        print("Complete Graph")
        return 0

    def DLS(self, src, target, maxDepth):

        if src == target: return True
        if maxDepth <= 0: return False

        for i in self.graph[src]:
            if self.DLS(i, target, maxDepth - 1):
                return True
        return False

    def uniform_cost_search(self, goal, start):
        global cost
        answer = []
        queue = []

        for i in range(len(goal)):
            answer.append(10 ** 8)

        queue.append([0, start])
        visited = {}
        count = 0

        while len(queue) > 0:
            queue = sorted(queue)
            p = queue[-1]
            del queue[-1]
            p[0] *= -1
            if p[1] in goal:
                index = goal.index(p[1])
                if answer[index] == 10 ** 8:
                    count += 1
                if answer[index] > p[0]:
                    answer[index] = p[0]

                del queue[-1]
                queue = sorted(queue)
                if count == len(goal):
                    return answer

            if p[1] not in visited:
                for i in range(len(self.graph[p[1]])):
                    queue.append([(p[0] + cost[(p[1], self.graph[p[1]][i])]) * -1, self.graph[p[1]][i]])

            visited[p[1]] = 1
        return answer

    def IDDFS(self, src, target, maxDepth):
        for i in range(maxDepth):
            if self.DLS(src, target, i):
                return True
        return False

    def DFSUtil(self, v, visited, dfs, goal):
        visited.add(v)
        dfs.append(v)
        if v == goal:
            return dfs

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if neighbour not in visited:
                    self.DFSUtil(neighbour, visited, dfs, goal)
        return dfs

    def DFS(self, start, goal):
        dfs = []
        visited = set()
        dfs = self.DFSUtil(start, visited, dfs, goal)
        return dfs

    def add_vertex(self, newVertex):
        if newVertex in self.graph:
            print("Vertex ", newVertex, " already exists.")
        else:
            self.NoOfVertices = self.NoOfVertices + 1
            self.graph[newVertex] = []

    def BFS(self, start, end):
        visited = []
        queue = []
        bfs = []
        visited.append(start)
        queue.append(start)

        while len(queue) != 0:
            first_out = queue.pop(0)
            bfs.append(first_out)

            for neighbour in self.graph[first_out]:
                if end not in bfs:
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.append(neighbour)
                else:
                    return bfs
        return -1

    def add_vertex(self, newVertex):
        if newVertex in self.graph:
            print("Vertex ", newVertex, " already exists.")
        else:
            self.NoOfVertices = self.NoOfVertices + 1
            self.graph[newVertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            print("Vertex1 ", vertex1, " not exist.")
        elif vertex2 not in self.graph:
            print("Vertex2", vertex2, "not exist.")
        else:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)

    def display(self):
        print("\033[91m {}\033[00m".format("  Graph"))
        print("\033[91m {}\033[00m".format(self.graph))

    def makeplot(self):
        i = 0
        for V in range(1, 16):
            for H in range(1, 16):
                newVertex = str(V) + ',' + str(H)
                self.add_vertex(newVertex)

        for vertex in self.graph.keys():
            spList = vertex.split(',')
            Ver = int(spList[0])
            Hor = int(spList[1])
            if Ver > 1:
                newVertex1 = str(Ver - 1) + ',' + str(Hor)
                self.add_edge(vertex, newVertex1)
            else:
                newVertex1 = 0
            if Hor > 1:
                newVertex2 = str(Ver) + ',' + str(Hor - 1)
                self.add_edge(vertex, newVertex2)

            else:
                newVertex2 = 0
            if Ver > 1 and Hor > 1:
                newVertex3 = str(Ver - 1) + "," + str(Hor - 1)
                self.add_edge(vertex, newVertex3)

            else:
                newVertex3 = 0
            if Ver < 15 and Hor < 15:
                newVertex4 = str(Ver + 1) + "," + str(Hor + 1)
                self.add_edge(vertex, newVertex4)

            else:
                newVertex4 = 0
            if Ver < 15:
                newVertex5 = str(Ver + 1) + "," + str(Hor)
                self.add_edge(vertex, newVertex5)

            else:
                newVertex5 = 0
            if Hor < 15:
                newVertex6 = str(Ver) + "," + str(Hor + 1)
                self.add_edge(vertex, newVertex6)

            else:
                newVertex6 = 0  # print(vertex,"-->",newVertex1,newVertex2,newVertex3,newVertex4,newVertex5,newVertex6)

        # self.display()


def cost(path):
    cos = 0;
    for i in range(2, 16):
        v1 = path[i - 1]
        v2 = path[i]
        v1L = v1.split(',')
        V1ver = int(v1L[0])
        V1Hor = int(v1L[1])

        v2L = v2.split(',')
        V2ver = int(v2L[0])
        V2Hor = int(v2L[1])

        difV = V1ver - V2ver
        DifH = V1Hor - V2Hor
        if (difV == 0 or difV == 0):

            cos = cos + 2
        else:
            cos = cos + 3
    return cos


def dispay(graph, sol, block):
    keys = graph.keys()
    for h in range(1, 16):
        for v in range(1, 16):
            vertex = str(16 - h) + ',' + str(v)
            # print(vertex,end='  ')
            if vertex in blocked:
                print("x", end='  ')
            elif vertex in sol:
                print("1", end='  ')
            else:
                print("0", end='  ')

        print("")


loop = True
blocked = ['6,2', '8,2', '9,2', '10,2', '13,1', '13,2', '14,2', '8,3', '9,3', '10,3', '3,4', '4,4', '3,5', '4,5', '6,5',
           '7,5', '8,5', '11,5', '13,5', '6,6', '7,6', '8,6', '11,6', '13,6', '6,7', '7,7', '8,7', '9,7', '11,7', '1,8',
           '2,8', '6,8', '7,8', '8,8', '9,8', '11,8', '6,9', '7,9', '8,9', '11,9', '13,9', '14,9', '11,10', '13,10',
           '14,10', '1,11', '2,11', '3,11', '6,11', '7,11', '8,11', '9,11', '1,12', '2,12', '3,12', '6,12', '7,12',
           '8,12', '9,12', '10,14', '11,14', '13,14', '1,15', '2,15', '3,15', '4,15', '5,15', '6,15', '10,15', '11,15',
           '13,15']
while (loop == True):
    print('1 for BFS')
    print('2 for DFS')
    print('3 for IDS')
    print('0 for exit')
    opt = input('Enter Option: ')
    opt = int(opt)
    if (opt == 1):
        plot = Graph()
        plot.makeplot()
        print("\n!->>BFS")

        print("Cost", cost(plot.BFS("1,1", "15,15")))
        dispay(plot.graph, plot.BFS("1,1", "15,15"), blocked)
    if (opt == 2):
        gdfs = Graph()
        gdfs.makeplot()
        print("\n!->>DFS")

        dispay(gdfs.graph, gdfs.DFS('1,1', '15,15'), blocked)
        print("Cost", cost(gdfs.DFS('1,1', '15,15')))
    if opt == 3:

        g = Graph()
        g.makeplot()
        print("\n\n!->>IDS")
        if g.IDDFS('1,1', '15,15', 5):
            print("Target is reachable from source " + "within max depth")
        else:
            print("Target is NOT reachable from source " + "within max depth")
    if (opt == 0):
        loop = False
