--7369번 사원의 사번 , 이름 ,job ,부서번호


DECLARE 
	vempno NUMBER;
	vename VARCHAR2 (100);
	vjob VARCHAR2 (100);
	vdeptno NUMBER;



BEGIN
	SELECT empno, ename, job, deptno
		INTO vempno , vename , vjob , vdeptno
	
	FROM emp
	WHERE empno = 7369;

	DBMS_OUTPUT.PUT_LINE('사번 : '|| vempno);
	DBMS_OUTPUT.PUT_LINE('이름 : ' || vename);
	DBMS_OUTPUT.PUT_LINE('직업 : ' || vjob);
	DBMS_OUTPUT.PUT_LINE('부서번호 : ' || vdeptno);




END;
/


