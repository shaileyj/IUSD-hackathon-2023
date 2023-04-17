from PyQt6.QtWidgets import QApplication, QMainWindow
import gpt_response
import output

widget = None
json_data = None


class idk():

    def __init__(self):
        self.question_num = 1

    def submit(self):
        right_button = None
        buttons = [widget.radioButton, widget.radioButton_2, widget.radioButton_3, widget.radioButton_4]
        if json_data["questions"][self.question_num - 1]["answer"].upper() == "A":
            right_button = 0
        elif json_data["questions"][self.question_num - 1]["answer"].upper() == "B":
            right_button = 1
        elif json_data["questions"][self.question_num - 1]["answer"].upper() == "C":
            right_button = 2
        elif json_data["questions"][self.question_num - 1]["answer"].upper() == "D":
            right_button = 3

        if buttons[right_button].isChecked():
            widget.label_2.setText("correct!" + json_data["questions"][self.question_num-1]["explanation"])
        else:
            widget.label_2.setText("incorrect." + json_data["questions"][self.question_num-1]["explanation"])

        if self.question_num < 5:
            widget.label.setText(json_data["questions"][self.question_num]["question"])
            buttons = [widget.radioButton, widget.radioButton_2, widget.radioButton_3, widget.radioButton_4]
            for index, option in enumerate(json_data["questions"][self.question_num]["options"]):
                buttons[index].setText(option)
            self.question_num += 1


if __name__ == "__main__":
    subject = input("What subject do you want multiple choice questions on?\n")
    json_data = gpt_response.get_questions(subject)
    app = QApplication([])
    window = QMainWindow()
    widget = output.Ui_MainWindow()
    widget.setupUi(window)
    widget.label.setText(json_data["questions"][0]["question"])
    buttons = [widget.radioButton, widget.radioButton_2, widget.radioButton_3, widget.radioButton_4]
    for index, option in enumerate(json_data["questions"][0]["options"]):
        buttons[index].setText(option)
    thing = idk()
    widget.pushButton_2.clicked.connect(thing.submit)
    window.show()
    app.exec()
