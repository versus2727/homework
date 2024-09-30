#вармани 10
while True:    
    x = input("\nВведите строку:\n")

    if len(x) >= 20:
        print("\nСимволов в вашей строке =", len(x))
            
        x = x.upper()
        x = x.replace("И", "Ы")
        x = x.center(50)

        print("\nИзменённая строка выглядит так:")
        print(x)
        break

    else:
        print("\nВпишите строку длиной не менее 20 символов")
        continue