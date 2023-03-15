program BubbleSort;

var
  arr: array[1..10] of integer;
  i, j, temp: integer;

begin
  writeln('Enter 10 numbers:');
  for i := 1 to 10 do
    readln(arr[i]);

  for i := 1 to 9 do
    for j := i + 1 to 10 do
      if arr[i] > arr[j] then begin
        temp := arr[i];
        arr[i] := arr[j];
        arr[j] := temp;
      end;

  writeln('Sorted array:');
  for i := 1 to 10 do
    write(arr[i], ' ');
end.