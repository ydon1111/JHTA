create OR REPLACE function find_annsal(vempno emp.empno%type)
    return number 
is 
    vannsal emp.sal%type :=0;

begin
  
    select sal*12 +nvl(comm,0)
     into vannsal 
    from emp 
    where empno = vempno;

    return vannsal;

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
