from system.core.controller import *
from time import strftime

class Time(Controller):
    def __init__(self, action):
        super(Time, self).__init__(action)
        self.load_model('TimeModel')
        self.db = self._app.db

    def display(self):
        time = strftime("%B %wth, %Y - %I:%M %p")
        return self.load_view('display.html', time=time)
