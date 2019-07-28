from kivy.app import App
from kivy.core.text import Label
from kivy.clock import Clock


class timer():
    def work1(self):
        print("Bla")


class arge(App):

    def build(self):
        my_label = Label(text="Plantopedia")
        Clock.schedule_once(timer.work1, 5)
        return my_label


if __name__ == "__main__":
    app = arge()
    app.run()