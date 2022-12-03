create or replace trigger update_tri
after update on dept 
for each row 


begin
    update cdept
    set dname = :new.dname , loc = :new.loc 
    where deptno = :old.deptno;


end;
/

-- old 와 new 가 있음 
-- old 는 기존에 있던 값
-- new 는 새로운값 