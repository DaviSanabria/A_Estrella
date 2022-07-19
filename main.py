from Tree import tree
from Node import Node
if __name__ == '__main__':
    ListaA = [[]]
    arbol = tree()
    arbol.Insert(Node(10, "A"), None)
    arbol.Insert(Node(4, "B"), "A")
    arbol.Insert(Node(4, "C"), "A")
    arbol.Insert(Node(0, "D"), "B")
    arbol.Insert(Node(6, "E"), "B")
    arbol.Insert(Node(6, "F"), "C")
    arbol.Insert(Node(0, "G"), "C")
    arbol.Insert(Node(0, "H"), "D")
    arbol.Insert(Node(3, "I"), "D")
    arbol.Insert(Node(0, "J"), "E")
    arbol.Insert(Node(-3, "K"), "F")
    arbol.Insert(Node(-3, "L"), "G")
    arbol.Insert(Node(-4,"M"),"H")
    arbol.Insert(Node(-4, "N"), "I")
    print("#ARBOL INORDER#")
    arbol.inorder(arbol.getRoot())

    List = [["Paso"],
            ["Lista Abierta                  "],
            ["Lista Cerrada"]]

    def OrdListaA():
        global ListaA
        ListaATemp = []
        while(len(ListaA) != 0):
            y = 0
            menor = 20
            while(len(ListaA) > y):
                if(y == 0):
                    menor = y
                else:
                    if (ListaA[y][1] < ListaA[menor][1]):
                        menor = y
                y= y+1
            ListaATemp.append(ListaA[menor])
            ListaA.remove(ListaA[menor])
        ListaA = ListaATemp

    def Menor():
        global ListaA
        menor = 20
        y = 0
        while (len(ListaA) > y):
            if (y == 0):
                menor = y
            else:
                if (ListaA[y][1] < ListaA[menor][1]):
                    menor = y
            y = y + 1
        return menor
    def AEstrella():
        global ListaA
        textoA =""
        textoB =""
        i = True
        List[0].append("1")
        List[1].append(arbol.getRoot().getData()+"("+str(arbol.getRoot().getHeuristic())+")")
        List[2].append("Void")
        nodo = arbol.getRoot()
        i = 2
        #metas
        while(nodo.getData() != "M" and nodo.getData() != "N" and nodo.getData() != "J" and nodo.getData() != "K" and nodo.getData() != "L"):
            textoA = ""
            if(i ==2):
                textoB = textoB + str(nodo.getData())
            else:
                textoB = textoB +", "+str(nodo.getData())
            List[0].append(i)
            List[2].append(textoB)
            derecha = nodo.getRight()
            izquierda = nodo.getLeft()
            if(i>2):
                ListaA.append([])
            if(derecha != None and izquierda !=Node):
                ListaA[i-2].append(izquierda.getData())
                ListaA[i-2].append(izquierda.getHeuristic())
                ListaA.append([])
                ListaA[i-1].append(derecha.getData())
                ListaA[i-1].append(derecha.getHeuristic())
            elif(derecha == None and izquierda !=None):
                ListaA[i - 2].append(izquierda.getData())
                ListaA[i - 2].append(izquierda.getHeuristic())
            elif (izquierda == None and derecha != None):
                ListaA[i - 2].append(derecha.getData())
                ListaA[i - 2].append(derecha.getHeuristic())
            OrdListaA()

            u=0
            while(len(ListaA)>u):
                if(u==0):
                    textoA = textoA+str(ListaA[u][0]) +"("+str(ListaA[u][1])+")"
                else:
                    textoA = textoA +", " +str(ListaA[u][0]) + "(" + str(ListaA[u][1]) + ")"
                u = u+1
            List[1].append(textoA)
            men = Menor()
            nodo = arbol.Find(ListaA[int(men)][0])
            ListaA.remove(ListaA[int(men)])
            i = i + 1
        return nodo
    def PrintMatrix():
        j = 0
        i = 0
        z = 0
        print("####MATRIZ#####")
        while len(List[0]) > z:
            j = 0
            while len(List) > j:
                if(z == 0):
                    print("\t", List[j][i], end=" ")
                else:
                    if(j == 0):
                        while(len(str(List[j][i])) < 3):
                            List[j][i] = str(List[j][i])+" "
                    elif (j == 1):
                        while (len(str(List[j][i])) < 32):
                            List[j][i] = List[j][i] + " "
                    print("\t", List[j][i], end=" ")
                j = j + 1
            print("")
            z = z + 1
            i = i + 1
    def solutionPath(nodeS):
        camino = []
        resultado = ""
        while(nodeS.getFather() != None):
            camino.append(nodeS.getData())
            nodeS = nodeS.getFather()
        camino.append(nodeS.getData())
        y = len(camino)-1
        i = 0
        print("")
        while (y >= i):
            if(y == len(camino)-1):
                resultado = resultado+str(camino[y])
            else:
                resultado = resultado +", "+ str(camino[y])
            y = y-1
        print("Camino solución: "+ str(resultado))
    nodo = AEstrella()
    PrintMatrix()
    solutionPath(nodo)

