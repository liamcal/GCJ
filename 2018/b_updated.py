'''
TroubleSort(L): // L is a 0-indexed list of integers
    let done := false
    while not done:
      done = true
      for i := 0; i < len(L)-2; i++:
        if L[i] > L[i+2]:
          done = false
          reverse the sublist from L[i] to L[i+2], inclusive
'''

def troublesort(l):
    done = False
    while not done:
        done = True
        for i in range(len(l)-2):
            if l[i] > l[i+2]:
                done = False
                l = l[:i] + list(reversed(l[i:i+3])) + l[i+3:]
    return l

def interleave_sort(l):
    a, b = sorted(l[::2]), sorted(l[1::2])
    c = [None] * (len(a) + len(b))
    c[::2], c[1::2] = a, b
    return c

def evaluate_sort(sorted_l):
    for i in range(len(sorted_l)-1):
        if sorted_l[i] > sorted_l[i+1]:
            return i
    return "OK"

def solve_case(i, case):
    return "Case #{}: {}".format(i + 1, evaluate_sort(interleave_sort(case)))

TEST_CASES = [
    ("5 6 8 4 3", "Case #1: OK"),
    ("8 9 7", "Case #2: 1")
]

def assert_same_result(f1, f2, trials):
    assert(all(f1(t) == f2(t) for t in trials))

def assert_cases(cases):
    assert(all(solve_case(i, format_case(case[0])) == case[1] for i, case in enumerate(cases)))

def format_case(case):
    return list(map(int, case.split()))

if __name__ == '__main__':
    # assert_cases(TEST_CASES)
    # assert_same_result(troublesort, interleave_sort, [case[0].split() for case in TEST_CASES ])
    t = int(input())
    for c in range(t):
        n = input()
        v = format_case(input)
        print(solve_case(c, v))
