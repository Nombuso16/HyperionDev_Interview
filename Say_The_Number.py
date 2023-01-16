digits = {
    "0": "",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
teens = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
}
tens = {
    "0": "",
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}
number_length = {
    0: "",
    1: "thousand",
    2: "million",
    3: "billion",
    4: "trillion"
}
# _ _ _ , _ _ _
def main(number_list):
    number_str = ""
    number_length = len(number_list)
    if number_length == 3:
        if number_list[1] != "1" and number_list[1] != "0":
            number_str += digits[number_list[0]] + " hundred and " + tens[number_list[1]] + " " + digits[number_list[2]]
        elif number_list[1] == "0":
            number_str += digits[number_list[0]] + " hundred and " + digits[number_list[2]]
        else:
            number_str += digits[number_list[0]] + " hundred and " + teens[number_list[1]+number_list[2]]
    elif number_length == 2:
        if number_list[0] != "1":
            number_str += tens[number_list[0]] + " " + digits[number_list[1]]
        else:
            number_str += teens[number_list[0]+number_list[1]]
    elif number_length == 1:
        if number_list[0] == "0":
            number_str += "zero"
        else:
            number_str += digits[number_list[0]]
    return number_str
def a(number_list):
    number_list = list(str(number_list))
    i = 0
    number_str = ""
    while len(number_list) > 3:
        new_number_str = main(number_list[-3::]) + " " + number_length[i] + ", " + number_str
        number_str = new_number_str
        number_list = number_list[:-3]
        i += 1
    new_number_str = main(number_list) + " " + number_length[i] + ", " + number_str
    number_str = new_number_str
    print(number_str[:-2])
    
if __name__ == "__main__":
    a(100)