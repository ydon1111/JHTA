create OR REPLACE function find_dname(vempno emp.empno%type)
    return dept.dname%type                -- ����� ���� ������ ���� ����� 

is 
    vdname dept.dname%type;

begin
  
    select dname
     into vdname
    from dept d , emp e
    where d.deptno = e.deptno and empno = vempno;

    return vdname;

end;
/


-- SQL> desc find_annsal                �Լ���� ã��

-- SQL> select distinct name, type 
--   2  from user_source;                �����Լ� ã��


-- set pangesize 5000 
-- SQL> select text                  �ҽ��ڵ� Ȯ���ϱ�
--   2  from user_source 
--   3  where name = 'FIND_ANNSAL';  �빮�ڷ� Ȯ���ؾ��� ���ڿ���



-- CREATE OR REPLACE FUNCTION         ������ �� �տ� ���(ȸ�翡���� ����ȵ�)

-- col find_dname(empno) format a20   ��°� ũ������ 