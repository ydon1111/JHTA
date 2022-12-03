ACCEPT vn01 prompt '����Է� : '
DECLARE 
	VEMPNO EMP.EMPNO%TYPE := &vn01;
	VENAME EMP.ENAME%TYPE;
	VSAL EMP.SAL%TYPE;
	--������ �̸��� ���� 
	vex1 exception;
	-- �����Ͽ��� ���ܰ� �߻��Ҷ� ���ܸ�� ������ȣ�� ������ ��� �����ϴ� ���
	PRAGMA exception_init(vex1,-06502);
	--����� ������ ����
	VEX2 EXCEPTION;


BEGIN
 --   vsal := 'scott';
	SELECT EMPNO,ENAME,SAL
		INTO VEMPNO , VENAME, VSAL
	FROM EMP
	WHERE empno = vempno;
	-- ����� �޿��� 3000 �̻��̸� ���� ��� 
	-- 3000���ϸ� ��� x 
	IF VSAL < 3000 THEN
		--���ܸ� �߻�
		RAISE VEX2;

	END IF;

	DBMS_OUTPUT.PUT_LINE(VEMPNO || ' ' ||VENAME|| ' ' || VSAL);
EXCEPTION 
	WHEN VEX2 THEN
		DBMS_OUTPUT.PUT_LINE('������ ���');
	
	WHEN vex1 THEN 
		dbms_output.put_line('���ڿ� ������ ���ڰ��� �Ҵ��� �� �����ϴ�.');
	--����ó����
	--�̸� ���ǵ� ����ó�� 
	WHEN NO_DATA_FOUND THEN --���ܸ� 
		dbms_output.put_line('�׷� ����� �������� �ʽ��ϴ�');
	--ó������2;
	WHEN TOO_MANY_ROWS THEN 
		dbms_output.put_line('�ش� ����� �� �̻��Դϴ�.');
	WHEN INVALID_CURSOR THEN 
		dbms_output.put_line('Ŀ���� �����̾���.');


END;
/

--DECLARE 


--EXCEPTION