ACCEPT no prompt '부서번호 : '

-- DECLARE 

-- CURSOR c1 IS 
-- 	SELECT sal 
-- 	FROM emp
-- 	WHERE deptno = &no; 

BEGIN
	-- FOR c2 IN c1 loop
	-- dbms_output.put_line(c2.sal);

	UPDATE emp
	SET sal = sal*(1.1)
	WHERE deptno = &no;
	
	-- END loop;
	-- dbms_output.put_line('----------------');
	
	-- FOR c2 IN c1 loop
	-- dbms_output.put_line(c2.sal);
	-- END loop;

END;
/


