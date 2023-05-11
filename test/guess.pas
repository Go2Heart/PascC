program programguess(input,output);
    const smaller="Smaller!";
          bigger="Bigger!";
    var x,y:integer;
    begin
        read(x);
        while 1 do
        begin
            read(y);
            if y=x then write(x);
            if y<x then write(smaller);
            if y>x then write(bigger);
        end;
    end.