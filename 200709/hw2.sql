
16.�̸��� s�ڷ� �����ϰ� ������ ���ڰ� h�� ����� ��������� ���?

SELECT *
FROM EMP
WHERE ENAME LIKE 'S%H'; 

17. �μ� ��ȣ�� 20�� ����� ���� �ӱ��� ��� �Ͽ� ���?

SELECT ENAME , ROUND(SAL/30 , 0) 
FROM EMP
WHERE DEPTNO = 20 

18. �Ի����� ����������� �̸��� ������ ����Ͽ���

SELECT ENAME , SAL 
FROM EMP
ORDER BY HIREDATE ;

19. �̸��� �ټ����� ����� ����Ʈ�� ����Ͽ���

SELECT ENAME 
FROM EMP
WHERE ENAME LIKE '_____';

20. �޴���(MGR)�� 7566�� 7782�� �����ȣ, �����, �޴���, �μ���ȣ�� ����ϼ���.

SELECT DEPTNO, ENAME , MGR , DEPTNO
FROM EMP
WHERE MGR IN(7566,7782);


21. �޿��� 1100���� ũ�� 2000���� ���� �����ȣ, �����, �޿��� ����ϼ���.

SELECT DEPTNO, ENAME , SAL
FROM EMP
WHERE SAL BETWEEN 1101 AND 1999;

22. �̸��� ù ���ڰ� M���� �����ϰų� �޿��� 1000 �̻��� ����� ������ �޿� �μ���ȣ�� ����϶�.

SELECT ENAME , SAL, DEPTNO 
FROM EMP 
WHERE ENAME LIKE 'M%'
AND SAL >=1000;

23. �޿��� 1000�̻��̰� �μ���ȣ�� 30���� ����� ����� �޿� �����ȣ�� ����϶�.

SELECT ENAME , SAL , DEPTNO 
FROM EMP
WHERE SAL >= 1000 
AND DEPTNO = 30; 

24. �̸��� A�� �����ϴ� �����ȣ,����,�μ���ȣ�� ����Ͻÿ�.

SELECT EMPNO , ENAME , DEPTNO
FROM EMP
WHERE ENAME LIKE 'A%';

25. �����ȣ�� 8�� �����ϰ� �ִ� �����ȣ,������ ����Ͻÿ�.

SELECT EMPNO , ENAME 
FROM EMP
WHERE EMPNO LIKE '%8%'

26. �޿��� 800&�̻� 1500�̸��� ����� �̸�,�μ�,������ ����Ͽ���.

SELECT ENAME , DEPTNO , SAL 
FROM EMP
WHERE SAL BETWEEN 800 AND 1499

27. ������ 300 �̰ų�, 500 �̰ų�, 1400�� ������� ���, �̸�, ������ ����ϼ���.

SELECT EMPNO , ENAME , SAL 
FROM EMP 
WHERE COMM IN ( 300, 500, 1400)

28. �̸����� 2��° �ڸ��� L �� ���� ����� �̸��� ����ϼ���.

SELECT ENAME 
FROM EMP
WHERE ENAME LIKE '_L%'

27. �ش� �����ڰ� null �� ����� ã�� ����Ͽ���.

SELECT ENAME 
FROM EMP
WHERE MGR IS NULL

28. �̸��� B�ν����ϴ� ����� ������ ����϶�

SELECT SAL 
FROM EMP
WHERE ENAME LIKE 'B%';

29. ������ 1500�̻�5000������ ��� �̸��� ����϶�

SELECT ENAME 
FROM EMP
WHERE SAL BETWEEN 1500 AND 5000;

30. ������̺��� �޿��� 2500 �����̰� ������ MANAGER�� ����� �����ȣ, ����, �޿�, �ش�����ڹ�ȣ�� ����϶�.

SELECT EMPNO , ENAME , SAL, MGR
FROM EMP
WHERE SAL <= 2500;

31. ������̺��� �Ի����ڰ� 82�⵵~83�⵵�� ����� �����ȣ, ����, ����, �Ի����ڸ� ����϶�.

SELECT EMPNO , ENAME , JOB , HIREDATE 
FROM EMP 
WHERE HIREDATE BETWEEN '82/01/01' AND '83/12/31' 

32. �Ի����ڰ� 83�� ���� �̸� 87�� ������ ����� �̸��� ����� ����Ͻÿ�.

SELECT ENAME , EMPNO
FROM EMP
WHERE HIREDATE BETWEEN '83/01/01' AND '87/12/31'

33. ������ �ش���׾��� ������� ���,�̸�, �Ի糯¥�� ����Ͻÿ�.

SELECT EMPNO , ENAME , HIREDATE 
FROM EMP
WHERE COMM IS NULL


34. ȸ��μ����� �޿��� 1500�� �Ѵ� ���

SELECT ENAME , SAL 
FROM EMP
WHERE DEPTNO = (SELECT DEPTNO FROM DEPT WHERE DEPTNO = 10)
AND SAL > 1500;

35. �Ǹźμ��� �����̸�, ����, �Ի����� ���

SELECT ENAME , SAL*12 , HIREDATE
FROM EMP 
WHERE DEPTNO = (SELECT DEPTNO FROM DEPT WHERE DEPTNO = 30);

