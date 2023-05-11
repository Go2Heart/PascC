program test(input, output);
var ans:integer;
{
    求斐波那契数列值的过程，利用引用参数保存结果;
    n表示求第n项斐波那契数列值;
    fib(0)=1, fib(1)=1, ……, fib(n)=fib(n-1)+fib(n-2);
}
procedure fib(n:integer;var res:integer);
var tmp1,tmp2:integer;
begin
    if n=0 then
        res:=1
    else
        if n=1 then
            res:=1
        else
        begin
            fib(n-1,tmp1);
            fib(n-2,tmp2);
            res:=tmp1+tmp2;
        end;
end;
{
    自己编写的输出函数，可以实现输出n次out值;
    递归调用自身，n每次减1;
    out值采用的是引用参数;
}
procedure mywrite(n:integer; var out:integer);
begin
    if n=0 then
        {exit}
    else
    begin
        writeln(out);
        mywrite(n-1, out);
    end;
end;

begin
    fib(10, ans); //ans=fib(10)
    mywrite(3, ans); //输出ans 3次
end.

