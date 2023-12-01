string_to_number = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def rewriteStringWithDigits(input: str) -> str:
    for k, v in string_to_number.items():
        input = input.replace(k, v)
        if k == "one":
            input = input.replace("1ight", "1eight")
            input = input.replace("tw1", "two1")
        if k == "two":
            input = input.replace("2ne", "2one")
            input = input.replace("eigh2", "eight2")
        if k == "seven":
            input = input.replace("7ine", "7nine")
        if k == "eight":
            input = input.replace("8wo", "8two")

    return input

def findFirstDigitInString(input: str) -> str:
    for character in input:
        if character.isdigit():
            return character
        
    return None

def findLastDigitInString(input: str) -> str:
    for character in input:
        if character.isdigit():
            lastdigit = character

    try:
        return lastdigit
    except:
        return None

digit_list = []
result = 0
with open("input.txt", "r") as f:
    input_list = f.readlines()

for line in input_list:
    line = rewriteStringWithDigits(line)
    print(line)
    first_digit = findFirstDigitInString(line)
    last_digit = findLastDigitInString(line)

    print(first_digit + "" + last_digit)
    result = result + int(first_digit + last_digit)
    
print(result)

