def main():
  minus1, minus2 = 1, 0
  for _ in range(50):
    print(minus2)
    minus2, minus1 = minus1, minus2 + minus1

main()