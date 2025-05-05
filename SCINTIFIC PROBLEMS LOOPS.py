for i in range(1, 11):
    print(i**2, end=' ')  # square numbers
print("\nNumber Pattern:")
for i in range(1, 6):
    print(" ".join(str(j) for j in range(1, i+1)))
print("Pyramid Pattern:")
for i in range(1, 6):
    print(' ' * (5 - i) + '* ' * i)
