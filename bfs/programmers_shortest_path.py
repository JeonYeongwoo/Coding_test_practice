from collections import deque

def solution(maps):
    answer = 0
    
    x_len = len(maps[0])
    y_len = len(maps)
    
    print(y_len)
    
    # N x N 짜리 맵 생성
    check = [[0 for _ in range(x_len)] for _ in range(y_len)]
    
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    q = deque()
    q.append([0,0,1]) # x, y, 카운트
    check[0][0] = 1
    
    while (q):
        item = q.popleft()
        
        for i in range(4):
            nx = item[0] + dx[i]
            ny = item[1] + dy[i]
            
            if ( 0 <= nx <= x_len-1 and 0 <= ny <= y_len-1 
                and check[ny][nx] == 0 and maps[ny][nx] == 1):
                
                print(nx, ny, check[ny][nx])
                
                # 끝지점이면 이전 cnt +1 리턴
                if ( nx == x_len-1 and ny == y_len-1):
                    return item[2] + 1
                else : 
                    check[ny][nx] = 1
                    q.append([nx,ny, item[2] + 1])
    
    # 못찾은경우
    return -1