marks = {}

sub1 = int(input("Enter marks of maths :"))
sub2 = int(input("Enter the marks of english :"))
sub3 = int(input("Enter the marks of chemistry :"))

marks.update({"maths":sub1})
marks.update({"english":sub2})
marks.update({"chemistry":sub3})

print(marks)