from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.core.window import Window


'''
 #Define the network client
from xrpl.clients import JsonRpcClient
JSON_RPC_URL = "https://s.altnet.rippletest.net:51234/"
client = JsonRpcClient(JSON_RPC_URL)

# Create a wallet using the testnet faucet:
# https://xrpl.org/xrp-testnet-faucet.html
from xrpl.wallet import generate_faucet_wallet
test_wallet = generate_faucet_wallet(client, debug=True)

print(test_wallet)
'''

class ConverterApp(App):
    def build(self):

        Window.clearcolor = (1, 1, 1, 1)

        welcome = Label(text = 'Celsius Farenheit Converter',
                        color = (109, 0, 183, 0.6),
                        font_size = "40sp",
                        bold = True)

        btn = Button(text = "Calculate",
            font_size = "20sp",
            background_color = (109, 0, 183, 0.1),
            color = (109, 0, 183, 0.6),
            size = (100, 100),
            size_hint = (1, 1),
            pos = (200, 200),
            on_press=self.when_pressed)
        
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
        
        b.add_widget(welcome)
        b.add_widget(l)
        b.add_widget(self.t)
        b.add_widget(btn)
        b.add_widget(clear)
        
        b.add_widget(self.a)
        
        #btn.bind(on_press = self.when_pressed)
        return b
    
    def when_pressed(self, obj):
       print(self.t.text, "degrees Celsius equals", round(int(self.t.text)* (9/5)+32, 2), "degrees Farenheit")
       self.a.text = self.a.text + str(round(int(self.t.text) * (9/5)+32, 2)) + " °F"

    def when_clear(self, obj):
        self.a.text = "Answer: "
        self.t.text = ''

       
       

    

root = ConverterApp()

root.run()