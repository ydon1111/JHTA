--7369�� ����� ��� , �̸� ,job ,�μ���ȣ


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

	DBMS_OUTPUT.PUT_LINE('��� : '|| vempno);
	DBMS_OUTPUT.PUT_LINE('�̸� : ' || vename);
	DBMS_OUTPUT.PUT_LINE('���� : ' || vjob);
	DBMS_OUTPUT.PUT_LINE('�μ���ȣ : ' || vdeptno);




END;
/


