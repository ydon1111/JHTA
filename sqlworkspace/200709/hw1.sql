<   SUBQUERY   �ǽ�����  > 
 
1.  SMITH ���� ������  ���� �޴� ������� �̸��� ������ ����϶� ? 
 
	SELECT ENAME , SAL 
	FROM EMP
	WHERE SAL > (SELECT SAL FROM EMP WHERE ENAME = 'SMITH');
 
2.  10 �� �μ��� ������ ���� ������ �޴� ������� �̸��� ���ް� �μ� 
   ��ȣ�� ����϶� ? 
 
	SELECT ENAME , SAL , DEPTNO 
	FROM EMP
	WHERE SAL IN (SELECT SAL FROM EMP WHERE DEPTNO = 10);
 
3. BLAKE �� ���� �μ��� �ִ� ������� �̸��� �Ի����� ����ϵ�  BLAKE �� ���� 
 
	SELECT ENAME , HIREDATE 
	FROM EMP
	WHERE DEPTNO = (SELECT DEPTNO FROM EMP WHERE ENAME = 'BLAKE')
	AND ENAME <> 'BLAKE';
	
4. ��� �޿����� ���� �޿��� �޴� ������� ���, �̸�, ������ ��Ÿ���� ������ ���� ��� 
������  ����϶� ? 
	
	SELECT EMPNO , ENAME , SAL 
	FROM EMP
	WHERE SAL > (SELECT AVG(SAL) FROM EMP)
	ORDER BY SAL  DESC;
 
 
5. �̸���  T  �� �����ϰ� �ִ� ������  ������ �μ����� �ٹ��ϰ� �ִ� ����� ��� ��
ȣ�� �̸���  ����϶� ? 

	SELECT EMPNO , ENAME 
	FROM EMP 
	WHERE ENAME IN (SELECT ENAME FROM EMP WHERE ENAME LIKE '%T%');
 

6. 30 �� �μ��� �ְ� �޿��� �޴� ��� ���ٵ� �� ���� �޿��� �޴� ��ü ������� ����϶� 
 
	SELECT ENAME , SAL  
	FROM EMP 
	WHERE SAL > (SELECT MAX(SAL) FROM EMP WHERE DEPTNO =30)
 
7. �μ� ��ġ�� DALLAS ��  ��� ����� �̸�, �μ� ��ȣ �� ������ ����϶� ? 
 
	SELECT ENAME , DEPTNO , JOB 
	FROM EMP 
	WHERE DEPTNO = (SELECT DEPTNO FROM DEPT WHERE LOC = 'DALLAS');
	
 
8.  SALES  �μ��� ��� ����� ���� �μ���ȣ, �̸� �� ������ ����϶� ? 
 
	SELECT DEPTNO , ENAME , JOB 
	FROM EMP 
	WHERE DEPTNO =(SELECT DEPTNO FROM DEPT WHERE DNAME = 'SALES');
 
9.  KING ����  ���� �ϴ� ��� ����� �̸��� �޿��� ����϶� ? (�� ���ӻ�簡 KING �� 
���) 
	
	SELECT ENAME , SAL 
	FROM EMP
	WHERE MGR = (SELECT EMPNO FROM EMP WHERE ENAME = 'KING');
	
 
10.  �ڽ���  �޿��� ��� ��� �޿����� �����鼭  �̸��� S �� ����  ����� ���� ��
����  ���  ����� �����ȣ, �̸�  �� �޿��� ����϶� ? 

	SELECT EMPNO , ENAME , SAL ,DEPTNO 
	FROM EMP
	WHERE SAL > (SELECT AVG(SAL) FROM EMP) 
	AND DEPTNO IN (SELECT DEPTNO FROM EMP WHERE ENAME LIKE '%S%');
	
	