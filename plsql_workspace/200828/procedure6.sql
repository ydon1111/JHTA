create or replace procedure lotto_bonus(vempno emp.empno%type)
is 

vename  emp.ename%type;
vjob  emp.job%type;
vsal  emp.sal%type;
vcomm  emp.comm%type;


begin
-- 1. �Է��� ������� ������� �˻�
-- 2. ������ �Ҵ�
-- 3. bounus ���̺� ��´�


select ename, job, sal, comm
 into vename, vjob, vsal , vcomm
from emp 
where empno = vempno;

insert into bonus 
values (vename, vjob, vsal,vcomm);

commit;



end;
/