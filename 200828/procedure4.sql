-- -- lotto_sal (7788,20) ==> 40% Ȯ���� �޿� �λ�
-- -- lotto_sal (7788,20) ==> 40% Ȯ���� �޿� �谨

-- create or replace procedure lotto_sal(vempno emp.empno%type, vration number)
-- is
-- vsal emp.sal%type := 0;
-- vcheck number;

-- vupsal emp.sal%type := 0;
-- vdownsal emp.sal%type :=0;

-- begin

-- -- 40% Ȯ����?
--     --PL/SQL DB���� ����ߴ� �Լ��� �״�� ��� ���� 
--     vcheck :=trunc(dbms_random.value(0,10),0);
--         dbms_output.put_line(vcheck ||'��');
    
--     if vcheck in(2,5,7,9) then 
--     select sal 
--     into vsal 
--     from emp
--     where empno = vempno;
--     dbms_output.put_line(vempno||' ����޿� : '||vsal);
    
--     vupsal := vsal* (vration/100);
--     dbms_output.put_line(vration||' %�λ�'||vupsal);
    
--     update emp
--     set sal = vsal + vupsal 
--     where empno = vempno;
--     dbms_output.put_line(vempno||'�� ����� �޿� : '||(vsal + vupsal));
        
        
--     elsif vcheck in(1,3,6,10) then     
--     select sal 
--     into vsal
--     from emp 
--     where empno = vempno;
--     dbms_output.put_line(vempno||' ����޿� : '||vsal);
    
--     vdownsal := vsal*(vration/100);
--     dbms_output.put_line(vration||' %����'||vdownsal);
    
--     update emp
--     set sal = vsal - vdownsal
--     where empno = vempno;
--     dbms_output.put_line( vempno||'�� ����� �޿� : ' || (vsal - vdownsal)); 
    
--     else 
            
--     dbms_output.put_line('�� ������ȸ��');
    
--     end if;

-- end;
-- /