
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
	IF C1%ISOPEN THEN
		DBMS_OUTPUT.PUT_LINE('CURSOR ���µ�');
	END IF;
	
	
	-- 3. FETCH 
	LOOP 
		FETCH C1 INTO C2;
		IF C1%FOUND THEN 
			DBMS_OUTPUT.PUT_LINE('��ġ����');
		END IF;
		IF C1%NOTFOUND THEN 
			DBMS_OUTPUT.PUT_LINE('��ġ����');
		END IF;
		--���̻� ��ġ�� ���� ���ٸ� Ż�� 

		EXIT WHEN C1%NOTFOUND;
			DBMS_OUTPUT.PUT_LINE(C1%ROWCOUNT || '��° ROW: ' ||C2.EMPNO ||' ' ||C2.ENAME||' '||C2.SAL);
		END LOOP;
	--4. CLOSE
	CLOSE C1;
END;
/

-- Ŀ����  

--%ISOPEN  T,F  ���ȴ��� Ȯ�� 
--%FOUND   T,F  FETCH ã������ Ȯ�� 
--%NOTFOUND T,F FETCH ��ã������ T
--%ROWCOUNT  FETCH Ƚ��

