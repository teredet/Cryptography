from kivy.app import App
from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.togglebutton import ToggleButton


ciphers = [f'test{i}' for i in range(20)]


class CryptographyApp(App):


    def build(self):
        Window.size = (700, 500)

        root = BoxLayout(orientation='horizontal', padding=3)

        left = ScrollView(size_hint=[.4,1])
        right = BoxLayout(orientation='vertical')

        LeftGrid = GridLayout(cols=1, size_hint_y=None)
        LeftGrid.bind(minimum_height=LeftGrid.setter('height'))

        self.toggle = ['0' for _ in range(len(ciphers))]
        
        for i in range(len(ciphers)):
            self.toggle[i] = ToggleButton(
                text=ciphers[i], group='cipher',
                height=30, state='normal', size_hint_y=None)
            LeftGrid.add_widget(self.toggle[i])


        left.add_widget(LeftGrid)

        root.add_widget(left)

        return root

if __name__ == '__main__':
    CryptographyApp().run()