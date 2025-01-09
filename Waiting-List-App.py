import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QVBoxLayout, QPushButton, QWidget, QTableWidgetItem
from PyQt5.QtCore import QTimer, Qt  
from datetime import datetime
class Waiting_list_app(QMainWindow):


    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("Countdown Tracker")  
        self.setGeometry(100, 100, 600, 400)  
        
        
        self.table = QTableWidget()
        self.table.setEditTriggers(QTableWidget.AllEditTriggers)
        self.table.setColumnCount(3)
        self.table.cellChanged.connect(self.table_cell_changed)
        self.table.setHorizontalHeaderLabels(["Event Name","Date/Time", "Timer"])
        
        self.setCentralWidget(self.table)
        
        self.layout = QVBoxLayout()
        self.button_add = QPushButton("Add Event")
        self.button_add.clicked.connect(self.add_row)
        
        self.layout.addWidget(self.button_add)
        self.layout.addWidget(self.table)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
        self.timer = QTimer(self)
        self.timer.setInterval(1000)  
        self.timer.timeout.connect(self.update_countdowns)
        self.timer.start()
        
    def add_row(self):
        row_count = self.table.rowCount()   
        self.table.insertRow(row_count)
        self.table.setItem(row_count, 0, QTableWidgetItem("New Event"))
        self.table.setItem(row_count, 1, QTableWidgetItem("YYYY-MM-DD HH:MM"))
        
    def table_cell_changed(self, row, column):
        if column ==1:
            cell_value = self.table.item(row, column).text()
            
            try:
                 
                target_date = datetime.strptime(cell_value, "%Y-%m-%d %H:%M")
            
                
                self.table.setItem(row, 2, QTableWidgetItem("Valid Date"))
            except ValueError:
                
                self.table.setItem(row, 2, QTableWidgetItem("Invalid Date"))
    
    def update_countdowns(self):
          for row in range(self.table.rowCount()):
              target_date_str = self.table.item(row, 1).text()
              
              try: 
                  target_date = datetime.strptime(target_date_str, "%Y-%m-%d %H:%M")
                  current_date = datetime.now()
                  time_diff = target_date - current_date
                  
                  
                  if time_diff.total_seconds() <= 0:
                     self.table.setItem(row, 2, QTableWidgetItem("Congrats, your thing is here now"))
                  else:
                    days = time_diff.days
                    hours, remainder = divmod(time_diff.seconds, 3600)   
                    minutes, seconds = divmod(remainder, 60)
                    time_left = f"{days}d {hours}h {minutes}m {seconds}s"
                    self.table.setItem(row, 2, QTableWidgetItem(time_left))
                    
              except ValueError:
                  self.table.setItem(row, 2, QTableWidgetItem("Invalid Date"))
                  invalid_item = QTableWidgetItem("Invalid Date")
                  invalid_item.setFlags(Qt.ItemIsSelectable)  
                  self.table.setItem(row, 2, invalid_item)  
            
def main():
    app = QApplication(sys.argv)  
    window = Waiting_list_app()  
    window.show()  
    sys.exit(app.exec_())  

if __name__ == "__main__":
    main()  