DECLARE 
	vsum NUMBER := 0;

BEGIN
    FOR i IN 1..100 LOOP 
-- := 대입
-- = 비교
		IF mod(i,3)=0 THEN 
			vsum := vsum+i;			
		END IF; 
		
	END loop;
DBMS_OUTPUT.PUT_LINE('1부터 100 사이의 3의배수의 누적합 ' ||vsum);	
END;
/

