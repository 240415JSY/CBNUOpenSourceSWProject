###################

  #프로그램명: 성적 관리 프로그램

  #작성자: 소프트웨어학부 정소연

  #작성일: 2025.06.11

  #프로그램 설명: n명의 학생의 세개의 교과목 (영어, C-언어, 파이썬)에 대하여
  #학번, 이름, 영어점수, C-언어 점수, 파이썬 점수를 입력받고
  #총점, 평균, 학점, 등수, 80점 이상 학생 수를 계산하는 프로그램.
  #객체지향 프로그램으로 구현.
  #sqlite3와 연동함. 

####################
# sqlite3 연동
import sqlite3

# ===============================
# 학생 클래스(Student)
# 학생의 기본 정보, 성적, 성적 계산(총점, 평균, 학점, 등수 초기값) 포함
# ===============================
class Student:
    def __init__(self, student_id, name, eng, clang, py):
        self.id = student_id
        self.name = name
        self.eng = eng
        self.clang = clang
        self.py = py
        self.total = eng + clang + py
        self.avg = self.total / 3
        self.grade = self.calculate_grade()
        self.rank = 0
        
    def calculate_grade(self):
        if self.avg >= 90:
            return 'A'
        elif self.avg >= 80:
            return 'B'
        elif self.avg >= 70:
            return 'C'
        elif self.avg >= 60:
            return 'D'
        else:
            return 'F'

# ===============================
# 성적 관리 클래스(GradeManagement)
# DB 생성 및 연결, 삽입/삭제/검색/정렬/출력 등의 기능을 포함
# ===============================
class GradeManagement:
    def __init__(self, db_name='gradeManagement.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()
    
    # 학생 테이블 생성
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT,
            eng INTEGER,
            clang INTEGER,
            py INTEGER,
            total INTEGER,
            avg REAL,
            grade TEXT,
            rank INTEGER
        )
        ''')
        self.conn.commit()
        
    # 학생 데이터 DB에 삽입/갱신
    # 각 ?는 값이 들어갈 자리, execute() 함수의 두 번째 인자인 튜플에 있는 값들이
    # 차례대로 첫 번째 ?부터 마지막 ?까지 자동으로 대입된다.
    def insert_student_db(self, student):
        self.cursor.execute('''
        INSERT OR REPLACE INTO students (id, name, eng, clang, py, total, avg, grade, rank)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (student.id, student.name, student.eng, student.clang, student.py,
              student.total, student.avg, student.grade, student.rank))
        self.conn.commit()
    
    # DB에서 모든 학생 정보 불러오기
    def load_students(self):
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()
        students = []
        for row in rows:
            s = Student(row[0], row[1], row[2], row[3], row[4])
            s.total = row[5]
            s.avg = row[6]
            s.grade = row[7]
            s.rank = row[8]
            students.append(s)
        return students
    
    # 등수 계산, DB 갱신
    def calculate_ranks(self):
        students = self.load_students()
        students.sort(key=lambda s: s.total, reverse=True)
        rank = 1
        count = 1
        for i, student in enumerate(students):
            if i == 0:
                student.rank = rank
            else:
                before = students[i - 1]
                if student.total == before.total:
                    student.rank = rank
                    count += 1
                else:
                    rank += count
                    student.rank = rank
                    count = 1
            # DB 갱신
            self.insert_student_db(student)
    
    # 학생 점수 입력
    def input_scores(self):
        n = int(input("입력할 학생 수를 입력하세요: "))
        for i in range(n):
            print(f"{i + 1}번 학생의 성적을 입력하세요.\n")
            student_id = input("학번: ")
            name = input("이름: ")
            eng = int(input("영어: "))
            clang = int(input("C-언어: "))
            py = int(input("파이썬: "))
            student = Student(student_id, name, eng, clang, py)
            # DB 갱신
            self.insert_student_db(student)
            print("\n")
        # DB 갱신
        self.calculate_ranks()
    
    # 학생 추가(삽입)
    def insert_student(self):
        print("\n새로운 학생 정보를 입력하세요.\n")
        student_id = input("학번: ")  
        name = input("이름: ")
        eng = int(input("영어: "))
        clang = int(input("C-언어: "))
        py = int(input("파이썬: "))
        student = Student(student_id, name, eng, clang, py)
        # DB 갱신
        self.insert_student_db(student)
        self.calculate_ranks()
        print("학생이 추가되었습니다.\n")
        
    # 학생 삭제
    def delete_student(self):
        student_id = input("삭제할 학생의 학번을 입력하세요: ")
        self.cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
        if self.cursor.rowcount == 0:
            print("해당 학생을 찾을 수 없습니다.\n")
        else:
            self.conn.commit()
            # DB 갱신
            self.calculate_ranks()
            print(f"{student_id} 학번의 학생이 삭제되었습니다.\n")
    
    # 학생 검색(탐색)
    def search_student(self):
        student_id = input("찾을 학생의 학번을 입력하세요: ")
        self.cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
        row = self.cursor.fetchone()
        if row:
            print("\n검색 결과:")
            print(f"학번: {row[0]}, 이름: {row[1]}, 영어: {row[2]}, C-언어: {row[3]}, 파이썬: {row[4]}, 총점: {row[5]}, 평균: {row[6]:.2f}, 학점: {row[7]}, 등수: {row[8]}")
        else:
            print("해당 학생을 찾을 수 없습니다.\n")
    
    # 평균 80점 이상인 학생 수 출럭
    def count_high_scores(self):
        self.cursor.execute('SELECT COUNT(*) FROM students WHERE avg >= 80')
        count = self.cursor.fetchone()[0]
        print(f"\n평균 80점 이상인 학생 수: {count}\n")
    
    # 전체 학생 정보 출력(총점 순 정렬)
    def result(self):
        # DB에서 정보 다시 불러오기
        students = self.load_students()
        students.sort(key=lambda s: s.total, reverse=True)
        print("\n\t\t\t성적관리 프로그램")
        print("=" * 80)
        print("\t학번\t\t이름   영어  C-언어  파이썬  총점   평균  학점  등수")
        print("=" * 80)
        for s in students:
            print(f"{s.id}\t{s.name}\t{s.eng}    {s.clang}     {s.py}    {s.total}   {s.avg:.2f}   {s.grade}    {s.rank}")
        self.count_high_scores()
    
    # DB에 연결 종료
    def close(self):
        self.conn.close()

# ===============================
# 메인 함수
# ===============================
def main():
    manager = GradeManagement()
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
            manager.close()
            break
        else:
            print("잘못된 입력입니다. 다시 입력하세요.")

if __name__ == "__main__":
    main()