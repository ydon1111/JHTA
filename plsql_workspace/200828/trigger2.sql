create or replace trigger update_tri
after update on dept 
for each row 


begin
    update cdept
    set dname = :new.dname , loc = :new.loc 
    where deptno = :old.deptno;


end;
/

-- old �� new �� ���� 
-- old �� ������ �ִ� ��
-- new �� ���ο 