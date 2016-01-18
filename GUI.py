from tkinter import *
from Observer import Observer


class GUI(Observer):
    def __init__(self, subject, timer):
        Observer.__init__(self, subject)

        self.tk = Tk()
        self.tk.geometry('400x440')
        self.timer = timer

        self.canvas = Canvas(self.tk, bg='white', width=360, height=360)
        self.canvas.place(x=20, y=20)

        self.round_label = Label(self.tk, text="round:0")
        self.round_label.place(x=20, y=396)

        self.start_button = Button(self.tk, text='start', width=8,
                                   command=self.start_button_onclick)
        self.start_button.place(x=316, y=396)

        self.tk.mainloop()

    def start_button_onclick(self):
        self.start_button['state'] = 'disabled'
        self.timer.start()

    def update(self, **kwargs):
        assert 'round' in kwargs and 'map' in kwargs
        self.round_label['text'] = 'round:%d' % kwargs['round']
        self.draw(kwargs['map'])

    def draw(self, map):
        width = float(self.canvas['width'])
        height = float(self.canvas['height'])
        num_of_rows = len(map)
        num_of_cols = len(map[0])
        unit_width = width / num_of_cols
        unit_height = height / num_of_rows

        self.canvas.create_rectangle(0, 0, width, height,
                                     fill='white', outline='white')

        for i in range(num_of_rows):
            for j in range(num_of_cols):
                if (map[i][j] == 1):
                    self.canvas.create_rectangle(
                        j * unit_width,
                        i * unit_height,
                        (j + 1) * unit_width - 1,
                        (i + 1) * unit_height - 1,
                        fill='black',
                        outline='white')
