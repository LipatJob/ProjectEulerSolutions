n = int(input("Enter side")) + 1
dp = [[0 for x in range(n)] for y in range(n)]

dp[0][0] = 1;

for x in range(n):
    for y in range(n):
        if x == 0 and y == 0:
            continue;
        prev1 = 0
        prev2 = 0
        if x - 1 >= 0:
            prev1 = dp[x - 1][y]
        if y - 1 >= 0:
            prev2 = dp[x][y - 1]
        dp[x][y] = prev1 + prev2

print(dp[n-1][n-1])
