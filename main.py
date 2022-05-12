import math

from termcolor import cprint

INFINITY = 10000
loop = True
blocked = ['6,2', '8,2', '9,2', '10,2', '13,1', '13,2', '14,2', '8,3', '9,3',
           '10,3', '3,4', '4,4', '3,5', '4,5', '6,5', '7,5', '8,5', '11,5', '13,5', '6,6', '7,6', '8,6', '11,6', '13,6',
           '6,7', '7,7', '8,7',
           '9,7', '11,7', '1,8', '2,8', '6,8', '7,8', '8,8', '9,8', '11,8', '6,9',
           '7,9', '8,9', '11,9', '13,9', '14,9', '11,10', '13,10', '14,10', '1,11',
           '2,11', '3,11', '6,11', '7,11', '8,11', '9,11', '1,12', '2,12', '3,12',
           '6,12', '7,12', '8,12', '9,12', '10,14', '11,14', '13,14', '1,15', '2,15',
           '3,15', '4,15', '5,15', '6,15', '10,15', '11,15', '13,15']


class Node:
    def __init__(self):
        self.state = 0
        self.cost = 0
        self.parent = 0
        self.goal = 0

    def __init__(self, state, cost, parent, goal):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.goal = goal

    def __lt__(self, other):
        return self.cost < other.cost

    def __gt__(self, other):
        return self.cost > other.cost

    def __eq__(self, other):
        return self.state == other.state


class BFSNode:
    def __init__(self):
        self.state = 0
        self.cost = 0

        self.parent = 0
        self.goal = 0

    def __init__(self, state, cost, parent, goal):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.goal = goal

    def __lt__(self, other):
        return Euclidean_distance(self.state, self.goal) < Euclidean_distance(other.state, other.goal)

    def __eq__(self, other):
        return self.state == other.state


def solution(node):
    if node.parent is None:
        return [node]
    else:
        finalPath = solution(node.parent)
        finalPath.append(node)

        return finalPath


