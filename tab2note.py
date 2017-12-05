import sys


e_map = {
    '0': "E5",
    '1':"F5",
    '2':"F#5",
    '3':"G5",
    '4':"G#5",
    '5':"A6",
    '6':"Bb6",
    '7':"B6",
    '8':"C6",
    '9':"C#6",
    '10':"D6",
    '11':"D#6",
    '12':"E6",
}
B_map = {
    '0':"B5",
    '1':"C5",
    '2':"C#5",
    '3':"D5",
    '4':"D#5",
    '5':"E5",
    '6':"F5",
    '7':"F#5",
    '8':"G5",
    '9':"G#5",
    '10':"A6",
    '11':"Bb6",
    '12':"B6",
}
G_map = {
    '0':"G4",
    '1':"G#4",
    '2':"A5",
    '3':"Bb5",
    '4':"B5",
    '5':"C5",
    '6':"C#5",
    '7':"D5",
    '8':"D#5",
    '9':"E5",
    '10':"F5",
    '11':"F#5",
    '12':"G5",
}
D_map = {
    '0':"D4",
    '1':"D#4",
    '2':"E4",
    '3':"F4",
    '4':"F#4",
    '5':"G4",
    '6':"G#4",
    '7':"A5",
    '8':"Bb5",
    '9':"B5",
    '10':"C5",
    '11':"C#5",
    '12':"D5",
}
A_map = {
    '0':"A4",
    '1':"Bb4",
    '2':"B4",
    '3':"C4",
    '4':"C#4",
    '5':"D4",
    '6':"D#4",
    '7':"E4",
    '8':"F4",
    '9':"F#4",
    '10':"G4",
    '11':"G#4",
    '12':"A5",
}
E_map = {
    '0':"E3",
    '1':"F3",
    '2':"F#3",
    '3':"G3",
    '4':"G#3",
    '5':"A4",
    '6':"Bb4",
    '7':"B4",
    '8':"C4",
    '9':"C#4",
    '10':"D4",
    '11':"D#4",
    '12':"E4",
}

def get_string_map(s):
    return {
        'e': e_map,
        'B': B_map,
        'G': G_map,
        'D': D_map,
        'A': A_map,
        'E': E_map,
    }.get(s, E_map)

def tab2note(line):
    line=line.strip("\n")
    string_map = get_string_map(line[0])
    notes = []
    skip = False
    line = line[2:]
    for (i, l) in enumerate(line):
        if skip:
            notes.append(string_map[line[i-1]+l])
            skip = False
            continue
        elif l == "1" and not line[i+1] == "-":
            notes.append("")
            skip = True
            continue
        if l == "-":
            notes.append("")
        elif l == "|":
            continue
        else:
            notes.append(string_map[l])
    return notes

def merge_notes(lines):
    notes = []
    for i in range(0, len(lines[0])):
        note = ""
        for j in range(0, len(lines)):
            note += lines[j][i]
        notes.append(note)
    return notes

if __name__ == '__main__':
    file = open(sys.argv[1], "r")
    lines = []
    for line in file.readlines():
        lines.append(tab2note(line))
    notes = merge_notes(lines)
    print [[n,0.5] for n in notes if n != '']
