program RecordExample;

type
  TStudent = record
    Name: string;
    Age: integer;
    GPA: real;
  end;

  TCourse = record
    Name: string;
    Code: string;
    Credit: integer;
  end;

  TEnrollment = record
    Student: TStudent;
    Course: TCourse;
    Grade: integer;
  end;

var
  Enrollment: TEnrollment;

begin
  Enrollment.Student.Name := 'Alice';
  Enrollment.Student.Age := 20;
  Enrollment.Student.GPA := 3.5;
  Enrollment.Course.Name := 'Programming 101';
  Enrollment.Course.Code := 'CS101';
  Enrollment.Course.Credit := 3;
  Enrollment.Grade := 85;

  writeln('Student: ', Enrollment.Student.Name);
  writeln('Course: ', Enrollment.Course.Name);
  writeln('Grade: ', Enrollment.Grade);
end.