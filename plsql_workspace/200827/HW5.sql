ACCEPT VJOB prompt '직업을 입력하세요 : '

DECLARE
	CURSOR C1 IS
			SELECT EMPNO,ENAME,SAL,JOB,DEPTNO
			FROM EMP
			WHERE JOB = &VJOB;
			
BEGIN
    
	FOR C2 IN C1 LOOP
	IF C2.DEPTNO != 10 THEN
		DBMS_OUTPUT.PUT_LINE(C2.EMPNO || ' ' ||C2.ENAME||' '||C2.SAL||' '||C2.JOB||' '||C2.DEPTNO);
	END IF;
	END LOOP;

END;
/


