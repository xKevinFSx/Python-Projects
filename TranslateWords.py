from translate import Translator

while True:

    to_lang = input('Digite para qual idioma deverá ser traduzido\n' +
                    'pt para Português\n' +
                    'es para Espanhol\n' +
                    'zh para Chinês\n' +
                    'de para Alemão\n')

    tradutor = Translator(to_lang=to_lang)

    print('Digita a palavra ou frase')

    frase = tradutor.translate(input(''))

    print(frase + '\n')
    
    print('Deseja traduzir mais? (S/N)')
    
    resp = input()
    if resp == 'N':
        break
