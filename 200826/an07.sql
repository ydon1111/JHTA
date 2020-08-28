DECLARE 
	i NUMBER := 0;

BEGIN
    -- BASIC LOOP¹®
	LOOP
		i := i +1;
	EXIT WHEN i >9;
	 DBMS_OUTPUT.PUT_LINE('3 * ' || i || '=' || 3*i);
	 END loop;
END;
/
