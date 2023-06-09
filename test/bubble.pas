program BubbleSort;

const 
  c = 2;
type
  TStudent = record
    Age: integer;
    GPA: real;
  end;

  TCourse = record
    Credit: integer;
  end;

  TEnrollment = record
    Student: TStudent;
    Course: TCourse;
    Grade: integer;
  end;
var
  arr: array[1..10] of integer;
  i, j, temp: integer;
begin
  writeln('Enter 10 numbers:');
  i:=1;
  while i<=10 do
  BEGIN
      readln(arr[i]);
      i := i+1;
  END;

repeat 
  i:=i-1;
until i=0;
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