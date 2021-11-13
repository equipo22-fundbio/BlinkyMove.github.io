from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class panel(App):


    def build(self):

        layout = GridLayout(cols=2)

        layout.add_widget(Button
                          (text='Vamos a comer',
                           size_hint_x=None,
                           width=400))

        layout.add_widget(Button(text='Quiero ir al baño'))

        layout.add_widget(Button
                          (text='Hola',
                           size_hint_x=None,
                           width=400))

        layout.add_widget(Button(text='Tengo sed'))

        # 3rd row
        layout.add_widget(Button
                          (text='Iré a dormir',
                           size_hint_x=None,
                           width=400))

        layout.add_widget(Button(text='Tengo frío'))


        # returning the layout
        return layout




if __name__ == '__main__':
	panel().run()