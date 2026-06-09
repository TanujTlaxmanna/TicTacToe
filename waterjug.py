capacity = (12, 8, 5)
x = capacity[0]
y = capacity[1]
z = capacity[2]

ans = []
memory = {}


def waterjug(states):
    a = states[0]
    b = states[1]
    c = states[2]
    
    if a == 6 and b == 6:
        ans.append(states)
        return True

    if (a, b, c) in memory:
        return False

    memory[(a, b, c)] = True  

    if a > 0:

        if a + b <= y:
            if waterjug((0, a + b, c)):
                ans.append(states)
                return True

        else:
            if waterjug((a - (y - b), y, c)):
                ans.append(states)
                return True

        if a + c <= z:
            if waterjug((0, b, a + c)):
                ans.append(states)
                return True

        else:
            if waterjug((a - (z - c), b, z)):
                ans.append(states)
                return True

    if b > 0:

        if b + a <= x:
            if waterjug((b + a, 0, c)):
                ans.append(states)
                return True

        else:
            if waterjug((x, b - (x - a), c)):
                ans.append(states)
                return True

        if b + c <= z:
            if waterjug((a, 0, b + c)):
                ans.append(states)
                return True

        else:
            if waterjug((a, b - (z - c), z)):
                ans.append(states)
                return True

    if c > 0:

        if c + a <= x:
            if waterjug((c + a, b, 0)):
                ans.append(states)
                return True

        else:
            if waterjug((x, b, c - (x - a))):
                ans.append(states)
                return True

        if c + b <= y:
            if waterjug((a, b + c, 0)):
                ans.append(states)
                return True

        else:
            if waterjug((a, y, c - (y - b))):
                ans.append(states)
                return True

    return False


initial_state = (12, 0, 0)

waterjug(initial_state)

ans.reverse()
print(ans)