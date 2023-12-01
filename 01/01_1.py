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
    result = result + int(findFirstDigitInString(line) + findLastDigitInString(line))
    
print(result)

