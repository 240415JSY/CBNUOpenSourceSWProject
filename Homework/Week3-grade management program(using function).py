def input_scores():
    students = []
    for i in range(5):
        print(f"{i + 1}번 학생의 성적을 입력하세요.\n")
        student = {} #딕셔너리 생성. 학생 한 명의 정보를 저장함.
        student['id'] = input("학번: ")
        student['name'] = input("이름: ")
        student['eng'] = int(input("영어: "))
        student['clang'] = int(input("C-언어: "))
        student['py'] = int(input("파이썬: "))
        students.append(student) #딕셔너리의 정보를 students라는 이름의 리스트에 저장
        print("\n")
    return students

def calculate_avg(students): #평균 계산
    for student in students:
        student['total'] = student['eng'] + student['clang'] + student['py']
        student['avg'] = student['total'] / 3

def calculate_grade(students): #학점 계산
    for student in students:
        if student['avg'] >= 90:
            student['grade'] = 'A'
        elif student['avg'] >= 80:
            student['grade'] = 'B+'
        elif student['avg'] >= 70:
            student['grade'] = 'C'
        elif student['avg'] >= 60:
            student['grade'] = 'D'
        else:
            student['grade'] = 'F'

def calculate_rank(students): #등수 계산
    for i in range(5):
        rank = 1  # 1등에서 시작
        for j in range(5):
            if i != j and students[i]['total'] < students[j]['total']:  # 총점이 더 작으면
                rank += 1  # 순위 증가. 자기보다 윗 순위가 있다는 뜻이기 때문에
        students[i]['rank'] = rank  # 해당 학생에게 등수를 부여

def result(students): #\n은 줄바꿈, \t는 탭과 같은 기능
    print("\n\t\t\t성적관리 프로그램")
    print("=" * 80)
    print("\t학번\t\t이름   영어  C-언어  파이썬  총점   평균  학점  등수")
    print("=" * 80)
    for student in students:
        print(f"{student['id']}\t{student['name']}\t{student['eng']}    {student['clang']}"
              f"     {student['py']}    {student['total']}   {student['avg']:.2f}   {student['grade']}    {student['rank']}")

students = input_scores()
calculate_avg(students)
calculate_grade(students)
calculate_rank(students)
result(students)