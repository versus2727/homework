while True:    
    x = input("\nВведите строку:\n")

    if len(x) >= 20:
  
        soglas = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z",]
        latbukv = 0

        for x in x:
            if x in soglas:
                latbukv += 1

        print("\nСогласных латинских прописных букв в строке:")
        print(latbukv)
        break

    else:
        print("\nВпишите строку длиной не менее 20 символов")
        continue