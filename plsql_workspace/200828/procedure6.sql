create or replace procedure lotto_bonus(vempno emp.empno%type)
is 

vename  emp.ename%type;
vjob  emp.job%type;
vsal  emp.sal%type;
vcomm  emp.comm%type;


begin
-- 1. 입력한 사번으로 사원정보 검색
-- 2. 변수에 할당
-- 3. bounus 테이블에 담는다


select ename, job, sal, comm
 into vename, vjob, vsal , vcomm
from emp 
where empno = vempno;

insert into bonus 
values (vename, vjob, vsal,vcomm);

commit;



end;
/