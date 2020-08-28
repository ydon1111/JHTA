declare
    -- 변수를 성너하면서 초기값을 지정
    vno number := 100;

begin
--put_line 함수를 매개변수 1개만 올수 있다.begin
-- 문자 숫자 연결 ||
    dbms_output.put_line('vno:' || vno);

end;
/

-- set serverout on