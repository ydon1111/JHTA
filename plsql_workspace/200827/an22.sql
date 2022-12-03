ACCEPT vn01 prompt '사번입력 : '
DECLARE 
	VEMPNO EMP.EMPNO%TYPE := &vn01;
	VENAME EMP.ENAME%TYPE;
	VSAL EMP.SAL%TYPE;
	--예외의 이름을 지정 
	vex1 exception;
	-- 컴파일에게 예외가 발생할때 예외명과 에러번호를 연결해 라고 지시하는 명령
	PRAGMA exception_init(vex1,-06502);
	--사용자 정의형 예외
	VEX2 EXCEPTION;


BEGIN
 --   vsal := 'scott';
	SELECT EMPNO,ENAME,SAL
		INTO VEMPNO , VENAME, VSAL
	FROM EMP
	WHERE empno = vempno;
	-- 사원의 급여가 3000 이상이면 값을 출력 
	-- 3000이하면 출력 x 
	IF VSAL < 3000 THEN
		--예외를 발생
		RAISE VEX2;

	END IF;

	DBMS_OUTPUT.PUT_LINE(VEMPNO || ' ' ||VENAME|| ' ' || VSAL);
EXCEPTION 
	WHEN VEX2 THEN
		DBMS_OUTPUT.PUT_LINE('월급은 비밀');
	
	WHEN vex1 THEN 
		dbms_output.put_line('숫자열 변수에 문자값을 할당할 수 없습니다.');
	--예외처리부
	--미리 정의된 예외처리 
	WHEN NO_DATA_FOUND THEN --예외명 
		dbms_output.put_line('그런 사원은 존재하지 않습니다');
	--처리문장2;
	WHEN TOO_MANY_ROWS THEN 
		dbms_output.put_line('해당 사원이 둘 이상입니다.');
	WHEN INVALID_CURSOR THEN 
		dbms_output.put_line('커서의 사용법이없다.');


END;
/

--DECLARE 


--EXCEPTION