class Graph:

    def __init__(self):
        self.solution = []
        self.last = []
        self.graph = {}
        self.NoOfVertices = 0

    def isComplete(self):
        for n in self.graph:
            if self.graph.get(n) != self.graph.keys():
                print("incomplete Graph")
                return 0
        print("Complete Graph")
        return 0

    def Euclidean_distance(self, start, end):
        spList = start.split(',')

        Ver = int(spList[0])
        Hor = int(spList[1])

        spList1 = end.split(',')
        Ver1 = int(spList1[0])
        Hor1 = int(spList1[1])
        dist = math.sqrt((pow(abs(Ver - Ver1), 2)) + (pow(abs(Hor - Hor1), 2)))
        return dist

    def RBFS(self, node, goal):
        if goal in blocked:
            print('Goal is Blocked can not react destination')
            return 0
        self.solution.append(node)

        if (self.Euclidean_distance(node.state, goal) == 0):
            self.solution.append(node)
            return 0

        if not self.graph[node.state]:
            return INFINITY

        nodeChildren = []
        print("Expanding:", node.state, "childs -->", end=' ')
        for ch in self.graph[node.state]:
            print(ch.state, end=' ')
            nodeChildren.append(ch)
        print()
        for i in range(2):
            nodeChildren.sort(key=lambda nod: self.Euclidean_distance(nod.state, goal))

            if len(nodeChildren) == 0:
                return INFINITY
            candidate = Node('', 0, '', '')
            while candidate.state == '':
                candidate = nodeChildren[0]
                if candidate.state in blocked:
                    candidate.state = ''
                nodeChildren.pop(0)

            visitCand = True
            rtnSet = INFINITY

            for prev in self.solution:
                if (candidate == prev):
                    visitCand = False

            if (visitCand):
                for ch in nodeChildren:
                    self.last.append(ch)
                    # if candidate.state not in blocked:
                    rtnSet = self.RBFS(candidate, goal)
                    if (rtnSet == 0):
                        return 0

    def checkInVisited(self, node, visited):
        for v in visited:
            if node.state == v.state and node.parent == v.parent:
                return True
        return False

    def BFS(self, start, goal):
        if goal in blocked:
            print('Goal is Blocked can not react destination')
            return 0
        node = BFSNode(start, 0, None, goal)
        priorityQue = [node]
        visited = []
        while True:
            if len(priorityQue) == 0:
                print("Failure")
                return False

            node = priorityQue.pop(0)

            if goal == node.state:
                return solution(node)

            visited.append(node.state)
            print("Expanding :", node.state, " childs: ", end=' ')
            for action in self.graph.get(node.state):
                print(action.state, end=' ')

                if action.state not in blocked:
                    child = BFSNode(action.state, node.cost + action.cost, node, goal)
                    if (not child.state in visited):
                        priorityQue.append(child)
                        priorityQue.sort()
            print()

    def A_search(self, start, goal):
        if goal in blocked:
            print('Goal is Blocked can not react destination')
            return 0
        node = Node(start, 0, None, goal)
        priorityQue = [node]
        visited = []

        while True:
            if len(priorityQue) == 0:
                print("Failure")
                return False

            node = priorityQue.pop(0)

            if goal == node.state:
                return solution(node)

            visited.append(node.state)
            print("Expanding :", node.state, " child: ", end=' ')
            for action in self.graph.get(node.state):
                print(action.state, end=' ')
                if action.state not in blocked:
                    child = Node(action.state, node.cost + action.cost + Euclidean_distance(node.state, goal), node,
                                 goal)
                    if child.state not in visited:
                        priorityQue.append(child)
                        priorityQue.sort()
            print()

    def add_vertex(self, newVertex):

        if newVertex in self.graph:
            print("Vertex ", newVertex, " already exists.")
        else:
            self.NoOfVertices = self.NoOfVertices + 1
            self.graph[newVertex] = []

    def add_edge(self, vertex1, vertex2, cost):
        node1 = Node(vertex1, cost, None, None)
        node2 = Node(vertex2, cost, None, None)
        if vertex1 not in self.graph:
            print("Vertex1 ", vertex1, " not exist.")

        elif vertex2 not in self.graph:
            print("Vertex2", vertex2, "not exist.")

        else:
            if len(self.graph[vertex1]) != 0:
                if node2 not in self.graph[vertex1]:
                    self.graph[vertex1].append(node2)
            else:
                self.graph[vertex1].append(node2)

            # if len(self.graph[vertex2]) != 0:
            #     if node1 not in self.graph[vertex2]:
            #         self.graph[vertex2].append(node1)
            # else:
            #     self.graph[vertex2].append(node1)

    def display(self):
        for key in self.graph:
            print(key, ":[", end='')
            for node in self.graph[key]:
                print("{", node.state, ":", node.cost, '},', end='')
            print('],')

    # def display(self):
    #     print("\033[91m {}\033[00m".format("  Graph"))
    #     print("\033[91m {}\033[00m".format(self.graph))

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
                # self.add_edge(vertex, newVertex1, 2)

            else:
                newVertex1 = 0
            if Hor > 1:
                newVertex2 = str(Ver) + ',' + str(Hor - 1)
                # self.add_edge(vertex, newVertex2, 2)

            else:
                newVertex2 = 0
            if Ver > 1 and Hor > 1:
                newVertex3 = str(Ver - 1) + "," + str(Hor - 1)
                # self.add_edge(vertex, newVertex3, 3)

            else:
                newVertex3 = 0
            if Ver < 15 and Hor < 15:
                newVertex4 = str(Ver + 1) + "," + str(Hor + 1)
                self.add_edge(vertex, newVertex4, 3)

            else:
                newVertex4 = 0
            if Ver < 15:
                newVertex5 = str(Ver + 1) + "," + str(Hor)
                self.add_edge(vertex, newVertex5, 2)

            else:
                newVertex5 = 0
            if Hor < 15:
                newVertex6 = str(Ver) + "," + str(Hor + 1)
                self.add_edge(vertex, newVertex6, 2)

            else:
                newVertex6 = 0
                # print(vertex,"-->",newVertex1,newVertex2,newVertex3,newVertex4,newVertex5,newVertex6)
            if Ver < 15 and Hor > 1:
                newVertex7 = str(Ver + 1) + "," + str(Hor - 1)
                # self.add_edge(vertex, newVertex7, 3)

            else:
                newVertex7 = 0
            if Ver > 1 and Hor < 15:
                newVertex8 = str(Ver - 1) + "," + str(Hor + 1)
                # self.add_edge(vertex, newVertex8, 3)

            else:
                newVertex8 = 0

        # self.display()


