create or replace procedure down_sal(vempno emp.empno%type , vration number)
is

vsal emp.sal%type := 0;
vdownsal emp.sal%type :=0;
begin
  
    select sal 
        into vsal
    from emp 
    where empno = vempno;

vdownsal := vsal*(vration/100);

update emp
   set sal = vsal - vdownsal
 where empno = vempno;
dbms_output.put_line( vempno||'±Þ¿©'|| (vsal - vdownsal));
end;
/