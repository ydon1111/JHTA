-- creat function 함수명(매개변수 자료형)
--         return 리턴값의 자료형
-- is 
-- 변수선언
-- begin
  
--     return ;

-- exception
--   when no_data_found then
--     ;

-- end;

create function find_sal(vempno emp.empno%type)  
    return number
is
    vsal emp.sal%type := 0;
begin

    select sal 
        into vsal
    from emp
    where empno = vempno;

    return vsal;
end;
/

-- show errors 에러가 무엇인지 찾기 

-- drop function find_sal; 삭제하기 