def cost(path, graph):
    cos = 0

    for i in range(1, len(path)):

        v1 = path[i - 1].state
        v2 = path[i].state
        v1L = v1.split(',')
        V1ver = int(v1L[0])
        V1Hor = int(v1L[1])

        v2L = v2.split(',')
        V2ver = int(v2L[0])
        V2Hor = int(v2L[1])

        difV = V1ver - V2ver
        difH = V1Hor - V2Hor
        if (difV == 0 or difH == 0):

            cos = cos + 2
        else:
            # print(v1,v2,cos)

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
            elif Node(vertex, 0, None, None) in sol:
                cprint('1', 'red', end='  ')
            else:
                print("0", end='  ')

        print()


def displaySol(self):
    for node in self:
        print("{", node.state, ":", node.cost, '},')

    print()
    return 0


def Euclidean_distance(start, end):
    spList = start.split(',')
    Ver = int(spList[0])
    Hor = int(spList[1])

    spList1 = end.split(',')
    Ver1 = int(spList1[0])
    Hor1 = int(spList1[1])

    dist = math.sqrt((pow(abs(Ver - Ver1), 2)) + (pow(abs(Hor - Hor1), 2)))
    # print(start,end,dist)
    return int(dist)


def displaySol2(self, goal):
    cost = 0
    for node in self:
        cost = cost + node.cost
        print("{", node.state, ":", node.cost, '+', Euclidean_distance(node.state, goal), '=',
              node.cost + Euclidean_distance(node.state, goal), '},', end='')
        print('],')
    print()
    return 0


g = Graph()
g.makeplot()

start = input("Enter Start Point : ")
end = input("Enter End   Point : ")
v1 = start
v2 = end
v1L = v1.split(',')
V1ver = int(v1L[0])
V1Hor = int(v1L[1])
v2L = v2.split(',')
V2ver = int(v2L[0])
V2Hor = int(v2L[1])
difV = V1ver - V2ver
difH = V1Hor - V2Hor
if (difV > 0 or difH > 0):
    print("Moving Left and Down not allowed.")
    exit()

print("Press 1 for BFS SEARCH")
print("Press 2 for A*  SEARCH")
print("Press 3 for RBFS  SEARCH")

op = input("Enter YourChoice:_")
if op == '1':
    sol = g.BFS(start, end)
    print("\n--------->Solution Path<---------\n")
    displaySol(sol)
    print("\n--------->Solution GRID<---------\n")

    dispay(g.graph, sol, blocked)
    print("\nCost: ", cost(sol, g.graph))

elif op == '2':
    sol = g.A_search(start, end)
    print("\n--------->Solution Path<---------\n")
    displaySol2(sol, end)
    print("\n--------->Solution GRID<---------\n")

    dispay(g.graph, sol, blocked)
    print("\nCost: ", cost(sol, g.graph))

elif op == '3':

    g.RBFS(Node(start, 0, None, end), end)
    print("\n--------->Solution Path<---------\n")
    displaySol(g.solution)
    print("\n--------->Solution GRID<---------\n")

    dispay(g.graph, g.solution, blocked)
    print("\nCost: ", cost(g.solution, g.graph))
