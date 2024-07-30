from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.graphics import Color, Line, RoundedRectangle
from kivy.core.window import Window
class MySlider(BoxLayout):
    def __init__(self, **kwargs):
        super(MySlider, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10  # Add padding to the BoxLayout
        self.spacing = 10
        with self.canvas.before:
            Color(0, 0.5, 1)  # Red color for the outline
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[10])
            self.outline = Line(width=2, rounded_rectangle=(self.x, self.y, self.width, self.height, 0, 10, 10, 10))
            self.bind(pos=self.update_rect, size=self.update_rect)
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.outline.rounded_rectangle = (self.x, self.y, self.width, self.height, 10, 10, 10, 10)
class MyApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        # Create a TextInput widget
        self.text_input = TextInput(size_hint=(1, 0.2))
        main_layout.add_widget(self.text_input)


        # Create a horizontal BoxLayout for sliders and buttons
        content_layout = BoxLayout(orientation='horizontal', spacing=10)


        # Create a vertical BoxLayout for sliders and labels
        slider_layout = BoxLayout(orientation='vertical', spacing=20)


        # Create sliders with labels
        self.temperature_slider_box = MySlider(size_hint=(1, None), height=100)
        self.temperature = Slider(min = 0, max = 100, value = 0, size_hint=(1, 0.2))
        self.temperature_label = Label(text="Temperature", size_hint=(1, 0.2), bold=True)
        self.temperature_value = Label(text=str(self.temperature.value), size_hint=(1, 0.2))
        self.temperature.bind(value=self.update_value_label(self.temperature_value))

        self.temperature_slider_box.add_widget(self.temperature)
        self.temperature_slider_box.add_widget(self.temperature_label)
        self.temperature_slider_box.add_widget(self.temperature_value)
        slider_layout.add_widget(self.temperature_slider_box)

 
        ''''
        for label_text in ["Temperature", "Friction Value", "Bounce Effect", "Ricochet Value"]:
            slider_box = MySlider(size_hint=(1, None), height=100)
            label = Label(text=label_text, size_hint=(1, 0.2), bold=True)
            slider = Slider(min=0, max=100, value=0, size_hint=(1, 0.5))
            self.value_label = Label(text=str(slider.value), size_hint=(1, 0.2))
            slider.bind(value=self.update_value_label(self.value_label))

            slider_box.add_widget(label)
            slider_box.add_widget(slider)
            slider_box.add_widget(self.value_label)
            slider_layout.add_widget(slider_box)
        '''

        # Create a vertical BoxLayout for buttons
        button_layout = BoxLayout(orientation='vertical', spacing=10)
        button1 = Button(text="Button 1", size_hint=(1, 0.4))
        button2 = Button(text="Button 2", size_hint=(1, 0.4))
        button3 = Button(text="Button 3", size_hint=(1, 0.4))
        clear = Button(text = "Clear", size_hint=(1, 0.4) )
        self.label1 = Label(text = '')


        #binding actions to the buttons
        button1.bind(on_press=self.on_button1_click)
        button2.bind(on_press=self.on_button2_click)
        button3.bind(on_press=self.on_button3_click)
        clear.bind(on_press=self.on_clear_click)

        # adding buttons to the widget
        button_layout.add_widget(button1)
        button_layout.add_widget(button2)
        button_layout.add_widget(button3)
        button_layout.add_widget(clear)
        button_layout.add_widget(self.label1)

        # Add the two vertical BoxLayouts to the horizontal BoxLayout
        content_layout.add_widget(slider_layout)
        content_layout.add_widget(button_layout)
        # Add the horizontal BoxLayout to the main layout
        main_layout.add_widget(content_layout)
        return main_layout
    
    #functions binded to the diff buttons
    def on_button1_click(self, instance):
        self.label1.text += "Temperature: " + str(round(self.temperature.value, 2))
    def on_button2_click(self, instance):
        self.label1.text = "Button 2 clicked! Text: " + self.text_input.text
    def on_button3_click(self, instance):
        #self.label1.text = "Button 3 clicked! Text: " + self.text_input.text
        self.temperature.value += 1
    def on_clear_click(self, instance):
        self.label1.text = ""
        self.temperature.value = 0
    def update_value_label(self, label):
        def update(instance, value):
            label.text = str(int(value))
            self.label1.text = str(round(self.temperature.value, 1))
            
        return update
    

    

if __name__ == '__main__':
    MyApp().run()
 
 