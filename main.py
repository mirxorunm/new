from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        # Увеличиваем размер поля ввода и выставляем его наверху
        self.result = TextInput(font_size=48, readonly=True, halign="right", multiline=False, padding=(10, 10))
        layout = GridLayout(cols=4, spacing=2, size_hint=(1, 5), height=500)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'Clear', '0', '+'
        ]

        for button_text in buttons:
            button = Button(text=button_text, pos_hint={'center_x': 0.5, 'center_y': 0.5})
            button.bind(on_press=self.on_button_press)
            layout.add_widget(button)

        # Добавляем кнопку "Backspace" для удаления последнего символа
        backspace_button = Button(text="Delete")
        backspace_button.bind(on_press=self.on_backspace)
        layout.add_widget(backspace_button)



        equals_button = Button(text="=")
        equals_button.bind(on_press=self.on_solution)

        layout.add_widget(equals_button)

        # Добавляем поле ввода на верхнюю часть
        root = GridLayout(rows=2, spacing=2)
        root.add_widget(self.result)
        root.add_widget(layout)
        return root

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == "C":
            self.result.text = ""
        else:
            new_text = current + button_text
            self.result.text = new_text

    def clear(self, instance):
        self.result.text = ""

    def on_solution(self, instance):
        text = self.result.text
        try:
            solution = str(eval(self.result.text))
            self.result.text = solution
        except Exception:
            self.result.text = "Ошибка(ronaldo bot)"

    def on_backspace(self, instance):
        current = self.result.text
        new_text = current[:-1]  # Удаляем последний символ
        self.result.text = new_text

if __name__ == '__main__':
    app = CalculatorApp()
    app.run()
