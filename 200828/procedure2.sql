create or replace procedure raise_sal2(vempno emp.empno%type,vration number)
is 
 vsal emp.sal%type :=0;
 vupsal emp.sal%type := 0;
begin


 select sal 
  into vsal 
 from emp
 where empno = vempno;
 dbms_output.put_line(vempno||' ����޿� : '||vsal);
 
 
 vupsal := vsal* (vration/100);
 dbms_output.put_line(vration||' %�λ�'||vupsal);
 
 
 update emp
    set sal = vsal + vupsal 
 where empno = vempno;
 dbms_output.put_line(vempno||'�� ����� �޿� : '||(vsal + vupsal));
 
end;
/