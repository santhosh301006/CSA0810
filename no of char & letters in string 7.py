def count_letters_and_characters(s):
    total_characters = len(s)
    letter_count = sum(1 for char in s if char.isalpha())
    print("Total characters:", total_characters)
    print("Number of letters:", letter_count)
user_input = input("Enter a string: ")
count_letters_and_characters(user_input)
