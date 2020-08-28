DECLARE 
vemp emp%rowtype;
-- emp 테이블의 모든 컬럼명을 멤버변수로 하는
-- 대표변수를 선언할수 있다.

BEGIN
    SELECT *
		INTO vempno,vename,vsal,vjob
	FROM emp 
	WHERE empno = 7788;
	-- 사번, 이름 ,급여 ,job 
	DBMS_OUTPUT.PUT_LINE(vemp.empno || ' '||vemp.ename||' '|| vemp.sal|| ' ' ||vemp.job);
END;
/


