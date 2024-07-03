import os
import json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class manager():
    def __init__(self):
        self.json_list = []
        for i in os.listdir():
            if i.endswith(".json"):
                if i != "colors.json":
                    self.json_list.append(i)
        with open("colors.json", "r") as file:
            self.two_commands = json.loads(file.read())

        self.char_list=["Base", "Vinyl", 'Frank', 'Coil', 'Red', 'Tryce','Bel','Rave','Solace','DjCyber','EclipseMember','DevilTheoryMember','FauxWithBoostPack','FleshPrince','Irene','Felix']
        self.character_current = "None"
        
    def reset_assigned(self):
        for i in self.json_list:
            with open(i, "w") as info:
                json.dump({"CharacterToReplace":"None"}, info, ensure_ascii=False, indent=4)
    def save_skin_assigned(self, file):
        with open(file, "w") as info:
            if self.character_current !="None":
                json.dump({"CharacterToReplace": self.character_current}, info, ensure_ascii=False, indent=4)
            info.close()
    def save_color(self):
        with open('..//trpg.brc.boostcolors.cfg', "w") as b_c:
            b_c.write("[Colors]\nconfigPrimaryColor = " + self.two_commands["Boost"]+"\nconfigSecondaryColor = "+ self.two_commands["Slide"])
            b_c.close()
        with open("colors.json", "w") as jfile:
            json.dump({"Boost":self.two_commands["Boost"], "Slide":self.two_commands["Slide"]}, jfile, ensure_ascii=False, indent=4)
            jfile.close()

obj = manager()
#obj.save_skin_assigned()

app = QApplication([])


window = QWidget()

mainline = QHBoxLayout()
right_column = QVBoxLayout()
left_column = QVBoxLayout()
json_hbox = QHBoxLayout()
color_hbox = QHBoxLayout()

choose_skin_button = QPushButton("Choose skin")
clear_char_assigned_button = QPushButton("Clear assigned skins")
boost_color = QPushButton("Boost color: "+ obj.two_commands["Boost"])
slide_color = QPushButton("Slide color: "+ obj.two_commands["Slide"])
run_but = QPushButton("Run game")

skin_list = QListWidget()
for item in obj.json_list:
    skin_list.addItem(item.replace(".json", ""))

json_character_choose = QListWidget()
char_list = ["None"]
for i in obj.char_list:
    char_list.append(i)
for i in char_list:
    json_character_choose.addItem(i)

color_choose = QListWidget()
possible_colors = ['Red', 'Orange', 'Yellow', 'Lime', 'Green', 'Teal', 'LightBlue', 'Blue', 'DarkBlue', 'Purple', 'Indigo', 'Magenta', 'Pink', 'White', 'Gray', 'Black']
for i in possible_colors:
    color_choose.addItem(i)

choose_char = QPushButton("Add character (current:"+obj.character_current+")")



def choose_skin():
    if skin_list.selectedItems():
        obj.save_skin_assigned(skin_list.currentItem().text()+".json")
def boost_color_select():
    if color_choose.selectedItems():
        print(color_choose.currentItem().text())
        obj.two_commands["Boost"] = color_choose.currentItem().text()
        boost_color.setText("Boost color: "+obj.two_commands["Boost"])
        obj.save_color()
def slide_color_select():
    if color_choose.selectedItems():
        obj.two_commands["Slide"] = color_choose.currentItem().text()
        slide_color.setText("Slide color: "+obj.two_commands["Slide"])
        obj.save_color()
def clear_char_assigned():
    global choose_char
    obj.reset_assigned()
    obj.character_current = "None"
    choose_char.setText("Add character (current:"+obj.character_current+")")


def run():
    os.startfile("..\\..\\..\\Bomb Rush Cyberfunk.exe")
    window.close()

def choose_character():
    if json_character_choose.selectedItems():
        obj.character_current = json_character_choose.currentItem().text()
        choose_char.setText("Add character (current:"+obj.character_current+")")


right_column.addWidget(color_choose)

color_hbox.addWidget(boost_color)
color_hbox.addWidget(slide_color)

right_column.addLayout(color_hbox)

right_column.addWidget(run_but)


left_column.addWidget(json_character_choose)
left_column.addWidget(choose_char)

left_column.addWidget(skin_list)
json_hbox.addWidget(choose_skin_button)
json_hbox.addWidget(clear_char_assigned_button)

left_column.addLayout(json_hbox)




mainline.addLayout(left_column)
mainline.addLayout(right_column)

choose_char.clicked.connect(choose_character)
run_but.clicked.connect(run)
boost_color.clicked.connect(boost_color_select)
slide_color.clicked.connect(slide_color_select)
clear_char_assigned_button.clicked.connect(clear_char_assigned)
choose_skin_button.clicked.connect(choose_skin)
window.setLayout(mainline)
window.show()
app.exec_()