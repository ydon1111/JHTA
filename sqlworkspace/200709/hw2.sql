
16.이름이 s자로 시작하고 마지막 글자가 h인 사람의 모든정보를 출력?

SELECT *
FROM EMP
WHERE ENAME LIKE 'S%H'; 

17. 부서 번호가 20인 사원의 일일 임금을 계산 하여 출력?

SELECT ENAME , ROUND(SAL/30 , 0) 
FROM EMP
WHERE DEPTNO = 20 

18. 입사일이 빠른순서대로 이름과 월급을 출력하여라

SELECT ENAME , SAL 
FROM EMP
ORDER BY HIREDATE ;

19. 이름이 다섯자인 사람의 리스트를 출력하여라

SELECT ENAME 
FROM EMP
WHERE ENAME LIKE '_____';

20. 메니저(MGR)가 7566과 7782인 사원번호, 사원명, 메니저, 부서번호를 출력하세요.

SELECT DEPTNO, ENAME , MGR , DEPTNO
FROM EMP
WHERE MGR IN(7566,7782);


21. 급여가 1100보다 크고 2000보다 작은 사원번호, 사원명, 급여를 출력하세요.

SELECT DEPTNO, ENAME , SAL
FROM EMP
WHERE SAL BETWEEN 1101 AND 1999;

22. 이름의 첫 글자가 M으로 시작하거나 급여가 1000 이상인 사람의 사원명과 급여 부서번호를 출력하라.

SELECT ENAME , SAL, DEPTNO 
FROM EMP 
WHERE ENAME LIKE 'M%'
AND SAL >=1000;

23. 급여가 1000이상이고 부서번호가 30번인 사람의 사원명 급여 사원번호를 출력하라.

SELECT ENAME , SAL , DEPTNO 
FROM EMP
WHERE SAL >= 1000 
AND DEPTNO = 30; 

24. 이름이 A로 시작하는 사원번호,성명,부서번호를 출력하시오.

SELECT EMPNO , ENAME , DEPTNO
FROM EMP
WHERE ENAME LIKE 'A%';

25. 사원번호에 8을 포함하고 있는 사원번호,성명을 출력하시오.

SELECT EMPNO , ENAME 
FROM EMP
WHERE EMPNO LIKE '%8%'

26. 급여가 800&이상 1500미만의 사람의 이름,부서,월급을 출력하여라.

SELECT ENAME , DEPTNO , SAL 
FROM EMP
WHERE SAL BETWEEN 800 AND 1499

27. 수당이 300 이거나, 500 이거나, 1400인 사람들의 사번, 이름, 수당을 출력하세요.

SELECT EMPNO , ENAME , SAL 
FROM EMP 
WHERE COMM IN ( 300, 500, 1400)

28. 이름에서 2번째 자리에 L 이 들어가는 사람의 이름을 출력하세요.

SELECT ENAME 
FROM EMP
WHERE ENAME LIKE '_L%'

27. 해당 관리자가 null 인 사람을 찾아 출력하여라.

SELECT ENAME 
FROM EMP
WHERE MGR IS NULL

28. 이름이 B로시작하는 사람의 연봉을 출력하라

SELECT SAL 
FROM EMP
WHERE ENAME LIKE 'B%';

29. 연봉이 1500이상5000이하인 사원 이름을 출력하라

SELECT ENAME 
FROM EMP
WHERE SAL BETWEEN 1500 AND 5000;

30. 사원테이블에서 급여가 2500 이하이고 직무가 MANAGER인 사람의 사원번호, 성명, 급여, 해당관리자번호를 출력하라.

SELECT EMPNO , ENAME , SAL, MGR
FROM EMP
WHERE SAL <= 2500;

31. 사원테이블에서 입사일자가 82년도~83년도인 사원의 사원번호, 성명, 직무, 입사일자를 출력하라.

SELECT EMPNO , ENAME , JOB , HIREDATE 
FROM EMP 
WHERE HIREDATE BETWEEN '82/01/01' AND '83/12/31' 

32. 입사일자가 83년 이후 이며 87년 이전인 사람의 이름과 사번을 출력하시오.

SELECT ENAME , EMPNO
FROM EMP
WHERE HIREDATE BETWEEN '83/01/01' AND '87/12/31'

33. 수당의 해당사항없는 사람들의 사번,이름, 입사날짜를 출력하시오.

SELECT EMPNO , ENAME , HIREDATE 
FROM EMP
WHERE COMM IS NULL


34. 회계부서에서 급여가 1500이 넘는 사람

SELECT ENAME , SAL 
FROM EMP
WHERE DEPTNO = (SELECT DEPTNO FROM DEPT WHERE DEPTNO = 10)
AND SAL > 1500;

35. 판매부서의 직원이름, 연봉, 입사일자 출력

SELECT ENAME , SAL*12 , HIREDATE
FROM EMP 
WHERE DEPTNO = (SELECT DEPTNO FROM DEPT WHERE DEPTNO = 30);

