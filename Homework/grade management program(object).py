 ##################

  #프로그램명: 성적 관리 프로그램

  #작성자: 소프트웨어학부 정소연

  #작성일: 2025.04.15

  #프로그램 설명: 5명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여
  #학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받고
  #총점, 평균, 학점, 등수를 계산하는 프로그램. 객체지향 프로그램으로 수정함

 ###################
  
class Student: #학생 객체 생성
    def __init__(self, student_id, name, eng, clang, py): #필요한 데이터 설정
        self.id = student_id
        self.name = name
        self.eng = eng
        self.clang = clang
        self.py = py
        self.total = 0
        self.avg = 0.0
        self.grade = ''
        self.rank = 0
        self.calculate_scores()
        
    def calculate_scores(self): #총점, 평균, 학점 계산
        self.total = self.eng + self.clang + self.py
        self.avg = self.total / 3
        self.grade = self.calculate_grade()
        
    def calculate_grade(self): #학점 기준
        if self.avg >= 90:
            return 'A'
        elif self.avg >= 80:
            return 'B+'
        elif self.avg >= 70:
            return 'C'
        elif self.avg >= 60:
            return 'D'
        else:
            return 'F'

class gradeManagement: #속성 관리 객체 생성
    def __init__(self):
        self.students = []

    def input_scores(self): #성적 입력, 등수 계산
        for i in range(5):
            print(f"{i + 1}번 학생의 성적을 입력하세요.\n")
            student_id = input("학번: ")
            name = input("이름: ")
            eng = int(input("영어: "))
            clang = int(input("C-언어: "))
            py = int(input("파이썬: "))
            self.students.append(Student(student_id, name, eng, clang, py))
            print("\n") 
        self.calculate_ranks()
            
    def calculate_ranks(self): #정렬, 등수 계산 기준
        #총점순으로 정렬
        self.students.sort(key=lambda s: s.total, reverse=True)
    
        rank = 1
        count = 1 #같은 등수를 세는 변수

        for i, student in enumerate(self.students):
            if i == 0: #같은 등수가 없으면 그대로
                student.rank = rank
            else:
                before = self.students[i - 1] 
                if student.total == before.total:
                    student.rank = rank  # 동점자 처리
                    count += 1
                else:
                   rank = rank + count  # 동점자 수만큼 건너뛰기
                   student.rank = rank
                   count = 1  # 다시 초기화

    def insert_student(self): #삽입 함수. 삽입 후 다시 평균, 등수, 순위 계산
        print("\n새로운 학생 정보를 입력하세요.\n")
        student_id = input("학번: ")
        name = input("이름: ")
        eng = int(input("영어: "))
        clang = int(input("C-언어: "))
        py = int(input("파이썬: "))
        self.students.append(Student(student_id, name, eng, clang, py))
        self.calculate_ranks()
        print("학생이 추가되었습니다.\n")

    def delete_student(self): #삭제 함수. 삭제 후 다시 평균, 등수, 순위 계산
        student_id = input("삭제할 학생의 학번을 입력하세요: ")
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                self.calculate_ranks()
                print(f"{student_id} 학번의 학생이 삭제되었습니다.\n")
                return
        print("해당 학생을 찾을 수 없습니다.\n")
        
    def search_student(self): #탐색 함수
        student_id = input("찾을 학생의 학번을 입력하세요: ")
        for student in self.students:
            if student.id == student_id:
                print("\n검색 결과:")
                print(f"학번: {student.id}, 이름: {student.name}, 영어: {student.eng}, C-언어: {student.clang}, "
                      f"파이썬: {student.py}, 총점: {student.total}, 평균: {student.avg:.2f}, "
                      f"학점: {student.grade}, 등수: {student.rank}")
                return
        print("해당 학생을 찾을 수 없습니다.\n")
        
    def count_high_scores(self): #80점 이상 카운트 함수
        count = sum(1 for s in self.students if s.avg >= 80)
        print(f"\n평균 80점 이상인 학생 수: {count}\n")

    def result(self): #출력 함수
        self.students.sort(key=lambda s: s.total, reverse=True)
        print("\n\t\t\t성적관리 프로그램")
        print("=" * 80)
        print("\t학번\t\t이름   영어  C-언어  파이썬  총점   평균  학점  등수")
        print("=" * 80)
        for s in self.students:
            print(f"{s.id}\t{s.name}\t{s.eng}    {s.clang}     {s.py}    {s.total}   {s.avg:.2f}   {s.grade}    {s.rank}")
        self.count_high_scores()
        
def main():
    manager = gradeManagement()
    manager.input_scores()
    manager.result()

    while True:
        word = input("삽입: insert, 삭제: delete, 검색: search, 종료: exit를 입력하세요: ")
        if word == 'insert':
            manager.insert_student()
            manager.result()
        elif word == 'delete':
            manager.delete_student()
            manager.result()
        elif word == 'search':
            manager.search_student()
        elif word == 'exit':
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")

if __name__ == "__main__":
    main()