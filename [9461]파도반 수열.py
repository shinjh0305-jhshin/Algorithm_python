import sys
Input = sys.stdin.readline
tc = int(Input())  # 테스트 케이스 개수
k = [int(Input()) for _ in range(tc)]  # 테스트 케이스 종류
dp = [0, 1, 1, 1, 2, 2]


def make_seq(target):
    for i in range(len(dp), target + 1):  # target번째 수열이 만들어 질 때 까지 계속한다
        dp.append(dp[-1] + dp[-5])
    return dp[-1]


def operate():
    ans = []
    for x in k:
        if len(dp) > x:  # 이미 해당 인덱스 값을 찾았었다
            ans.append(dp[x])
        else:  # 해당 인덱스 값을 찾은 적이 없다
            ans.append(make_seq(x))
    print(*ans, sep='\n')


operate()
