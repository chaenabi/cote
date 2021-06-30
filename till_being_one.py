import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        # given
        n, k = 25, 5
        count = 0

        # when
        # 입력값 n이 17이고, k가 4일때
        # n을 1로 만들 수 있는 최소 연산 갯수를 구하세요.
        # 단 연산은
        # 1. n에서 1을 뺀다.
        # 2. n을 k로 나눈 나머지가 0이면 n를 k로 나눈다.
        # 밖에 사용할 수 없어요.
        while n != 1:
            if n % k != 0:   n -= 1
            else         :   n /= k
            count += 1


        # then
        self.assertEqual(count, 2) # failed: cuz count is 0


if __name__ == '__main__':
    unittest.main()
