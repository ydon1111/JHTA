-- package 
-- ���� ���Ǵ� ������ ���������� �Լ��� ����
-- 1.package spec 
--     �̸� , �Ű����� , ����Ÿ�� ����

-- 2.package body
--     �ҽ� �ڵ� 

create or replace package my_pack
is

--package spec 
--find_annsal �Լ�
function find_annsal(vempno emp.empno%type)
    return number;
--riase_sal 
procedure raise_sal2(vempno emp.empno%type,vration number);

end;
/