class Node:
    def __init__(self, heuristic, data):
        self.left = None
        self.right = None
        self.father = None
        self.heuristic = heuristic
        self.data = data
    #Get methods
    def getLeft(self):
        return self.left;
    def getRight(self):
        return self.right;
    def getFather(self):
        return self.father;
    def getHeuristic(self):
        return self.heuristic;
    def getData(self):
        return self.data;
    # Set methods
    def setLeft(self, left):
        self.left = left;
    def setRight(self, right):
        self.right = right;
    def setFather(self, father):
        self.father = father;
    def setHeuristic(self, heuristic):
        self.heuristic = heuristic;
    def setData(self, data):
        self.data = data;

