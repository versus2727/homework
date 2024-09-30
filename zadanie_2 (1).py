#вариант 9
while True:    
    x = input("\nВведите строку:\n")

    if len(x) >= 20:
  
        x = ''.join([x * 2 if x != ' ' else x for x in x])

        print("\nИзменённая строка выглядит так:")
        print(x)
        break

    else:
        print("\nВпишите строку длиной не менее 20 символов")
        continue