
import csv
import os


def replace_all(text):
    text = text.replace(' \\" ', '"')
    text = text.replace(' \\n ', "\n")
    text = text.replace(' \\s ', " ")
    text = text.replace(' \\b ', "")
    text = text.replace(' /b ', "")
    text = text.replace(' \\i ', "")
    text = text.replace(' /i ', "")
    text = text.replace(' \\u ', "")
    text = text.replace(' /u ', "")
    return text


def make_all_cards(origin, destiny):
    with open(origin, mode ='r', encoding='utf-8') as file:
        csvFile = csv.reader(file)
        for i, data in enumerate(csvFile):
            question = replace_all(data[1])
            answer = replace_all(data[2])
            path = os.path.join(destiny, "Card " + str(i)) + ".txt"
            with open(path, mode='w', encoding='utf-8') as writer:
                writer.write("Cartão. " + str(i) + ".\n\n")
                writer.write("Questão.\n\n")
                writer.write(question)
                writer.write("\n\n")
                writer.write("{{Pause=6}}")
                writer.write("\n\n")
                writer.write("Resposta.\n\n")
                writer.write(answer)
                writer.write("\n\n")
                writer.write("{{Pause=6}}\n\n")
                writer.write("\n\n")

make_all_cards('data\\aptar.csv', 'C:\\Users\\emuvi\\Downloads')