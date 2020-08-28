-- PL/SQL CURSOR
-- SQL���� ó���ϱ����� ���� �޸𸮿� Ȯ���ϴ� ������ CURSOR�� �Ѵ�.
-- ���� : 1.�Ͻ��� Ŀ�� : SQL���� ���������
--		 2.����� Ŀ�� : PL/SQL������ �̰��� ��������� ���� �� �� �ִ�.


-- ����: 1. CURSOR����
--		2.OPEN
--		3.FETCH
--		4.CLOSE

-- �̷� SQL ���� ����Ҷ� ����� ������ Ŀ��������.

DECLARE 
	-- 1. C1 Ŀ���� ����
	CURSOR C1 IS 
		SELECT EMPNO , ENAME , SAL 
		FROM EMP
		WHERE DEPTNO =10;

	--3���� ������ ���� ��ǥ���� : PL/SQL RECORD 
	C2 C1%ROWTYPE;

BEGIN
	-- 2. OPEN 
	OPEN C1; 
	-- 3. FETCH 
	LOOP 
		FETCH C1 INTO C2;
		EXIT WHEN C1%NOTFOUND;
			DBMS_OUTPUT.PUT_LINE(C2.EMPNO||' ' ||C2.ENAME||' '||C2.SAL);
		END LOOP;
	--4. CLOSE
	CLOSE C1;
END;
/

<!-- Ŀ����  -->
<!-- 
%ISOPEN  T,F  ���ȴ��� Ȯ�� 
	%FOUND   T,F  FETCH ã������ Ȯ�� 
	%NOTFOUND T,F FETCH ��ã������ T
	%ROWCOUNT  FETCH Ƚ��

 -->