<   SUBQUERY   실습문제  > 
 
1.  SMITH 보다 월급을  많이 받는 사원들의 이름과 월급을 출력하라 ? 
 
	SELECT ENAME , SAL 
	FROM EMP
	WHERE SAL > (SELECT SAL FROM EMP WHERE ENAME = 'SMITH');
 
2.  10 번 부서의 사원들과 같은 월급을 받는 사원들의 이름과 월급과 부서 
   번호를 출력하라 ? 
 
	SELECT ENAME , SAL , DEPTNO 
	FROM EMP
	WHERE SAL IN (SELECT SAL FROM EMP WHERE DEPTNO = 10);
 
3. BLAKE 와 같은 부서에 있는 사람들의 이름과 입사일을 출력하되  BLAKE 는 제외 
 
	SELECT ENAME , HIREDATE 
	FROM EMP
	WHERE DEPTNO = (SELECT DEPTNO FROM EMP WHERE ENAME = 'BLAKE')
	AND ENAME <> 'BLAKE';
	
4. 평균 급여보다 많은 급여를 받는 사원들의 사번, 이름, 월급을 나타내되 월급이 높은 사람 
순으로  출력하라 ? 
	
	SELECT EMPNO , ENAME , SAL 
	FROM EMP
	WHERE SAL > (SELECT AVG(SAL) FROM EMP)
	ORDER BY SAL  DESC;
 
 
5. 이름에  T  를 포함하고 있는 사원들과  동일한 부서에서 근무하고 있는 사원의 사원 번
호와 이름을  출력하라 ? 

	SELECT EMPNO , ENAME 
	FROM EMP 
	WHERE ENAME IN (SELECT ENAME FROM EMP WHERE ENAME LIKE '%T%');
 

6. 30 번 부서의 최고 급여를 받는 사원 보다도 더 많은 급여를 받는 전체 사원들을 출력하라 
 
	SELECT ENAME , SAL  
	FROM EMP 
	WHERE SAL > (SELECT MAX(SAL) FROM EMP WHERE DEPTNO =30)
 
7. 부서 위치가 DALLAS 인  모든 사원의 이름, 부서 번호 및 직업을 출력하라 ? 
 
	SELECT ENAME , DEPTNO , JOB 
	FROM EMP 
	WHERE DEPTNO = (SELECT DEPTNO FROM DEPT WHERE LOC = 'DALLAS');
	
 
8.  SALES  부서의 모든 사원에 대한 부서번호, 이름 및 직업을 출력하라 ? 
 
	SELECT DEPTNO , ENAME , JOB 
	FROM EMP 
	WHERE DEPTNO =(SELECT DEPTNO FROM DEPT WHERE DNAME = 'SALES');
 
9.  KING 에게  보고 하는 모든 사원의 이름과 급여를 출력하라 ? (즉 직속상사가 KING 인 
사원) 
	
	SELECT ENAME , SAL 
	FROM EMP
	WHERE MGR = (SELECT EMPNO FROM EMP WHERE ENAME = 'KING');
	
 
10.  자신의  급여가 사원 평균 급여보다 많으면서  이름에 S 자 들어가는  사원과 동일 부
서인  모든  사원의 사원번호, 이름  및 급여를 출력하라 ? 

	SELECT EMPNO , ENAME , SAL ,DEPTNO 
	FROM EMP
	WHERE SAL > (SELECT AVG(SAL) FROM EMP) 
	AND DEPTNO IN (SELECT DEPTNO FROM EMP WHERE ENAME LIKE '%S%');
	
	