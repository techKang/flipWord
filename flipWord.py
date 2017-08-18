# -*- coding:utf-8 -*-

class FlipWord():
    # this class is used to flip words and now don`t support upper character 'BDKQR'
    def __init__(self, str='Test Str'):
        self.str = str
        self.fliped = ''

    def flipWord(self):
        srcChar = 'abcdefghijklmnopqrstuvwxyz'[::-1] + \
                  'abcdefghijklmnopqrstuvwxyz'[::-1].upper() + ','
        flipChar = 'zʎxʍʌnʇsɹbdouɯɿʞſ!ɥƃɟǝpɔqɐZ⅄XMΛ∩⊥SɹbԀONW⅂ʞſIH⅁ℲƎpƆq∀\''
        index = dict(zip(srcChar, flipChar))
        temp = self.str
        while temp != '':
            try:
                tempchar = index[temp[-1]]
                self.fliped += tempchar
            except:
                self.fliped += temp[-1]
            temp = temp[:-1]
        print(self.fliped)


if __name__ == "__main__":
    testClass = FlipWord('Even if I was reversed, I still want to moquan')
    testClass.flipWord()
