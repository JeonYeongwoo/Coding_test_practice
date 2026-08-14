def solution(N, number):
    answer = 0
    dp = [[] for _ in range(9)]
    dp[1].append(N)
    
    dp[2].append( int(str(N)*2) )
    dp[2].append( N+N )
    dp[2].append( N-N )
    dp[2].append( N*N )
    dp[2].append( N//N )

    for i in range(3,9):
        # dp[2][0] ~ dp[2][끝] 까지 각각 dp[1][0]~ dp[끝] 까지 +-*//
        dp[i].append(int(str(N)*i))
        dp[i-1].sort()
        for j in range(1,i):
            for item_cur in dp[i-j]:
                for item_prev in dp[j]:
                    if (item_cur+item_prev not in dp[i]):
                        dp[i].append(item_cur+item_prev)
                    if (item_cur*item_prev not in dp[i]):
                        dp[i].append(item_cur*item_prev)
                    if item_prev != 0 and item_cur//item_prev not in dp[i]:
                        dp[i].append(item_cur//item_prev)
                    if item_cur-item_prev not in dp[i]:
                        dp[i].append(item_cur-item_prev)

    for i in range(1,9):
        if number in dp[i]:
            return i
            
    return -1