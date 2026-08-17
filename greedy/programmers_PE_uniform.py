def solution(n, lost, reserve):
    # greedy 문제
    # 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려주기
    # 최대한 많은 학생이 체육수업
    
    # 1. 1개씩 있는 배열 만듦
    # 2. reserve 인 인덱스 +1
    # 3. lost 인 인덱스 -1
    
    # 이후 처음부터 끝까지 가면서 0인 경우 주변에 2인 사람 있으면 빌려옴
    # (발견한 경우 바로 빌려주는게 최선)
    
    # 끝에 0 아닌 사람들 카운트
    
    students = [1 for _ in range(n+1)]
    students [0] = 0 # 0은 가짜

    for l in lost:
        students[l] -= 1
        
    for r in reserve : 
        students[r] += 1
        
    
    # print(students)
    len_s = len(students) # 6
    
    for i in range(1, len_s):
        if (students[i] == 0): 
            if (i > 0 and students[i-1] == 2):

                students[i] += 1
                students[i-1] -= 1
            elif (i < n and students[i+1] == 2):

                students[i] += 1
                students[i+1] -= 1
                
    answer= 0
    for s in students:
        if (s != 0):
            answer += 1
            
    return answer
