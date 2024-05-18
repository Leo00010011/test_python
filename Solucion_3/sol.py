import random

class Node:
    def __init__(self,value, parent = None) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def is_left_chld(self):
        '''
        Retorna si el nodo es hijo izquierdo de su padre
        '''
        if self.parent == None:
            return False
        if self.parent.left == None:
            return False
        return self.parent.left.value == self.value

    def __repr__(self) -> str:
        return f'<{self.value}>'
    
    def cut(self):
        '''
        Elimina todas las conexiones `hacia` el nodo
        '''
        if self.parent != None:
            if self.is_left_chld():
                self.parent.left = None
            else:
                self.parent.right = None
        
        if self.right != None:
            self.right.parent = None

        if self.left != None:
            self.left.parent = None
        

class BinaryTree:
    '''Arbol Binario de Busqueda'''
    def __init__(self, root: Node) -> None:
        self.root: Node = root

    def insert(self,value):
        node = self.get_node(value)
        if value < node.value:
            node.left = Node(value, node)
        elif value > node.value:
            node.right = Node(value, node)
        else:
            new_node = Node(value,node)
            new_node.left = node.left
            if node.left != None:
                node.left.parent = new_node
            node.left = new_node

    def get_node(self,value):
        '''Devuelve el nodo que contiene el valor, o la hoja que puede ser su padre'''
        return self.__get_node(value,None,self.root)

    def __get_node(self,value,parent: Node,node: Node):
        
        if node == None:
            return parent
        if value < node.value:
            return self.__get_node(value,node,node.left)
        elif value > node.value:
            return self.__get_node(value,node,node.right)
        return node

    def remove(self,value):
        '''elimina el nodo con value, si existe'''
        node = self.get_node(value)        
        # el nodo no está
        if node.value != value:
            return
        
        # el nodo tiene uno o ningún hijo
        if node.left == None and node.right == None:
            # print(f'ningun hijo {value}')
            node.cut()
            return
        
        if node.right == None:
            # print(f'un hijo: {value}')
            if node.parent != None:
                if node.is_left_chld():
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
            else:
                self.root = node.left
            node.left.parent = node.parent
            return
        elif node.left == None:
            # print(f'un hijo: {value}')
            if node.parent != None:
                if node.is_left_chld():
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
            else:
                self.root = node.right
            node.right.parent = node.parent
            return
        
        
        # el nodo tiene dos hijos buscar menor de los mayores del hijo derecho
        max_min = None
        # print(f'dos hijos {value}')
        for item in self.__iter(node.right):
            max_min = item
            break

        if max_min == node.right:
            max_min.parent = node.parent
            if node.parent != None:
                if node.is_left_chld():
                    node.parent.left = max_min
                else:
                    node.parent.right = max_min
            else:
                self.root = max_min 
            max_min.left = node.left
            node.left.parent = max_min
        else:
            # hooking right branch of maxmin in maxmin parent
            if max_min.parent != None:
                max_min.parent.left = max_min.right
            if max_min.right != None:
                max_min.right.parent = max_min.parent

            # hoking maxmin in node position
            if node.parent != None:    
                if node.is_left_chld():
                    node.parent.left = max_min
                else:
                    node.parent.right = max_min
            else:
                self.root = max_min
            max_min.parent = node.parent

            # left branch of node
            max_min.left = node.left

            if node.left != None:
                node.left.parent = max_min

           # right branch of node
            max_min.right = node.right

            if node.right != None:
                node.right.parent = max_min

        
    def max(self):
        return self._max(self.root)
    
    def _max(self, node):
        if node.right != None:
            return self._max(node.right)
        else:
            return node
                
    def iter(self):
        '''
        itera por los elementos de menor a mayor
        '''
        for item in self.__iter(self.root):
            yield item

    def __iter(self,node: Node):
        # DFS
        if node is None:
            return []

        for item in self.__iter(node.left):
            yield item

        yield node

        for item in self.__iter(node.right):
            yield item


    def __str__(self) -> str:
        return ','.join(self.iter())



def test(case_number,case_len, remove_number = 0):
    '''
    Test para probar la clase `BinaryTree`
    @case_number: numero de casos a probar
    @case_len: cantidad de elementos de los casos a probar
    @remove_number: cantidad de elementos a remover en el test
    '''

    # El test se basa en que si el arbol esta construido correctamente, la iteración debe dar los elementos en orden

    nums = list(range(case_len))
    for _ in range(case_number):
        samples = random.choices(nums,k = case_len)
        bt = BinaryTree(Node(samples[0]))
        for item in samples[1:]:
            bt.insert(item)
        # Prueba sin remover
        sorted_mine = list(node.value for node in bt.iter())
        # print(samples)
        samples.sort()
        if samples != sorted_mine:
            print('Sort test')
            print(samples)
            print(sorted_mine)
            print('------------------------')

        # Prueba removiendo
        for _ in range(remove_number):
            index = random.randint(0, len(samples) - 1)
            bt.remove(samples[index])
            samples.remove(samples[index])

        sorted_mine = list(node.value for node in bt.iter())
        if samples != sorted_mine:
            print('\n')
            print('Remove Test')
            print(samples)
            print(sorted_mine)
            print('------------------------')
        # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

test(3000,50,15)
        
