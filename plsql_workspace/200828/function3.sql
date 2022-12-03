create OR REPLACE function find_dname(vempno emp.empno%type)
    return dept.dname%type                -- 출력할 값의 형식을 정해 줘야함 

is 
    vdname dept.dname%type;

begin
  
    select dname
     into vdname
    from dept d , emp e
    where d.deptno = e.deptno and empno = vempno;

    return vdname;

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

-- col find_dname(empno) format a20   출력값 크기조절 