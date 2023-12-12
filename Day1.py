import re

def calibration(notes):
    listCoords =[]

    number_words = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    def extract_number(note):
        pattern = r'(one|two|three|four|five|six|seven|eight|nine|\d)'
        return [number_words.get(word, word) for word in re.findall(pattern, note)]
    
    for i in range(len(notes)):
        digits = extract_number(notes[i])
        first = digits[0]
        last = digits[-1]
        num = int(first+last)
        listCoords.append(num)
    return sum(listCoords)

# The list of strings
input_lines = []
while True:
    line = input()
    if line:
        input_lines.append(line)
    else:
        break

# The list of strings
strings = input_lines
print(calibration(input_lines))
# Print the list of strings

