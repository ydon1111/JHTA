----------------------- SUBQUERY  --------------------------------------
  
  SELECT ENAME, SAL
  FROM EMP					
  WHERE SAL >=
  ( SELECT SAL FROM EMP WHERE ENAME = 'JONES');
  
  
  SELECT ENAME , HIREDATE 
  FROM EMP 
  WHERE HIREDATE >= (SELECT HIREDATE FROM EMP WHERE ENAME='BLAKE');
  
  
  SQL> SELECT EMPNO, ENAME , SAL , DEPTNO
  2  FROM EMP
  3  WHERE SAL > (SELECT AVG(SAL) FROM EMP WHERE DEPTNO = 20);

     EMPNO ENAME             SAL     DEPTNO
---------- ---------- ---------- ----------
      7566 JONES            2975         20
      7698 BLAKE            2850         30
      7782 CLARK            2450         10
      7788 SCOTT            3000         20
      7839 KING             5000         10
      7902 FORD             3000         20

6 개의 행이 선택되었습니다.

SELECT AVG(SAL) 
FROM EMP
GROUP BY DEPTNO 
HAVING DEPTNO = 20;

SELECT EMPNO , ENAME , SAL , DEPTNO
FROM EMP
WHERE SAL > (SELECT SAL FROM EMP WHERE HIREDATE LIKE '80%')


SELECT EMPNO , ENAME , SAL , DEPTNO
FROM EMP
WHERE SAL > (SELECT SAL FROM EMP WHERE HIREDATE LIKE '80/12/17')

SELECT EMPNO , ENAME , SAL , DEPTNO
FROM EMP
WHERE SAL > (SELECT SAL FROM EMP WHERE HIREDATE = '1980/12/17')


SELECT EMPNO , ENAME , SAL , DEPTNO
FROM EMP
WHERE SAL > (SELECT SAL FROM EMP WHERE HIREDATE = '80/12/17')


무슨차이일까??


LIKE '80%'


SELECT EMPNO , ENAME , SAL , DEPTNO
FROM EMP
WHERE SAL > (SELECT SAL FROM EMP WHERE HIREDATE LIKE '%80%')


    SINGLE ROW SUBQUERY       	결과값이 하나
    MULTIPLE ROW SUBQUERY   	결과값이 하나 이상 
	MULTIPLE COLUMN SUBQUERY 	컬럼이 하나 이상 


