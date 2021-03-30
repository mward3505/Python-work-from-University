"""Program to covert infix to postfix notation. It also can help evaluate
postfix expressions"""

from stack import Stack


def in2post(expr):
    """Converts infix to postfix notation"""
    if not isinstance(expr, str):
        raise ValueError
    precision = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}

    operator_stack = Stack()
    result_list = []
    token_list = expr.split()

    for token in token_list:
        if token.isalpha() or token.isdigit():
            result_list.append(token)
        elif token == "(":
            operator_stack.push(token)
        elif token == ")":
            if operator_stack.is_empty():
                raise SyntaxError
            top_token = operator_stack.pop()
            while top_token != "(":
                result_list.append(top_token)
                if operator_stack.is_empty():
                    raise SyntaxError
                top_token = operator_stack.pop()
        else:
            while (not operator_stack.is_empty()) \
                    and (precision[operator_stack.top()] >= precision[token]):
                result_list.append(operator_stack.pop())
            operator_stack.push(token)

    while not operator_stack.is_empty():
        result_list.append(operator_stack.pop())

    return " ".join(result_list)


def eval_postfix(expr):
    """Evaluates post fix expressions"""
    if not isinstance(expr, str):
        raise ValueError

    operand_stack = Stack()
    token_list = expr.split()

    for token in token_list:
        if token.isdigit():
            operand_stack.push(int(token))
        else:
            if operand_stack.is_empty():
                raise SyntaxError
            right_operand = operand_stack.pop()
            if operand_stack.is_empty():
                raise SyntaxError
            left_operand = operand_stack.pop()
            operand_stack.push(do_math(token, left_operand, right_operand))

    if operand_stack.is_empty():
        raise SystemError

    return operand_stack.pop()


def do_math(operator, left_operand, right_operand):
    """Helps do the math for the postfix evaluation method"""
    if operator == "+":
        result = left_operand + right_operand
    elif operator == "-":
        result = left_operand - right_operand
    elif operator == "*":
        result = left_operand * right_operand
    else:
        result = left_operand / right_operand

    return result


def main():
    """Reads a file and implements infix2postfix and evaluates the postfix"""
    file = "G:\\development\\CS2420\\projectFour\\data.txt"
    with open(file, "r") as read_file:
        contents = read_file.read().splitlines()

    for item in contents:
        print(f"infix: {item}")
        post_fix = in2post(item)
        print(f"postfix: {post_fix}")
        result = eval_postfix(post_fix)
        print(f"answer: {result}\n")


if __name__ == "__main__":
    main()
