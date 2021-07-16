from translate import Translator

translator = Translator(to_lang='ita')
with open('./input.txt') as input_file:
    text = input_file.read()
    translation = translator.translate(text)

with open('./output.txt', 'w') as output_file:
    output_file.write(translation)
