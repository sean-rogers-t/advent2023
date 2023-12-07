import re
def calibration2(notes):
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

def calibration1(notes):
    
    listCoords =[]
    
    for i in range(len(notes)):
        first = ""
        last=""
        
        coords=notes[i]
        firstFound = False
        lastFound = False
        coordsReverse = coords[::-1]
        for j in range(len(coords)):
            if coords[j].isdigit() and not firstFound:
                first = coords[j]
                firstFound = True
            if coordsReverse[j].isdigit() and not lastFound:
                last = coordsReverse[j]
                lastFound = True
        val =int(first+last)
        listCoords.append(val)
    
    return sum(listCoords)
# Initialize an empty list to store the strings
strings = []

# Start an infinite loop

input_lines = []
while True:
    line = input()
    if line:
        input_lines.append(line)
    else:
        break

# The list of strings
strings = input_lines
print(calibration2(input_lines))
# Print the list of strings

