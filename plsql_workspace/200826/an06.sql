begin
  for i in reverse 1..9 loop
      dbms_output.put_line('3 * '||i||'='|| 3*i);
  end loop;
  -- 3*9 = 27
  -- 3*8 = 24 

end;
/

