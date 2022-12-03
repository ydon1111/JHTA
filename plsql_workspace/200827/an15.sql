DECLARE 
	TYPE PL_REC IS RECORD 
	(vempno emp.empno%type,
	vename emp.ename%type,
	vsal emp.sal%type);

-- 구조체 
-- 변수명 자료형 
	pl2 pl_rec;

BEGIN
	SELECT empno,ename,sal
		INTO pl2
	FROM emp
	WHERE empno = 7369;
    	
	DBMS_OUTPUT.PUT_LINE(pl2.vempno||' ' || pl2.vsal);
END;
/


