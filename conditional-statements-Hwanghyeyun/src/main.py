# 황혜윤 과제 제출합니다#
import datetime

# (1) 초기 사용자 목록 생성
users = {
    "admin1": {"name": "황혜윤", "birth": "", "password": "1234", "role": "admin"},
    "editor1": {"name": "황혜정", "birth": "", "password": "4567", "role": "editor"},
    "viewer1": {"name": "황혜영", "birth": "", "password": "9876", "role": "viewer"}
}


def print_users():
    print("===사용자 목록===")
    print(
        f"아이디: {uid}, 이름: {info['name']}, 생년월일: {info['birth']}, 역할: {info['role']}")
    print("========")

# (2) 회원가입


def singup():
    print("===회원가입===")
    # 아이디
    while True:
        uid = input("아이디를 입력하세요")
        if uid in users:
            print("이미 존재하는 아이디 입니다")
        else:
            break

    # 이름
    name = input("이름을 입력하세요")

    # 생일
    while True:
        birth = input("생일을 입력하세요()")
        try:
            datetime.datetime.strptime(birth, "%Y-%m-%d")
            break
        except: print("잘못된 날짜 형식입니다. 다시 입력하세요.")
    # 비밀번호
        while True:
            password = input("비밀번호 10자 이상 입력하세요")
            if len(password) >= 10:
                break
            else:
                print("잘못된 비밀번호 입니다.")
    # 역할
        while True:
            role = input('역할을 지정하세요("viewer", "editor", "admin"): ')
            if role in ["viewer", "editor", "admin"]:
                break
            else:
                print("잘못된 역할입니다.")

    users[uid] = {"name": name, "birth": birth, "password": password, "role": role}
    print("====회원가입 완료====")
    print_users()
        

#(3) 로그인
def login():
    uid = input("아이디: ")
    pw = input("비밀번호: ")
    if uid in users and users[uid]["password"] == pw:
        print(f"{uid} 로그인 성공! 역할: {users[uid]['role']}")
        role = users[uid]["role"]

    print("====로그인 완료====")

#(4) 기능

    while True:
        print("1. 정보 수정  2. 회원 탈퇴 ")
        choice = input("선택: ")
        if choice == "1":
            target = uid if role == "viewer" else input("수정할 아이디 입력: ")
            if target in users:
                users[target]["name"] = input("새 이름 입력: ")
                print("정보 수정 완료!")
                print_users()

        elif choice == "2":  #탈퇴 
            target = uid if role != "admin" else input("삭제할 아이디 입력: ")
            if target in users:
                del users[target]
                print("계정 삭제 완료!")
                print_users()
                if role != "admin":
                    break
            else: print("아이디 또는 비밀번호 틀림")

#수정 
def update_user(target_uid):
    print(f"=== {target_uid} 정보 수정 ===")
    name = input("새 이름 입력: ")
    users[target_uid]["name"] = name
    print(f"{target_uid} 정보가 수정되었습니다.")
    print_users()
      

#사용자 목록 출력
def print_users():
    print("\n=== 사용자 목록 ===")
    for uid, info in users.items():
        print(f"{uid} | {info['name']} | {info['birth']} | {info['role']}")
    print("=================\n")





