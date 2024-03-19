def pattern(n, G):
    if len(n) <= 1:
        return False
    stack = [0] * len(n)
    top = -1

    for i in n:
        if G == 1:
            if int(i) == 1:
                top += 1
                stack[top] = 1
            elif int(i) == 0:
                if top == -1 or stack[top] != 1:
                    return False
                else:
                    top -= 1
            else:
                return False

        elif G == 2:
            if int(i) == 0:
                top += 1
                stack[top] = 0
            elif int(i) == 1:
                if top == -1 or stack[top] != 0:
                    return False
                else:
                    top -= 1
            elif int(i) == 2:
                top += 1
                stack[top] = 2
            elif int(i) == 3:
                if top == -1 or stack[top] != 2:
                    return False
                else:
                    top -= 1
            else:
                return False

    return top == -1
# G can be 1 or 2
print(pattern("00112233", 2))