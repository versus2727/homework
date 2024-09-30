while True:    
    x = input("\nВведите строку:\n")

    if len(x) >= 20:
  
        glas = ["A", "E", "I", "O", "U", "Y",]
        latbukv = 0

        for x in x:
            if x in glas:
                latbukv += 1

        print("\nГласных латинских прописных букв в строке:")
        print(latbukv)
        break

    else:
        print("\nВпишите строку длиной не менее 20 символов")
        continue