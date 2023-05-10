program test(input,output);
var   a,i:integer; //整型变量
      b:real; //浮点型变量
      c:char; //字符型变量
      d:array[1..6] of integer; //数组
procedure pro(var a:integer);
begin
    read(a);
end;
begin
    read(c,a); //读取字符和整数
    for i:=1 to 6 do
        pro(d[i]); //循环加调用程序读取6个整数
    read(b); //读取浮点数

    writeln(c,' ',a); //输出字符和整数
    for i:=1 to 6 do //输出6个整数，空格分隔
        write(d[i],' ');
//    writeln; //输出换行
    writeln(b); //输出浮点数
end.
