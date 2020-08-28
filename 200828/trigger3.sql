create or replace trigger del_tri
after delete on dept 
for each row

begin
 delete cdept
  where deptno = :old.deptno; 

end;
/