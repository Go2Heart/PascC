program test(input,output);  
const a = 1.5;  
      b = 3;  
      c = -a;  
      d = -b;  
      e = 2;  
      f = 5;  
      g = -c;  
var h:integer;  
    i:real;  
    j:array[1..10] of integer;  
begin  
    writeln(a);  
    writeln(b);  
    writeln(c);  
    writeln(d);  
    writeln(e);  
    writeln(f);  
    writeln(g);  
    h := h / (2+3-f); //除0错误  
    h := h mod (10 mod e); //除0错误  
    h := h div (1 div d); //除0错误  
    j[b+f]:=3; //正确  
    writeln(j[b+f]); //正确  
    j[-f]:=5; //越界  
end.  
