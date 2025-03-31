def input_scores(): #초기 성적 입력 함수
    students = []
    for i in range(5):
        print(f"{i + 1}번 학생의 성적을 입력하세요.\n")
        student = {}
        student['id'] = input("학번: ")
        student['name'] = input("이름: ")
        student['eng'] = int(input("영어: "))
        student['clang'] = int(input("C-언어: "))
        student['py'] = int(input("파이썬: "))
        students.append(student)
        print("\n")
    return students

def calculate_avg(students): #총점/평균 계산
    for student in students:
        student['total'] = student['eng'] + student['clang'] + student['py']
        student['avg'] = student['total'] / 3

def calculate_grade(students): #순위 계산
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
    for i in range(len(students)):
        rank = 1
        for j in range(len(students)):
            if i != j and students[i]['total'] < students[j]['total']:
                rank += 1
        students[i]['rank'] = rank

def insert_student(students): #삽입 함수. 삽입 후 다시 평균, 등수, 순위 계산
    print("\n새로운 학생 정보를 입력하세요.\n")
    student = {}
    student['id'] = input("학번: ")
    student['name'] = input("이름: ")
    student['eng'] = int(input("영어: "))
    student['clang'] = int(input("C-언어: "))
    student['py'] = int(input("파이썬: "))
    students.append(student)
    calculate_avg(students)
    calculate_grade(students)
    calculate_rank(students)
    print("학생이 추가되었습니다.\n")

def delete_student(students): #삭제 함수. 삭제 후 다시 평균, 등수, 순위 계산
    student_id = input("삭제할 학생의 학번을 입력하세요: ")
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            calculate_avg(students)
            calculate_grade(students)
            calculate_rank(students)
            print(f"{student_id} 학번의 학생이 삭제되었습니다.\n")
            return
    print("해당 학생을 찾을 수 없습니다.\n")

def sort_students(students): #정렬 함수
    students.sort(key=lambda student: student['total'], reverse=True)


def count_high_scores(students): #80점 이상 카운트 함수
    count = sum(1 for student in students if student['avg'] >= 80)
    print(f"\n평균 80점 이상인 학생 수: {count}\n")

def search_student(students): #탐색 함수
    student_id = input("찾을 학생의 학번을 입력하세요: ")
    for student in students:
        if student['id'] == student_id:
            print("\n검색 결과:")
            print(student)

def result(students): #출력 함수
    sort_students(students)
    print("\n\t\t\t성적관리 프로그램")
    print("=" * 80)
    print("\t학번\t\t이름   영어  C-언어  파이썬  총점   평균  학점  등수")
    print("=" * 80)
    for student in students:
        print(f"{student['id']}\t{student['name']}\t{student['eng']}    {student['clang']}"
              f"     {student['py']}    {student['total']}   {student['avg']:.2f}   {student['grade']}    {student['rank']}")
    count_high_scores(students)

# 실행
students = input_scores()
calculate_avg(students)
calculate_grade(students)
calculate_rank(students)
result(students)

while True: #추가 입력/삭게/종료
    word = input("삽입: insert, 삭제: delete, 종료: exit를 입력하세요: ")
    if word == 'insert':
        insert_student(students)
        result(students)
    elif word == 'delete':
        delete_student(students)
        result(students)
    elif word == 'exit':
        print("프로그램 종료")
        break
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")