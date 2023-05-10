program test(input,output);
function fun:integer;
var a,b:integer;
begin
    if a>0 then
        fun:=1
    else
        writeln(a); //该分支缺少返回值语句
end;
begin
    writeln(fun);
end.