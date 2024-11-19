def lowercase_at_position(string, position):
    if position < 0 or position >= len(string):
        return "Invalid position"  # Handle out-of-range positions

    return string[:position] + string[position].lower() + string[position+1:]

text = "TARIQ"
new_text = lowercase_at_position(text, 0)
print(new_text)