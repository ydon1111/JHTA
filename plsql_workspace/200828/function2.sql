create OR REPLACE function find_annsal(vempno emp.empno%type)
    return number 
is 
    vannsal emp.sal%type :=0;

begin
  
    select sal*12 +nvl(comm,0)
     into vannsal 
    from emp 
    where empno = vempno;

    return vannsal;

end;
/


-- SQL> desc find_annsal                함수요소 찾기

-- SQL> select distinct name, type 
--   2  from user_source;                만든함수 찾기


-- set pangesize 5000 
-- SQL> select text                  소스코드 확인하기
--   2  from user_source 
--   3  where name = 'FIND_ANNSAL';  대문자로 확인해야함 문자열은



-- CREATE OR REPLACE FUNCTION         수정할 때 앞에 사용(회사에서는 쓰면안됨)
