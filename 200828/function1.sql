-- creat function �Լ���(�Ű����� �ڷ���)
--         return ���ϰ��� �ڷ���
-- is 
-- ��������
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

-- show errors ������ �������� ã�� 

-- drop function find_sal; �����ϱ� 