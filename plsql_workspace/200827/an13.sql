DECLARE 
vemp emp%rowtype;
-- emp ���̺��� ��� �÷����� ��������� �ϴ�
-- ��ǥ������ �����Ҽ� �ִ�.

BEGIN
    SELECT *
		INTO vempno,vename,vsal,vjob
	FROM emp 
	WHERE empno = 7788;
	-- ���, �̸� ,�޿� ,job 
	DBMS_OUTPUT.PUT_LINE(vemp.empno || ' '||vemp.ename||' '|| vemp.sal|| ' ' ||vemp.job);
END;
/


