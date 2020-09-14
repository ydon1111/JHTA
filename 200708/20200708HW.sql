1. 사원들의 이름, 부서 번호, 부서 이름을 출력하라 ?

SELECT E.ENAME , DEPTNO, D.DNAME
FROM EMP E NATURAL JOIN DEPT D;


2. 30 번 부서의 사원들의 이름, 직업, 부서위치를 출력하라

	SELECT E.ENAME, E.JOB, D.LOC, DEPTNO
	FROM EMP E NATURAL JOIN DEPT D 
	WHERE DEPTNO = 30 


3. 커미션을 받는 사원의 이름 , 부서이름 및 부서위치를
 출력하라 ? (단 COMM 이 NULL 이 아닌 사원)  
 
    SELECT E.ENAME , DEPTNO, D.LOC
    FROM EMP E NATURAL JOIN DEPT D
    WHERE COMM IS NOT NULL
	
	
4. dallas 에서 근무하는 사원의 이름 , 직업, 부서번호 , 부서이름
 을 출력하라 ?
 
   SELECT E.ENAME, E.JOB, DEPTNO, D.DNAME
   FROM EMP E NATURAL JOIN DEPT D
   WHERE D.LOC = 'DALLAS'
 
 
5. 이름에 A 가 들어가는 사원들의 이름과 부서이름을 출력하라 ?

	select e.ename, d.dname
	from emp e NATURAL JOIN dept d
	WHERE e.ename LIKE '%A%';
	
	
6. 사원이름과 그 사원의 관리자 이름을 출력하라
( 단 컬럼 HEADING 을 employeee, manager 출력 )

	SELECT E.ENAME "employee" , C.ENAME "manager"
    FROM EMP E LEFT JOIN  EMP C ON (E.MGR = C.EMPNO)
	
	
7. 사원이름과 직업, 급여, 급여등급 을 출력하라 ?

	SELECT E.ENAME , E.JOB, E.SAL, S.GRADE
    FROM EMP E JOIN SALGRADE S
	ON E.SAL BETWEEN S.LOSAL AND S.HISAL 
	
	
8. 사원이름과 부서명과 월급을 출력하는데 월급이 3000 이상인 사원을
 출력하라 ? 
 
	SELECT E.ENAME, D.DNAME , E.SAL
    FROM EMP E NATURAL JOIN DEPT D
    WHERE E.SAL >= 3000 ;
	
	
9. 사원의 이름, 부서번호 와 같은 부서에 근무하는 동료 사원들을
출력하라 ? 

	SELECT D.ENAME , C.DEPTNO, C.ENAME
	FROM EMP D JOIN EMP C
    ON D.DEPTNO = C.DEPTNO 
	AND D.ENAME <> C.ENAME	
	
	
10. BLAKE 이란 사원보다 늦게 입사한 사원의 이름과 입사일을 출력하라 ? 

	SELECT e.ename, e.hiredate
	FROM EMP E JOIN EMP C 
	ON C.ename = 'BLAKE' AND e.hiredate > c.hiredate;
	

	
