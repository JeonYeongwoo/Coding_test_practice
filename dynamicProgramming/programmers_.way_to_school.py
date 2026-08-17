def solution(m, n, puddles):
    # dp 업데이트 조건 : dp 값이 업데이트 된 곳을 다시 건드는 경우는 최단 경로가 아님.
    #                   따라서, dp값이 업데이트 안된 곳만 갱신하면 됨.
    
    # 탐색용으로 저장
    map = [ [0 for _ in range(m+1)] for _ in range(n+1) ]
    dp = [ [0 for _ in range(m+1)] for _ in range(n+1) ]
    for p in puddles:
        y,x = p[1], p[0]
        map[y][x] = 1
    
    
    for i in range(1, m+1):
        if(map[1][i] == 1):
            break
        else:
            dp[1][i] = 1
            
    for i in range(1, n+1):
        if(map[i][1] == 1):
            break
        else:
            dp[i][1] = 1
    
    
    # 경로 개수를 저장.
    for i in range(2, n+1):
        for j in range(2, m+1):
            if(map[i][j] == 0 and dp[i][j] == 0):
                dp[i][j] = (dp[i-1][j] + dp[i][j-1] )% 1000000007
    
    return dp[n][m]