--지정된 값으로 물어보기
ACCEPT vno prompt '검색할 부서번호 입력:' 

DECLARE 
	--실행하는 순간에 vno 변수에 담을 값을 물얼보고
	--입력된 값이 치환되어 실행된다. 
	-- '&' 넣으면 담을 값을 입력할 수 있음 
	vdeptno NUMBER := &vno;
	vdname varchar2(20);
	vloc varchar2(20);

BEGIN
    SELECT dname,loc
		INTO vdname , vloc 
	FROM dept
	WHERE deptno = vdeptno;


	DBMS_OUTPUT.PUT_LINE('부서이름 : ' || vdname);
	DBMS_OUTPUT.PUT_LINE('지역 : ' || vloc);

END;
/


