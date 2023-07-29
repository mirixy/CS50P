def starts_with_two_letters(s):
    return s[:2].isalpha()

def has_valid_length(s):
    return 2 <= len(s) <= 6

def no_middle_numbers(s):
    for i in range(1, len(s) - 1):
        if s[i].isdigit():
            return False
    return True

def valid_end_numbers(s):
    if s[-1].isdigit() and s[0] != '0':
        return True
    return False

def no_punctuation(s):
    return s.isalnum()

def is_valid(s):
    if starts_with_two_letters(s) and has_valid_length(s) and valid_end_numbers(s) and no_punctuation(s):
        return True
    return False

def main():
    vanity_plate = input("Enter a vanity plate: ")
    if is_valid(vanity_plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
