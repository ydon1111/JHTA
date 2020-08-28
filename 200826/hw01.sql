DECLARE 

i NUMBER := 1;

BEGIN
    FOR i IN 2..9 LOOP
		DBMS_OUTPUT.PUT_LINE('------------------------');
		FOR r IN 1..9 loop
			DBMS_OUTPUT.PUT_LINE(i || '*' || r || '=' || i*r);
		END LOOP;

	END loop;

	
	
END;
/


