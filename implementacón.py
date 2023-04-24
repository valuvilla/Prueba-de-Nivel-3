class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, question, superhero, curr=None):
        if self.root is None:
            self.root = Node(question)
            self.root.left = Node(superhero)
            return

        if curr is None:
            curr = self.root

        answer = input(curr.data + " (s/n): ").lower()
        if answer == 's':
            if curr.left is None:
                curr.left = Node(superhero)
                return
            self.insert(question, superhero, curr.left)
        elif answer == 'n':
            if curr.right is None:
                curr.right = Node(superhero)
                return
            self.insert(question, superhero, curr.right)
        else:
            print("Por favor, responde con 's' o 'n'.")
            self.insert(question, superhero, curr)

    def search(self, question, curr=None):
        if self.root is None:
            return None

        if curr is None:
            curr = self.root

        answer = input(curr.data + " (s/n): ").lower()
        if answer == 's':
            if curr.left is None:
                return None
            elif curr.left.data in superheroes:
                return curr.left.data
            else:
                return self.search(question, curr.left)
        elif answer == 'n':
            if curr.right is None:
                return None
            elif curr.right.data in superheroes:
                return curr.right.data
            else:
                return self.search(question, curr.right)
        else:
            print("Por favor, responde con 's' o 'n'.")
            return self.search(question, curr)

superheroes = ['Thor', 'Hulk', 'Khan', 'Ant-Man', 'Capitán América', 'Capitana Marvel', 'The Winter Soldier', 'Nick Fury']
tree = BinaryTree()

# Insertar nodos
tree.insert("¿Necesitas destruir un ejército completo?", "Thor")
tree.insert("¿Necesitas destruir una gran cantidad de cosas?", "Hulk")
tree.insert("¿Necesitas realizar una misión intergaláctica en equipo?", "Khan")
tree.insert("¿Necesitas recuperar algo sin ser detectado?", "Ant-Man")
tree.insert("¿Necesitas infiltrarte con personas del lugar?", "The Winter Soldier")
tree.insert("¿Necesitas tomar una decisión rápida y moverte rápidamente?", "Nick Fury")
tree.insert("¿Necesitas una persona para varias misiones?", "Khan")
tree.insert("¿Necesitas viajar por las distintas galaxias?", "Capitana Marvel")
tree.insert("¿Necesitas una persona para comandar misiones de defensa y de recuperación?", "Capitán América")


