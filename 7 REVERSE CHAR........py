s = input("Enter a string: ")
reversed_str = ''
for ch in s:
    reversed_str = ch + reversed_str
print("Reversed:", reversed_str)
char = input("Enter character to count: ")
print(f"Count of '{char}':", s.count(char))
old = input("Character to replace: ")
new = input("Replace with: ")
print("Modified string:", s.replace(old, new))
