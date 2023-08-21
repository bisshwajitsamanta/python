grade = 72

if grade >=90:
    letter_grade = 'A'
else:
    if grade>=80:
        letter_grade = 'B'
    else:
        if grade >=70:
            letter_grade = 'C'
        else:
            if grade >=60:
                letter_grade = 'D'
            else:
                if grade >=50:
                    letter_grade = 'F'

print(letter_grade)