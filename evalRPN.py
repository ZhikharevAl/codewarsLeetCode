def evalRPN(self, tokens):
        stack = []
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: y - x,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(float(y) / x),
        }

        for token in tokens:
            if token in operations:
                stack.append(operations[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))

        return stack[0]
