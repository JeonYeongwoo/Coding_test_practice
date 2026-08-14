from collections import deque

def solution(n, edge):
    
    q = deque()

    # edge 정보 -> node 정보 변환
    for e in edge:
        e.sort()
    edge.sort()
    
    # 노드 형태로 전처리..
    node = [[]for _ in range(n+1)]
    for e in edge:
        node[e[0]].append(e[1])
        node[e[1]].append(e[0])
    # print(node)
    
    # 변수 부분
    visited = [0 for _ in range(n+1)] # 노드 방문 기록
    d = [0 for _ in range(n+1)] # distance

    # 알고리즘
    visited[1] = 1
    i = 0
    for item in node[1]:
        d[item] = 1 # 1이랑 연결: 거리 1 위치
        visited[item] = 1
        q.append(item)

    while(q):
        cur = q.popleft() 
        for item in node[cur]:
            if (visited[item] == 0):
                visited[item] = 1
                q.append(item)
                d[item] = d[cur]+1
    
    d.sort()
    i = len(d)-1
    max = d[i]
    cnt = 0

    # print(max)
    while(d[i] == max):
        cnt += 1
        i -= 1
    
    return cnt