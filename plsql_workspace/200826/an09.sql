DECLARE 
	vsum NUMBER := 0;

BEGIN
    FOR i IN 1..100 LOOP 
-- := ����
-- = ��
		IF mod(i,3)=0 THEN 
			vsum := vsum+i;			
		END IF; 
		
	END loop;
DBMS_OUTPUT.PUT_LINE('1���� 100 ������ 3�ǹ���� ������ ' ||vsum);	
END;
/

