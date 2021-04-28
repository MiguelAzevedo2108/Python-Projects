from PIL import Image

def secretMessage():
    words = Image.open('word_matrix.png')
    mask = Image.open('mask.png')

    mask = mask.resize((1015,559)) #make mask form same size as words
    mask.putalpha(200) #add transparency

    words.past(mask(0,0),mask)

if __name__ == '__main__':
    secretMessage()

    print('Done!')
