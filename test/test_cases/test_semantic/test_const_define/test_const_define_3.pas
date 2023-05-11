program test(input,output);  
const a = 1.5;  
      b = 3;  
      {c = -a;
      d = -b;}
      e = 2;  
      f = 5;  
      {g = -c;}
begin  
    a:=3; //常量不能作为左值  
    e:=6-3; //常量不能作为左值  
    g:=b+c; //常量不能作为左值  
end.  
