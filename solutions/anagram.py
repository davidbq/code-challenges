def main(str_1, str_2):
  return str_1.lower() != str_2.lower() and sorted(str_1) == sorted(str_2)

print(main('listen', 'silent'))
print(main('listen', 'listen'))
print(main('listen', 'house'))
print(main('listen', 'Listen'))