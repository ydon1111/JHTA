--1부터 100까지 출력
--변수를 하나 선언

declare
    -- 누적값을 담을 변수 vsum을 선언
    -- 숫자형 변수 초기값 0

    vsum number :=0;

begin
  
    for i in 1..100 loop
        vsum := vsum + i;
    end loop;
    dbms_output.put_line(vsum);
        
end;
/