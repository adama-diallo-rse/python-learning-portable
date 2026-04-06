def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Rule 1: Length between 2 and 6
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Rule 2: All characters must be alphanumeric (no spaces, periods, etc.)
    if not s.isalnum():
        return False
    
    # Rule 3: Must start with at least 2 letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    # Rule 4: Numbers must come at the end, and first number can't be 0
    # Find where numbers start
    first_digit_index = -1
    for i, char in enumerate(s):
        if char.isdigit():
            first_digit_index = i
            break
    
    # If there are digits
    if first_digit_index != -1:
        # First digit can't be 0
        if s[first_digit_index] == '0':
            return False
        
        # All characters after first digit must be digits
        for i in range(first_digit_index, len(s)):
            if not s[i].isdigit():
                return False
    
    return True


main()
