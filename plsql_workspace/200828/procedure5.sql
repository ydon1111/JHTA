-- lotto_sal (7788,20) ==> 40% Ȯ���� �޿� �λ�
-- lotto_sal (7788,20) ==> 40% Ȯ���� �޿� �谨

create or replace procedure lotto_sal(vempno emp.empno%type, vration number)
is
vsal emp.sal%type := 0;
vcheck number;

vupsal emp.sal%type := 0;
vdownsal emp.sal%type :=0;

begin

-- 40% Ȯ����?
    --PL/SQL DB���� ����ߴ� �Լ��� �״�� ��� ���� 
    vcheck :=trunc(dbms_random.value(0,10),0);
        dbms_output.put_line(vcheck ||'��');
    
    if vcheck in(2,5,7,9) then 
        raise_sal2(vempno,vration);
        
    elsif vcheck in(1,3,6,10) then     
        down_sal(vempno,vration);

    
    else 
            
    dbms_output.put_line('�� ������ȸ��');
    
    end if;

end;
/