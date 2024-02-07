def the_result_of_a_postfix_expression(expression):
    stack = []
    ops = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }

    tokens = re.findall(r"\d+|\S", expression)
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif token in ops:
            if len(stack) < 2:
                return False
            op2 = stack.pop()
            op1 = stack.pop()
            result = opstoken
            stack.append(result)

    return stack[0] if len(stack) == 1 else False
