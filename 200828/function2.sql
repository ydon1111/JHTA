create function find_annsal(vempno emp.empno%type)
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