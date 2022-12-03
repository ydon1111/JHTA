#사용자로부터 글자를 입력받아 이 문자가 대문자인지 소문자인지 판단
# 1.사용자의 입력값을 받아오기
# 2.이 값의 ascii 코드 값을 구한다.
# 3. A:65     a:97
# 4. 65~ 90      97~ 122 범위
# 5. 판단 후 출력 

data = input("한글자를 입력하세요 : ")
print(data)
print(ord(data))   #ord ascii 값으로 변환
code = ord(data)   #ascii 코드값 가져오기 
if code >= 65 and code <= 90:             # and 를 사용해서 조건 2개 넣기
    print(data + "대문자입니다",code)
elif code >= 97 and code <=122:
    print(data + "소문자입니다",code)

    

