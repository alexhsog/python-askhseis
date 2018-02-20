int_to_roman_list = [[1,"I"],
                     [4,"IV"],
                     [5,"V"],
                     [9,"IX"],
                     [10,"X"],
                     [40,"XL"],
                     [50,"L"],
                     [90,"XC"],
                     [100,"C"],
                     [400,"CD"],
                     [500,"D"],
                     [900,"CM"],
                     [1000,"M"],
                     [10000,"?"]]

roman_number = ''
input_number = int(input("ΔΩΣΕ ΑΡΙΘΜΟ ή ΒΑΛΕ ΜΗΔΕΝ ΓΙΑ ΝΑ ΣΤΑΜΑΤΗΣΕΙ ΤΟ ΠΡΟΓΡΑΜΜΑ:  "))
while input_number != 0:
    while input_number > 0 and input_number <= 9999:
        for i in range(len(int_to_roman_list)):
            if int_to_roman_list[i+1][0] < input_number:
                continue
            elif int_to_roman_list[i+1][0] == input_number:
                roman_number += int_to_roman_list[i+1][1]
                input_number -= int_to_roman_list[i+1][0]
                break
            else:
                roman_number += int_to_roman_list[i][1]
                input_number -= int_to_roman_list[i][0]
                break
    print(roman_number)
    roman_number = ''
    input_number = int(input("ΔΩΣΕ ΑΡΙΘΜΟ ή ΒΑΛΕ ΜΗΔΕΝ ΓΙΑ ΝΑ ΣΤΑΜΑΤΗΣΕΙ ΤΟ ΠΡΟΓΡΑΜΜΑ:  "))
