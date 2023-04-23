class Node:
    def __init__(self, question=None, left=None, right=None):
        self.question = question
        self.left = left
        self.right = right

def add_node(root, question, left=None, right=None):
    new_node = Node(question, left, right)
    if root is None:
        root = new_node
    else:
        current_node = root
        while current_node is not None:
            last_node = current_node
            if question.lower() < current_node.question.lower():
                current_node = current_node.left
            else:
                current_node = current_node.right
        if question.lower() < last_node.question.lower():
            last_node.left = new_node
        else:
            last_node.right = new_node

def search_node(root, question):
    current_node = root
    while current_node is not None:
        if question.lower() == current_node.question.lower():
            return current_node
        elif question.lower() < current_node.question.lower():
            current_node = current_node.left
        else:
            current_node = current_node.right
    return None

# Crear el árbol binario
root = Node("¿El superhéroe es adecuado para misiones de destrucción?")
add_node(root, "¿Tiene el poder para destruir ejércitos completos?", Node("Thor"))
add_node(root, "¿Es una excelente opción para misiones de destrucción?", Node("Hulk"))
add_node(root, "¿Es ideal para misiones intergalácticas en equipo?", Node("Khan"))
add_node(root, "¿Es excelente en misiones de recuperación donde se requiere no ser detectado?", Node("Ant-Man"))
add_node(root, "¿Es un supersoldado de ética incorruptible ideal para comandar misiones de defensa y de recuperación?", Node("Capitán América"))
add_node(root, "¿Es muy poderosa y puede viajar por las distintas galaxias?", Node("Capitana Marvel"))
add_node(root, "¿Es muy hábil y puede ser útil para varias misiones?", Node("Khan"))
add_node(root, "¿Es la persona indicada para misiones de recuperación donde requiera infiltrarse con personas del lugar?", Node("The Winter Soldier"))
add_node(root, "¿Es la opción más lógica para elegir la próxima acción y moverse rápidamente de un lugar a otro?", Node("Nick Fury"))

# Buscar un nodo en el árbol binario
search_node(root, "¿Es una excelente opción para misiones de destrucción?")

# Salida
print(search_node(root, "¿Es una excelente opción para misiones de destrucción?").left.question)