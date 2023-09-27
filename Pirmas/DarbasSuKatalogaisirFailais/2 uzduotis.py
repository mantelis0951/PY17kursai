while True:
    try:
        input_line = input("Iveskite norima eiluciu kieki")
        if not input_line:
            break
        input_line = int(input_line)
        sentences = []
        for words in range(input_line):
            input_text = input(f"Irasykite {words+1} teksta: ")
            sentences.append(input_text)
        filename = input("Irasykite failo pavadinima: ")
        with open(filename, 'w', encoding='utf-8') as failas:
            for printing in sentences:
                failas.write(f"{printing}\n")
        break
    except ValueError:
        print("Error")
