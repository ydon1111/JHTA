INSERT INTO COPY_EMP4
SELECT *
FROM EMP;


connect system/oracle;

desc DBA_users;
     접근법위_관심keyword 복수형 
	 
	 user_내가 생성한 object 정보
	 
	 connect scott/tiger;
	 desc user_tables
	 내가 만든 테이블
	 
	 DESC ALL_TABLES; 
	 
	 SELECT TABLE_NAME , OWNER
		FROM ALL_TABLES;
		
		--USER_ , ALL_ 
		
		--USER_관심대상S 
		--ALL_관심대상S 
		
		
		
	회원 
	
	ID 	        PW	      NAME    EMAIL     TEL       INTRO        STATUS
	VARCHAR 2 VARCHAR2
	
	
	LONG ===> LOB (LARGE OBJECT 
			  CLOB	
			  BLOB
			  BFILE 
	2GB 넣을 수 있음 
	
	
	CREATE TABLE MEMEBER 
	(ID VARCHAR2(20),
	PW VARCHAR2(20),
	NAME VARCHAR2(20),
	EMAIL VARCHAR2(20),
	TEL CHAR(11),
	INTRO CLOB,
	STATUS NUMBER(2));
	
	
	INSERT INTO MEMEBER
	VALUES('GGG','GGG','YEONGDON KIM','GGGG@NAVER.COM',010-1111-1111,'HELLO BYE',1);
	
	
	
	
	
	
	
	CREATE TABLE COPY_EMP99
	AS 
	SELECT *
	FROM EMP;
	
	컬럼 추가
	ALTER TABLE COPY_EMP99
	ADD HP VARCHAR2(10);
	
	컬럼명 변경 
	ALTER TABLE COPY_EMP99 RENAME COLUMN HP TO MP;
	
	칼럼형식 변경 줄이는 건 불가능 , 늘리는 것만 가능함  
	ALTER TABLE COPY_EMP99 
	MODIFY MP VARCHAR2(13); 
	
	컬럼 삭제
	ALTER TABLE COPY_EMP99
	DROP COLUMN MP;
	
	CREATE , ALTER ,DROP
	
	테이블 삭제
	DROP TABLE COPY_EMP99;
	
	
	DROP  == TABLE 구조를 지움
	DELETE == TABLE ROW 지움 
	
	휴지통
	SHOW RECYCLEBIN;
	
	지운자료 가져오기 
	FLASHBACK TABLE COPY_EMP99
	TO BEFORE DROP;
	
	RENAME A T0 B 
	
	테이블명 변경 
	RENAME COPY_EMP99 TO CEMP;
	
	
	테이블 안에 모든 데이터를 삭제
	TRUNCATE  TABLE CEMP;
	
	테이블 안에 데이터를 삭제, 삭제된걸 되돌릴 수 있음 
	DELETE CEMP; 
	
	DROP TABLE CEMP;
	
	SHOW RECYCLEBIN;
	
	FLASHBACK TABLE CEMP
	TO BEFORE DROP;
	
	휴지통에 안들어가고 바로 삭제
	DROP TABLE CEMP PURGE;
	
	
	----
	COMMENT ON TABLE EMP
	IS 'EMPLOYEE TABLE'
	
	
	내가 생성한 테이블의 주석 
	DESC USER_TAB_COMMENTS 
	
	SELECT * FROM USER_TAB_COMMENTS;
	
	
	----------DDL 명령어
	CREATE , ALTER , DROP , RENAME , TRUNCATE , COMMENT 
	
	
	
	
	
	INSERT INTO DEPT
	VALUES(50 , 'A' , 'B')
	
	SELECT * FROM DEPT;
	
	
	
	 SET SQLPROMPT "부산B>"
	
	TCL : TRANSACTION 
	일련의 작업처리를 위한 연관된 DML의 모음 
	
	ALL OR NOTHING 의 성격을 가짐 
	
	
	SELECT * FROM DEPT;
	
	변경 transaction 실행 
	COMMIT;
	
	
	해당 TRANSACTION 취소 
	ROLLBACK;
	
	
	INSERT INTO BONUS
	VALUES ('AAA', 'MANAGER', 3000,100)
	
	INSERT INTO BONUS
	SELECT * FROM BONUS;
	
	
	중간 저장하기 
	SAVEPOINT A1;
	
	
	
	저장한 지점으로 이동하기 
	ROLLBACK TO A3;
	
	
	접속자 이름 알려주기 
	SET SQLPROMPT "_USER>"
	
	
	UPDATE EMP 
	SET SAL = 100
	WHERE ENAME = 'SCOTT';
	
	SELECT SAL 
	FROM EMP
	WHERE ENAME = 'SCOTT';
	
	UPDATE EMP 
	SET SAL =200
	WHERE ENAME = 'SCOTT';
	
	
	LOCK 
	T 간 상호 파괴적인 행위를 막기 위해 ORACLE 보호 관리 메카니즘 
	ROW , TABLE , DATABASE 에 락을 걸 수 있음 	
	기본적으로 ROW LOCK 을 사용함  
	무한대기 
	
	데드락 
	양쪽에 크로스로 락이 걸린 상황
	먼저 기다린 명령문을 취소시켜줘서 해결함
	
	서울A>UPDATE EMP
  2  SET SAL = 100
  3  WHERE ENAME = 'SCOTT';

1 행이 갱신되었습니다.

서울A>UPDATE EMP
  2  SET SAL = 300
  3  WHERE ENAME = 'SMITH';
UPDATE EMP
       *
1행에 오류:
ORA-00060: 자원 대기중 교착 상태가 검출되었습니다
	
	
	SQL
	QUERY - SELECT 
	DML - INSERT , UPDATE , DELETE 
	TCL - COMMIT , ROLLBACK
	DDL - CREATE , ALTER , DROP , RENAME , TRUNCATE , COMMENT
	
	T == > SQLPLUS == LOGIN  LOGOUT ===> 1T
	
	
	비정상 종료 : AUTO ROLLBACK 
	정상 종료(EXIT) , DDL, DCL : AUTO COMMIT;  
	
	
database 특성	
	
동시성
무결성

제약조건 
constraint 

table 생성할때 제약조건 

table 이후 제약조건


1.COLUMN LEVEL 정의 방식
		컬럼명 자료형 [CONSTRAINT 제약명] 제약종류         
		제약명 : 오라클이 임의의 이름을 부여 
				(SYS_C숫자형식)
				
				제약명 == 관리하기 편하기 위해서 이름을 부여함

2.TABLE LEVEL 정의방식 
		컬럼명 자료형, 
		컬럼명 자료형,
		CONSTRAINT 제약명 제약종류 (컬럼명) 




primary key   
not null 
check 
FOREIGN key
uniQue
	
	
	CREATE TABLE DEPT1 
	(DEPTNO NUMBER(2) PRIMARY KEY,
	DNAME VARCHAR2(20) UNIQUE,
	LOC VARCHAR2(20));
	
	
	CREATE TABLE EMP1
	(EMPNO NUMBER(4) CONSTRAINT EMP1_EMPNO_PK PRIMARY KEY,
	ENAME VARCHAR2(20) NOT NULL,
	SAL NUMBER(7,2),
	DEPTNO NUMBER(2),
	CONSTRAINT EMP1_SAL_CK CHECK (SAL BETWEEN 500 AND 5000),
	CONSTRAINT EMP1_DEPTNO_FK FOREIGN KEY (DEPTNO)
	REFERENCES DEPT1(DEPTNO));
	
	
	
	INSERT INTO DEPT1 VALUES(1,'A','B');
	
	
	