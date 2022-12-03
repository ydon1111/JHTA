import salary as s                        #모듈을 만들어서 가져오기 

print(s.raise_sal(5000))
print(s.reduce_sal(5000))

print('--------------------------------------------')
import lottosalary as ls

#50% 확율로 급여가 20%인상
print(ls.raise_rnd_salary(2000))
#50% 확율로 급여가 20%감소
print(ls.reduece_rnd_salary(2000))