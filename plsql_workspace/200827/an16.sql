DECLARE 
	-- PL/SQL TABLE 선언 : PL_TAB 새로운 자료형 
	TYPE PL_TAB IS TABLE OF EMP.ENAME%TYPE 
	INDEX BY BINARY_INTEGER; 
	-- 배열은 아파트형 변수 
	-- 같은 사이즈의 연속된 공간에 할당되는 변수 


	-- 변수 선언
	PL1 PL_TAB;
	-- VEMPNO NUMBER;

BEGIN

	FOR i IN 1..20 LOOP
		PL1(i) := 'SCOTT'||i;
	END LOOP;

	FOR J IN 1..20 LOOP
		DBMS_OUTPUT.PUT_LINE(PL1(J));
	END LOOP;
END;
/


