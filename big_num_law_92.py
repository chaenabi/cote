import unittest


def get_input():
    # N, M, K = map(int, input().split())
    # numbers = list(map(int, input().split()))
    # return N, M, K, numbers
    return 5, 8, 3, [2, 4, 5, 4, 6]

class MyTestCase(unittest.TestCase):
    def big_num_law_test(self):
        # given
        n, m, k, numlist = get_input()
        numlist.sort()

        # when
        iterate = (m / (k + 1) * k) + (m % (k + 1))
        first = numlist[n - 1] * iterate
        second = numlist[n - 2] * (m - iterate)

        # then
        result = int(first + second)

        self.assertEqual(result, 46)


if __name__ == '__main__':
    unittest.main()
