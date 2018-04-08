def evaluate_damage(command):
    damage = 0
    strength = 1
    for c in command:
        if c == 'S':
            damage += strength
        elif c == 'C':
            strength *= 2
        else:
            raise ValueError('Invalid Character: {}'.format(c))
    return damage

def reduce_damage(command):
    i = command.rfind('CS')
    if i == -1:
        return command
    return command[:i] + 'SC' + command[i+2:]

def hack(threshold, command):
    threshold = int(threshold)
    dmg = evaluate_damage(command)
    hacks = 0
    while dmg > threshold:
        new_command = reduce_damage(command)
        if new_command == command:
            return "IMPOSSIBLE"
        else:
            command = new_command
            hacks += 1
            dmg = evaluate_damage(command)
    return hacks

TEST_CASES = [
    ("1 CS", "Case #1: 1"),
    ("2 CS", "Case #2: 0"),
    ("1 SS", "Case #3: IMPOSSIBLE"),
    ("6 SCCSSC", "Case #4: 2"),
    ("2 CC", "Case #5: 0"),
    ("3 CSCSS", "Case #6: 5")
]

def assert_cases(cases):
    assert(all(solve_case(i, case[0]) == case[1] for i, case in enumerate(cases)))

def solve_case(i, case):
    return "Case #{}: {}".format(i+1, hack(*case.split()))

if __name__ == '__main__':
    #assert_cases(TEST_CASES)
    t = int(input())
    for i in range(t):
        print(solve_case(i,input()))
