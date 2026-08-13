from collections import deque

def solution(n, computers):
    q = deque()
    
    cnt = 0
    check = [0 for _ in range(n)]
    
    for i in range(n):
        # 방문 전이면 다른거 다 타면서 검색
        if (check[i] == 0):
            check[i] = 1
            cnt += 1
            q.append(i)
            # print(i)
            
            while (q):
                item = q.popleft() # 검색할 인덱스 하나가 나옴
                
                # 검색 중인 인덱스와 연결된 것 중 탐색되지 않은 노드 찾기
                for j in range(n):
                    if (check[j] == 0 and computers[item][j] == 1):
                        check[j] = 1
                        q.append(j)
    
    return cnt