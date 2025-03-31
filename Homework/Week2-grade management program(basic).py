#학점 계산 프로그램

students = [] # 리스트 초기화
for i in range(5):
    print(f"{i + 1}번 학생의 성적을 입력하세요.")
    eng = int(input("영어: "))
    clang = int(input("C언어: "))
    py = int(input("파이썬: "))
    
    total = eng + clang + py # 총점: 한 학생의 시험 총점
    avg = total / 3
    
    if avg >= 90:
        grade = 'A'
    elif avg >= 80:
        grade = 'B'
    elif avg >= 70:
        grade = 'C'
    elif avg >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    students.append({ # 구한 각각의 총점, 평균, 학점을 리스트에 저장한다
        'total': total,
        'avg': avg,
        'grade': grade,
    })

for i in range(5):
    rank = 1  # 1등에서 시작
    for j in range(5):
        if i != j and students[i]['total'] < students[j]['total']:  # 총점이 더 작으면
            rank += 1  # 순위 증가. 자기보다 윗 순위가 있다는 뜻이기 때문에
    students[i]['rank'] = rank  # 해당 학생에게 등수를 부여


for i in range(5):
    print(f"{i + 1}번 학생의 총점: {students[i]['total']} 평균: {students[i]['avg']:.2f} 학점: {students[i]['grade']} 등수: {students[i]['rank']}")
