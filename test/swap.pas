program gcd_program(input,output);
    var x,y,temp,ret:integer;
    function swap(var a,b:integer):integer; 
        begin
            temp := a;
            a := b;
            b := temp;
            swap:=1;
        end;
    begin
        read(x);
        read(y);
        ret:=swap(x, y);
        write(x,y);
end.
