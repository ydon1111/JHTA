DECLARE 
vempno NUMBER;
vename varchar2(20);
vsal number;


BEGIN    
	SELECT empno , ename , sal*12+ nvl(comm,0)
		INTO  vempno,vename,vsal 
	FROM emp
	WHERE empno = 7788;

	
	DBMS_OUTPUT.PUT_LINE('��� :'||vempno);
	DBMS_OUTPUT.PUT_LINE('�̸� :'||vename);
	DBMS_OUTPUT.PUT_LINE('���� :'||vsal);

END;
/


