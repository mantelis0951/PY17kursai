class Sakinys:
    def __init__(self, sentence):
        self.sentence = sentence

    def reversed_text(self):
        print(f"Tekstas atbulai: {self.sentence[::-1]}")

    def lowercase_text(self):
        print(f"Tekstas mazosiomis: {self.sentence.lower()}")

    def uppercase_text(self):
        print(f"Tekstas didziosiomis: {self.sentence.upper()}")

    def queue_number(self):
        queuelist.append(textinput)
        splitted = textinput.split()
        ##print(splitted)
        input_number = int(input("Irasykite eiles numeri zodziui gauti: "))
        input_number = splitted[input_number-1]
        print(f"Jusu zodis: {input_number}")
        ##print(splitted.index(input_number)+1)

    def symbolsandwords(self):
        words = textinput.split()
        print(f"tekste yra simboliu: {len(self.sentence)}")
        print(f"Tekste yra zodziu: {len(words)}")

    def changesymbolsandwords(self):
        input_sentence = input("Įrašykite tekstą: ")
        print(input_sentence)
        input_word = input("Įrašykite žodį arba simbolį, kurį norite pakeisti: ")

        # Pridedame į sąrašą
        inputwordtolist = [input_sentence, input_word]

        replacement_word = input("Įrašykite žodį arba simbolį, į kurį norite pakeisti: ")

        # Pakeičiame žodžius arba simbolius
        modified_sentence = input_sentence.replace(input_word, replacement_word)

        print("Modifikuotas sakinys:", modified_sentence)





inputfirstword = []

queuelist = []

special_characters = "!@#$%^&*()-+?_=,<>/"

symbolsandwordslist = []

textinput = input("Iveskite zodi: ")
sentence = Sakinys(textinput)

sentence.reversed_text()
sentence.lowercase_text()
sentence.uppercase_text()
sentence.queue_number()
sentence.symbolsandwords()
sentence.changesymbolsandwords()

