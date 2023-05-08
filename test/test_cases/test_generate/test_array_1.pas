program test(input,output);
var i,j,k:integer;
    a:array[0..1, 2..3, 4..5] of integer; //数组定义
begin
    for i:=0 to 1 do
        for j:=2 to 3 do
            for k:=4 to 5 do
                read(a[i,j,k]); //三重循环，读入每一个数组元素，共8个
    for i:=0 to 1 do
        for j:=2 to 3 do
            for k:=4 to 5 do
                writeln(a[i,j,k]) //三重循环，输出每一个数组元素，换行符分隔
end.
