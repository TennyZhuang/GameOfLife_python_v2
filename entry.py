from GUI import GUI
from Model import Model
from RepeatableTimer import RepeatableTimer


def main():
    timer = RepeatableTimer(0.3)
    model = Model(timer)
    GUI(model, timer)

if __name__ == '__main__':
    main()