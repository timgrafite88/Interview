
# 1
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Пустой стэк")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Пустой стэк")

    def size(self):
        return len(self.items)

# 2
def is_balanced(string):
    stack = Stack()
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in bracket_map.values():
            stack.push(char)
        elif char in bracket_map.keys():
            if stack.is_empty() or stack.pop() != bracket_map[char]:
                return "Несбалансированно"

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"

# Проверка работы функции
if __name__ == '__main__':
    print(is_balanced('(((([{}]))))'))
    print(is_balanced('[([])((([[[]]])))]{()}'))
    print(is_balanced('{{[(])]}}'))