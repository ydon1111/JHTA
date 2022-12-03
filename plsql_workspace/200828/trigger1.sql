-- trigger 
-- 정해진 이벤트에 의해서 암시적으로 호출되는 pl/sql promgram unit

-- dept 테이블에 데이터가 추가된 후에 
-- cdept 테이블에 이 내용을 추가 

create or replace trigger ins_tri
-- 트리거가 동작할 이벤트에 대해서 기술 
after insert on dept
-- 각 행마다 실행
for each row  

begin
  
-- 이코드를 실행
    --  방금 추가한 데이터의 값을 가져오기
    -- cdept테이블에 추가 
    insert into cdept 
    values (:new.deptno, :new.dname,:new.loc );
    -- :new 사용해서 새로운 값을 가져옴
end;
/
