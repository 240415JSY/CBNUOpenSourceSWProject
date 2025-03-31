import random #컴퓨터가 랜덤힌 곳에 두도록 할 수 있음.

def print_board(board):
    for i in range(3):
        print(" | ".join(board[i])) #사이사이에 구분하기
        if i < 2:
            print("-" * 10) #가로로 구분하기


def check(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def move(board): #보드 위에서 원하는 곳으로 이동
    moves = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                moves.append((r, c)) #해당 좌표로 이동
    return moves

def player_move(board): #플레이어의 배치
    while True:
        move_input = input("배치하고자 하는 행과 열을 입력하세요.(범위: 0~2 0~2): ")
        number = move_input.split() #공백 기준으로 나누가. 0 2 입력하면 number운 0, 2
        #두 개로 구분되었고 모두 숫자라면
        if len(number) == 2 and number[0].isdigit() and number[1].isdigit():
            a, b = int(number[0]), int(number[1]) #각각 a와 b에 저장
            if (a, b) in move(board):
                board[a][b] = "X" #보드에 표시
                break
        print("잘못된 접근입니다. 다시 입력하세요")

def computer_move(board): #컴퓨터의 배치
    print("컴퓨터의 배치:")
    a, b = random.choice(move(board)) #랜덤한 좌표로 이동
    board[a][b] = "O" #해당 좌표에 표시

def main():
    board = [[" " for _ in range(3)] for _ in range(3)] #틱택토 보드의 범위 설정
    print_board(board) #출력
    
    for _ in range(9):
        player_move(board)
        print_board(board)
        if check(board, "X"):
            print("당신의 승리")
            return
        
        if move(board):
            computer_move(board)
            print_board(board)
            if check(board, "O"):
                print("컴퓨터 승리")
                return
    
    print("무승부")

main()