DECLARE 
i NUMBER :=1;

BEGIN
	WHILE i <10 LOOP 
	DBMS_OUTPUT.PUT_LINE('3 * ' || i || '=' || i *3);
	i := i+1;
	END loop;

END;
/


-- loop   while ���� loop  for ���� in ���Ѱ�..���Ѱ� loop


