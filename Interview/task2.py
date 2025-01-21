from task1 import Stack

def is_balanced(brackets_string):
    stack = Stack()
    brackets_dict = {')': '(', ']': '[', '}': '{'}

    for bracket in brackets_string:
        if bracket in '([{':
            stack.push(bracket)
        elif bracket in ')]}':
            if stack.is_empty():
                return False
            if stack.pop() != brackets_dict[bracket]:
                return False

    return stack.is_empty()


def check_balance(brackets_string):
    if is_balanced(brackets_string):
        return "Сбалансированно"
    return "Несбалансированно"


# Примеры использования:
print(check_balance("(((([{}]))))"))
print(check_balance("[([])((([[[]]])))]{()}"))
print(check_balance("{{[()]}}"))
print(check_balance("}{"))
print(check_balance("{{[(])]}}"))  
print(check_balance("[[{())}]"))