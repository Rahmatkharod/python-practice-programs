full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if name == "":
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long" 
    if " " in name:
        return "The character name should not contain spaces"
    if not all(isinstance(x, int) for x in [strength, intelligence, charisma]):
        return "All stats should be integers"
    if any(x < 1 for x  in  [strength, intelligence, charisma]):
        return  "All stats should be no less than 1"
    if any(x > 4 for x  in  [strength, intelligence, charisma]) :
        return "All stats should be no more than 4"
    elif strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    
    result = name + "\n"
    result += "STR " + full_dot*strength + empty_dot*(10 - strength) + "\n"
    result += "INT " + full_dot*intelligence + empty_dot*(10 - intelligence)+ "\n"
    result += "CHA " + full_dot*charisma + empty_dot*(10 - charisma)
    return result
print(create_character('Rahmat', 4,1,2))