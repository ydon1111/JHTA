-- PL/SQL CURSOR
-- SQL문을 처리하기위해 서버 메모리에 확보하는 공간을 CURSOR라 한다.
-- 종류 : 1.암시적 커서 : SQL문을 사용했을때
--		 2.명시적 커서 : PL/SQL에서는 이것을 명시적으로 제어 할 수 있다.


-- 사용법: 1. CURSOR정의
--		2.OPEN
--		3.FETCH
--		4.CLOSE

-- 이런 SQL 문을 사용할때 생기는 공간을 커서라하자.

DECLARE 
	-- 1. C1 커서를 정의
	CURSOR C1 IS 
		SELECT EMPNO , ENAME , SAL 
		FROM EMP
		WHERE DEPTNO =10;

	--3개의 변수를 담을 대표변수 : PL/SQL RECORD 
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

<!-- 커서명  -->
<!-- 
%ISOPEN  T,F  열렸는지 확인 
	%FOUND   T,F  FETCH 찾았으면 확인 
	%NOTFOUND T,F FETCH 못찾았으면 T
	%ROWCOUNT  FETCH 횟수

 -->