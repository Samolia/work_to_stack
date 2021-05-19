from .class_stack import Stack


stack = Stack()


def is_balanced_sequence(sequence: str):
    paired_brackets = ['()', '[]', '{}']
    for element in sequence:
        if element in '([{':
            stack.push(element)
        elif element in ')]}':
            if stack.is_empty():
                return False
            else:
                if (stack.peek() + element) in paired_brackets:
                    stack.pop()
                else:
                    return False
    if stack.is_empty():
        return True
    else:
        return False
