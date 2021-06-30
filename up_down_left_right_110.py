import unittest

# working as clock: arrow key with (dx dy) must be mapped each other (example: UP is mapping with (-1, 0))
arrow_key = ['U', 'R', 'D', 'L']
dx = ( -1, 0, 1, 0 )
dy = ( 0, 1, 0, -1 )

def get_input():
    # N = int(input()) # expect 5
    # command_list = list(input().split()) # expect value like R R R U D D
    return 5, ['R', 'R', 'R', 'R', 'R', 'R', 'U', 'D', 'U', 'D', 'D', 'L']

def solve():
    n, commands = get_input()
    x = y = 1
    for command in commands:
        for i in range(len(arrow_key)):
            if command == arrow_key[i]:
                nx = x + dx[i]
                ny = y + dy[i]

                if 1 <= nx <= n and 1 <= ny <= n:
                    x, y = nx, ny
    return x, y

class Test(unittest.TestCase):
    def test_solve(self):
        x, y = solve()
        self.assertEqual(x, 3)
        self.assertEqual(y, 4)

if __name__ == '__main__':
    unittest.main()