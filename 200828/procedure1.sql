-- create procedure ���ν�����(���� �ڷ���,....)

-- �޿� 10% �λ��ϴ� ���ν��� raise_sal 

create or replace procedure raise_sal (vempno emp.empno%type)
is  
 vsal emp.sal%type := 0;
begin
    --����� �޿� ��������
    select sal 
        into vsal
    from emp
    where empno = vempno;

    -- 10% �λ�� �޿� ���
 

    vsal := vsal*1.1;

    --����
    update emp
    set sal = vsal
    where empno = vempno;


end;
/


-- execute raise_sal(7788);         procedure ���� 