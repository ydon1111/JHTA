create or replace trigger del_tri
after delete on dept 
for each row

begin
 delete cdept
  where deptno = :old.deptno; 

end;
/

-- SQL> select trigger_name from user_triggers;


-- SQL> drop trigger del_tri;    
