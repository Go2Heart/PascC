program test(input,output);
var a:integer;
procedure pro;
begin
    writeln(a);
end;
function fun:integer;
begin
    fun:=100;
end;
begin
    writeln(fun);
    a:=fun mod 3;
    pro;
end.
