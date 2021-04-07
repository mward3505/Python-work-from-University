import string


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def infix2postfix(expression):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    operator_stack = Stack()
    result_list = []
    token_list = expression.split()

    for token in token_list:
        if token.isalpha() or token.isdigit():
            result_list.append(token)
        elif token == "(":
            operator_stack.push(token)
        elif token == ")":
            top_token = operator_stack.pop()
            while top_token != "(":
                result_list.append(top_token)
                top_token = operator_stack.pop()
        else:
            while (not operator_stack.is_empty()) and (prec[operator_stack.peek()] >= prec[token]):
                result_list.append(operator_stack.pop())
            operator_stack.push(token)

    while not operator_stack.is_empty():
        result_list.append(operator_stack.pop())

    return " ".join(result_list)


def postfix_eval(expression):
    operand_stack = Stack()
    token_list = expression.split()

    for token in token_list:
        if token.isdigit():
            operand_stack.push(int(token))
        else:
            right_operand = operand_stack.pop()
            left_operand = operand_stack.pop()
            operand_stack.push(do_math(token, left_operand, right_operand))

    return operand_stack.pop()


def do_math(operator, left_operand, right_operand):
    if operator == "+":
        return left_operand + right_operand
    elif operator == "-":
        return left_operand - right_operand
    elif operator == "*":
        return left_operand * right_operand
    else:
        return left_operand / right_operand


def main():
    expression = infix2postfix(" 8*5-3+2-7-3 ")
    print(postfix_eval(expression))


if __name__ == "__main__":
    main()
