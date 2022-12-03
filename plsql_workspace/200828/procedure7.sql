create or replace procedure lotto_bonus2(vdeptno emp.deptno%type)
is
    cursor c1 is 
     select ename, job ,sal ,comm
     from emp
     where deptno = vdeptno ;

begin
    for c2 in c1 loop 
    insert into bonus
        values (c2.ename,c2.job,c2.sal,c2.comm);
    
    
    
    -- dbms_output.put_line(c2.ename ||' '|| c2.job||' '||c2.sal||' '||c2.comm);
    
    end loop;

    commit;


end;
/
-- SQL> truncate table bonus; 테이블 내용삭제


