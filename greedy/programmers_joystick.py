def solution(name):
    
    # 다시 풀어보기 -> 지피티 사용
    answer = 0

    # 위아래 이동
    n = len(name)
    for c in name:
        up = ord(c) - ord('A')
        down = ord('Z') - ord(c) + 1
        
        answer += min(up,down)

    # 좌우 이동
    move = n-1
    
    for i in range(n):
        next_idx = i+1
        
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
        
        # 왼쪽 -> 오른쪽
        case1 = 2 * ( n-next_idx ) + i
        
        # 오른쪽 -> 왼쪽
        case2 = 2 * i + (n - next_idx)
        
        move = min(move, case1, case2)
        
    answer += move
    
    return answer