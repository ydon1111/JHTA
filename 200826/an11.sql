--������ ������ �����
ACCEPT vno prompt '�˻��� �μ���ȣ �Է�:' 

DECLARE 
	--�����ϴ� ������ vno ������ ���� ���� ���󺸰�
	--�Էµ� ���� ġȯ�Ǿ� ����ȴ�. 
	-- '&' ������ ���� ���� �Է��� �� ���� 
	vdeptno NUMBER := &vno;
	vdname varchar2(20);
	vloc varchar2(20);

BEGIN
    SELECT dname,loc
		INTO vdname , vloc 
	FROM dept
	WHERE deptno = vdeptno;


	DBMS_OUTPUT.PUT_LINE('�μ��̸� : ' || vdname);
	DBMS_OUTPUT.PUT_LINE('���� : ' || vloc);

END;
/


