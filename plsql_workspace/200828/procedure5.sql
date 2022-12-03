-- lotto_sal (7788,20) ==> 40% 확률로 급여 인상
-- lotto_sal (7788,20) ==> 40% 확률로 급여 삭감

create or replace procedure lotto_sal(vempno emp.empno%type, vration number)
is
vsal emp.sal%type := 0;
vcheck number;

vupsal emp.sal%type := 0;
vdownsal emp.sal%type :=0;

begin

-- 40% 확률은?
    --PL/SQL DB에서 사용했던 함수를 그대로 사용 가능 
    vcheck :=trunc(dbms_random.value(0,10),0);
        dbms_output.put_line(vcheck ||'값');
    
    if vcheck in(2,5,7,9) then 
        raise_sal2(vempno,vration);
        
    elsif vcheck in(1,3,6,10) then     
        down_sal(vempno,vration);

    
    else 
            
    dbms_output.put_line('꽝 다음기회에');
    
    end if;

end;
/