numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]

numbers.append(49)
numbers.insert(3, 78)

numbers.sort()
numbers.reverse()

letters.sort()
letters.reverse()

print(letters.count("a"))

print(val)