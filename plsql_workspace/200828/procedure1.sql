-- create procedure 프로시져명(변수 자료형,....)

-- 급여 10% 인상하는 프로시져 raise_sal 

create or replace procedure raise_sal (vempno emp.empno%type)
is  
 vsal emp.sal%type := 0;
begin
    --사원의 급여 가져오기
    select sal 
        into vsal
    from emp
    where empno = vempno;

    -- 10% 인상된 급여 계산
 

    vsal := vsal*1.1;

    --변경
    update emp
    set sal = vsal
    where empno = vempno;


end;
/


-- execute raise_sal(7788);         procedure 실행 