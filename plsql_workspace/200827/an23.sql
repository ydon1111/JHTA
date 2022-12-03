BEGIN
  
   UPDATE emp
   SET sal = 100
   WHERE empno = 7788;

   commit;

END;
/


