declare 
    -- 변수 선언부 
    VNO NUMBER ; --변수명 자료형 
    VSTR VARCHAR2(20); -- 컬럼 자료형

begin 
    -- 실행할 코드 
    VSTR := 'ORACLE';
    VNO := 20;  -- 대입 연산자
   
    -- 변수 값을 화면에 출력 
    DBMS_OUTPUT.PUT_LINE(VNO);
    DBMS_OUTPUT.PUT_LINE(VSTR);

end;
/