1. ( ) 사용
2.SINGLE ROW SUBQUERY => SINGLE ROW OPERATOR 
3.MULTIPLE ROW SUBQUERY => MULTIOLE ROW OPERATOR  ( IN () 등을 사용)
4.( ) ORDER BY  X 지원하지 않음 필요없기 때문에 
	단 8I 이후 버전부터 FROM 절에 사용되는 SUBQUERY의 경우 사용가능함 => INLINE-VIEW 
	
	
	SELECT EMPNO , ENAME , SAL 
	FROM EMP 
	WHERE DEPTNO IN ( SELECT DEPTNO FROM DEPT WHERE LOC = 'CHICAGO';
	
	
	JOIN 사용해서 
	
	SELECT E.EMPNO , E.ENAME , E.SAL
	FROM EMP E, DEPT D 
	WHERE E.DEPTNO = D.DEPTNO
	AND D.LOC = 'CHICAGO'





테이블 변경 방법 (추가, 삭제, 등 )

DML 

SELECT *
FROM DEPT;


-------------------------------------------자료추가 

INSERT INTO DEPT 
VALUES(50,'A','B');

SQL> SELECT *
  2  FROM DEPT;

    DEPTNO DNAME          LOC
---------- -------------- -------------
        10 ACCOUNTING     NEW YORK
        20 RESEARCH       DALLAS
        30 SALES          CHICAGO
        40 OPERATIONS     BOSTON



SQL> INSERT INTO DEPT
  2  VALUES(50,'A','B');

1 개의 행이 만들어졌습니다.





SQL> SELECT *
  2  FROM DEPT;

    DEPTNO DNAME          LOC
---------- -------------- -------------
        50 A              B
        10 ACCOUNTING     NEW YORK
        20 RESEARCH       DALLAS
        30 SALES          CHICAGO
        40 OPERATIONS     BOSTON



-------------------자료추가 


INSERT INTO DEPT
VALUES (60, NULL, 'C');

SQL> INSERT INTO DEPT
  2  VALUES (60, NULL, 'C');

1 개의 행이 만들어졌습니다.

SQL> SELECT *
  2  FROM DEPT;

    DEPTNO DNAME          LOC
---------- -------------- -------------
        50 A              B
        60                C
        10 ACCOUNTING     NEW YORK
        20 RESEARCH       DALLAS
        30 SALES          CHICAGO
        40 OPERATIONS     BOSTON

6 개의 행이 선택되었습니다.

INSERT INTO DEPT(DEPTNO,DNAME)
VALUES (70,'영업');

SQL> SELECT *
  2  FROM DEPT;

    DEPTNO DNAME          LOC
---------- -------------- -------------
        50 A              B
        60                C
        70 영업
        10 ACCOUNTING     NEW YORK
        20 RESEARCH       DALLAS
        30 SALES          CHICAGO
        40 OPERATIONS     BOSTON

7 개의 행이 선택되었습니다.


----------------------------변경하기


UPDATE DEPT 
SET LOC = '제주'
WHERE DEPTNO = 50; 

SQL> SELECT *
  2  FROM DEPT;

    DEPTNO DNAME          LOC
---------- -------------- -------------
        50 A              제주
        60                C
        70 영업
        10 ACCOUNTING     NEW YORK
        20 RESEARCH       DALLAS
        30 SALES          CHICAGO
        40 OPERATIONS     BOSTON

7 개의 행이 선택되었습니다.
 
UPDATE DEPT 
SET DNAME = 'AI' , LOC = 'LA'
WHERE DEPTNO =60

SQL> SELECT *
  2  FROM DEPT;

    DEPTNO DNAME          LOC
---------- -------------- -------------
        50 A              제주
        60 AI             LA
        70 영업
        10 ACCOUNTING     NEW YORK
        20 RESEARCH       DALLAS
        30 SALES          CHICAGO
        40 OPERATIONS     BOSTON

7 개의 행이 선택되었습니다.

---------------------------지우기
DELETE (FROM) DEPT                FROM 생략가능
WHERE DEPTNO IN (50,60,70);

DELETE DEPT 
WHERE DEPTNO IN (50,60,70);




SQL> SELECT *
  2  FROM DEPT;

    DEPTNO DNAME          LOC
---------- -------------- -------------
        10 ACCOUNTING     NEW YORK
        20 RESEARCH       DALLAS
        30 SALES          CHICAGO
        40 OPERATIONS     BOSTON

   TABLE 

	사용자 정의형 TABLE 



	관리용 TABLE 
      DATA DICTIONARY 
	  
	  
	  
   DDL  테이블 만들기 
   
   CREATE TABLE COPY_EMP 
   (EMPNO NUMBER(4),       숫자 4자리 9999
	ENAME VARCHAR2(20),    글 20 글자 
	SAL NUMBER(7,2),       숫자 실수7, 소수2  9999999.99
	HIREDATE DATE);         자료형 
	
	
	SQL> DESC COPY_EMP;
 이름                                      널?      유형
 ----------------------------------------- -------- ----------------------------
 EMPNO                                              NUMBER(4)
 ENAME                                              VARCHAR2(20)
 SAL                                                NUMBER(7,2)
 HIREDATE                                           DATE
 
 
 CHAR  = 고정문자 (2000자) 자리가 주어진 고정으로 자리잡음, 자료를 불러오기 편함 
 
 VARCHAR = 가변문자 현재 사용하지않음 2로 자동 변환됨
 VARCHAR2 = 가변문자 성능이 더 좋음 (4000자) 남는 자리를 반납하여 공간사용 데이터를 아낌
 


 CREATE TABLE COPY_EMP2
 (EMPNO NUMBER(4),
	ENAME VARCHAR2(10),
	JOB VARCHAR2(9),
	MGR NUMBER(4),
	HIREDATE DATE,
	SAL NUMBER(7,2),
	COMM NUMBER(7,2),
	DEPTNO NUMBER(2));
 
 SQL> INSERT INTO COPY_EMP2
  2  VALUES (7788,'SCOTT','ANALYST',7566,'87/04/19',3000,NULL,20);
 
 
 ------------CREAT < == SUBQUERY 가능
 ----TABLE 복사하기 
 
 CREATE TABLE COPY_EMP3
 AS
 SELECT *
 FROM EMP; 
 
 COPY_EMP4 : EMP 테이블의 구조와 동일한구조 ROW는 없는 
 
 CREATE TABLE COPY_EMP4
 AS
 SELECT *
 FROM EMP
 WHERE EMPNO = 9999;   <--자료에서 없는 값을 넣어서 비어줌(혹시 나올 수 있음)
 
 CREATE TABLE COPY_EMP5
 AS
 SELECT *
 FROM EMP
 WHERE 0 = 1 ; <---자료에서 없는 값을 넣어서 비어줌 (절대 나올 수 없음)

------------자료값 복사하기









 
   
        