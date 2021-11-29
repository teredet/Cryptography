from io import TextIOWrapper
from kivy.app import App
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.codeinput import CodeInput
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton

from ciphers import сaesar_сiplet, vigenere_cipher



def test(mode, message, key):
    return f'Mode: {mode}, message: {message}, key: {key}'

ciphers = {'Caesar Ciplet':сaesar_сiplet, 'Vigenere Cipher':vigenere_cipher, 'test3':test, 'test4':test, }


class CryptographyApp(App):

    def getCipher(self, mode):
        mode_short = mode.text[0]
        if not self.message.text: 
            self.result.text = ":: Message is not found ::"; return
        if not self.key.text: 
            self.result.text = ":: Key is not found ::"; return
        for i in range(len(ciphers)):
            if self.toggle[i].state == 'down':
                self.result.text = ciphers[self.toggle[i].text](mode_short,  self.message.text, self.key.text)
                break
        else:
            self.result.text = ":: Cipher is not chosed ::"; return



    def clear(self, mode):
        self.result.font_size = 14
        self.key.text = ""
        self.message.text = ""
        self.result.text = ""

    def build(self):
        Window.size = (700, 500)

        root = BoxLayout(orientation='horizontal', padding=3)

        left = ScrollView(size_hint=[.4,1])
        right = BoxLayout(orientation='vertical')

        LeftGrid = GridLayout(cols=1, size_hint_y=None)
        LeftGrid.bind(minimum_height=LeftGrid.setter('height'))

        self.toggle = ['0' for _ in range(len(ciphers))]
        
        j = 0
        for i in ciphers.keys():
            self.toggle[j] = ToggleButton(
                text=i, group='cipher',
                height=30, state='normal', size_hint_y=None)
            LeftGrid.add_widget(self.toggle[j])
            j += 1

        left.add_widget(LeftGrid)
        root.add_widget(left)


        topBox = BoxLayout(orientation='horizontal', size_hint=[1,.33])
        self.key = TextInput(hint_text='Key', multiline = False, font_size = 16)
        topBox.add_widget(self.key)

        rightTopBox = BoxLayout(orientation='vertical', size_hint=[.5,1])
        rightTopBox.add_widget(Button(text='Encrypt', on_press = self.getCipher))
        rightTopBox.add_widget(Button(text='Decrypt', on_press = self.getCipher))


        topBox.add_widget(rightTopBox)
        right.add_widget(topBox)

        self.message = TextInput(hint_text='Message', font_size=16)
        right.add_widget(self.message)

        self.result = CodeInput(readonly=True, hint_text='Result', font_size=14, background_color=[1,1,1,.8])
        right.add_widget(self.result)

        downBox = BoxLayout(orientation='horizontal', size_hint=[1,.15])
        downBox.add_widget(Button(text='Clear', on_press = self.clear))

        right.add_widget(downBox)

        root.add_widget(right)

        return root

if __name__ == '__main__':
    CryptographyApp().run()