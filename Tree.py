from Node import Node

class tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, root):
        self.root = root
    #preOrder
    def preorder(self, node, sNode):
        if node:
            if(node.data == sNode):
                return node
            r = self.preorder(node.getLeft(), sNode)
            if(r != None):
                return r
            r = self.preorder(node.getRight(), sNode)
            if (r != None):
                return r
    #Find:
    def Find(self, nodeData):
        if(self.root != None):
            r = self.preorder(self.root, nodeData)
            return r
        else:
            print("rootless")
    #Insert
    def Insert(self, node, father):
        if(father != None):
            r = self.Find(father)
            if(r != None):
                if(r.left == None):
                    node.setFather(r)
                    r.setLeft(node)
                elif (r.right == None):
                    node.setFather(r)
                    r.setRight(node)
                elif(r.getLeft() != None and r.getRight() != None):
                    return print("Father Full")
                else:
                    while (r.getFather() != None):
                        r = r.getFather()
                    self.setRoot(r)
            else:
                print("Father not found")
        else:
            if(self.root == None):
                self.root = node
            else:
                print("root already defined")
    #printInorder
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)
