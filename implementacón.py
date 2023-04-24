class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if node is None:
            return Node(data)
        if data.lower() == 'yes':
            node.left = self.insert(node.left, input("¿Cuál es la pregunta para el subarbol izquierdo? "))
        elif data.lower() == 'no':
            node.right = self.insert(node.right, input("¿Cuál es la pregunta para el subarbol derecho? "))
        else:
            print("Superhéroe encontrado: " + data)
            return Node(data)

    def search(self, node, data):
        if node is None:
            return None
        if node.data.lower() == data.lower():
            return node
        elif data.lower() == 'yes':
            return self.search(node.left, input(node.data + " (s/n) "))
        elif data.lower() == 'no':
            return self.search(node.right, input(node.data + " (s/n) "))

tree = Tree()
tree.root = Node(input("¿Cuál es la pregunta inicial? "))
tree.insert(tree.root, input("¿Cuál es la respuesta para el subarbol izquierdo? "))
tree.insert(tree.root, input("¿Cuál es la respuesta para el subarbol derecho? "))

hero = tree.search(tree.root, input("¿Cuál es tu pregunta? (Escribe 'yes' o 'no') "))

if hero:
    print("Superhéroe encontrado: " + hero.data)
else:
    print("No se encontró ningún superhéroe que coincida con las respuestas dadas.")

