

kor , eng , mat = input("점수입력 :").split()  #점수를 입력받음

kor = int(kor)              #입력 받은 점수를 int로 형변환
eng = int(eng)              #입력 받은 점수를 int로 형변환
mat = int(mat)              #입력 받은 점수를 int로 형변환

tot = kor + eng + mat
avg = tot/3
print(kor,eng,mat,tot,avg)

if avg >= 90:
    print(avg, "A")
elif avg >= 80:
    print(avg, "B")
elif avg >= 70:
    print(avg, "C")
elif avg >= 60:
    print(avg, "D")
else :
    print(avg, "f")    