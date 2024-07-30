from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class TicTacToe(App):
    def build(self):
        self.active_player = 1
        Window.clearcolor = (1, 1, 1, 1)

        layout = GridLayout(cols = 3)
        welcome = Label(text = 'Welcome to Tic Tac Toe!!',
                        color = (109, 0, 183, 0.6),
                        font_size = "20sp",
                        bold = True)

        self.r1c1 = Button(text = " ",
                        font_size = "200sp",
                      on_press = self.when_pressed_r1c1)
        self.r1c2 = Button(text = " ",
                      font_size = "200sp",
                      on_press = self.when_pressed_r1c2)
        
        
        self.r1c3 = Button(text = " ",
                      font_size = "200sp",
                      on_press = self.when_pressed_r1c3)
        self.r2c1 = Button(text = " ",
                      font_size = "200sp",
                      on_press = self.when_pressed_r2c1)
        self.r2c2 = Button(text = " ",
                      font_size = "200sp",
                      on_press = self.when_pressed_r2c2)
        self.r2c3 = Button(text = " ",
                      font_size = "200sp",
                      on_press = self.when_pressed_r2c3)
        self.r3c1 = Button(text = " ",
                      font_size = "200sp",
                      on_press = self.when_pressed_r3c1)
        self.r3c2 = Button(text = " ",
                      font_size = "200sp",
                      on_press = self.when_pressed_r3c2)
        self.r3c3 = Button(text = " ",
                      font_size = "200sp",
                      on_press = self.when_pressed_r3c3)
        
        layout.add_widget(self.r1c1)
        layout.add_widget(self.r1c2)   
        layout.add_widget(self.r1c3)
        layout.add_widget(self.r2c1)
        layout.add_widget(self.r2c2)
        layout.add_widget(self.r2c3)
        layout.add_widget(self.r3c1)
        layout.add_widget(self.r3c2)
        layout.add_widget(self.r3c3)
        
        
        clear = Button(text = "clear",
            font_size = "20sp",
            background_color = (1, 1, 1, 1),
            color = (1, 1, 1, 1),
            size = (100, 100),
            size_hint = (1, .7),
            pos = (0.4, 0.4),
            on_press=self.when_clear)


        b = BoxLayout(orientation = 'vertical')
        l = Label(text = "Enter temperature in Celsius: ",
                  color = (109, 0, 183, 0.6))
        self.a = Label(text = "Answer: ",
                       font_size = "30sp",
                       color = (109, 0, 183, 0.6))

        self.t = TextInput(text = ' ',
            font_size = 30,
            foreground_color = (109, 0, 183, 0.6),
            size_hint_y = None,
            height = 100)
        
        #self.convert = int(self.t.text) * (9/5)+32
        
        ''''
        b.add_widget(welcome)
        b.add_widget(l)
        b.add_widget(self.t)
        b.add_widget(btn)
        b.add_widget(clear)
        
        b.add_widget(self.a)
        '''
        #btn.bind(on_press = self.when_pressed)
        return layout
    
    def when_pressed_r1c1(self, obj):
        finished = False
        while not(finished):
            if (self.active_player % 2) == 1:
                self.r1c1.text = "x"
                finished = True
            else:
                self.r1c1.text = "o"
                finished = True

            self.active_player += 1

    def when_pressed_r1c2(self, obj):
        finished = False
        while not(finished):
            if (self.active_player % 2) == 1:
                self.r1c2.text = "x"
                finished = True
            else:
                self.r1c2.text = "o"
                finished = True
            self.active_player += 1

    def when_pressed_r1c3(self, obj):
        finished = False
        while not(finished):
            if (self.active_player % 2) == 1:
                self.r1c3.text = "x"
                finished = True
            else:
                self.r1c3.text = "o"
                finished = True
            self.active_player += 1

    def when_pressed_r2c1(self, obj):
        finished = False
        while not(finished):
            if (self.active_player % 2) == 1:
                self.r2c1.text = "x"
                finished = True
            else:
                self.r2c1.text = "o"
                finished = True
            self.active_player += 1
    
    def when_pressed_r2c2(self, obj):
        finished = False
        while not(finished):
            if (self.active_player % 2) == 1:
                self.r2c2.text = "x"
                finished = True
            else:
                self.r2c2.text = "o"
                finished = True
            self.active_player += 1

    def when_pressed_r2c3(self, obj):
        finished = False
        while not(finished):
            if (self.active_player % 2) == 1:
                self.r2c3.text = "x"
                finished = True
            else:
                self.r2c3.text = "o"
                finished = True
            self.active_player += 1

    def when_pressed_r3c1(self, obj):
        finished = False
        while not(finished):
            if (self.active_player % 2) == 1:
                self.r3c1.text = "x"
                finished = True
            else:
                self.r3c1.text = "o"
                finished = True
            self.active_player += 1

    def when_pressed_r3c2(self, obj):
        finished = False
        while not(finished):
            if (self.active_player % 2) == 1:
                self.r3c2.text = "x"
                finished = True
            else:
                self.r3c2.text = "o"
                finished = True
            self.active_player += 1

    def when_pressed_r3c3(self, obj):
        finished = False
        while not(finished):
            if (self.active_player % 2) == 1:
                self.r3c3.text = "x"
                finished = True
            else:
                self.r3c3.text = "o"
                finished = True
            self.active_player += 1
       

    def when_clear(self, obj):
        self.a.text = "Answer: "
        self.t.text = ''

       
       

    

root = TicTacToe()

root.run()