-- trigger 
-- ������ �̺�Ʈ�� ���ؼ� �Ͻ������� ȣ��Ǵ� pl/sql promgram unit

-- dept ���̺� �����Ͱ� �߰��� �Ŀ� 
-- cdept ���̺� �� ������ �߰� 

create or replace trigger ins_tri
-- Ʈ���Ű� ������ �̺�Ʈ�� ���ؼ� ��� 
after insert on dept
-- �� �ึ�� ����
for each row  

begin
  
-- ���ڵ带 ����
    --  ��� �߰��� �������� ���� ��������
    -- cdept���̺� �߰� 
    insert into cdept 
    values (:new.deptno, :new.dname,:new.loc );
    -- :new ����ؼ� ���ο� ���� ������
end;
/
