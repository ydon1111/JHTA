-- package 
-- 자주 사용되는 연관된 프러시져와 함수의 모음
-- 1.package spec 
--     이름 , 매개변수 , 리턴타입 정보

-- 2.package body
--     소스 코드 

create or replace package my_pack
is

--package spec 
--find_annsal 함수
function find_annsal(vempno emp.empno%type)
    return number;
--riase_sal 
procedure raise_sal2(vempno emp.empno%type,vration number);

end;
/