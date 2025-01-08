import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QVBoxLayout, QPushButton, QWidget

class Waiting_list_app(QMainWindow):


    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Countdown Tracker")  # Title of the window
        self.setGeometry(100, 100, 600, 400)  # x, y, width, height
        
        
        self.table = QTableWidget()
        
        
        self.table.setColumnCount(3)
        
        self.table.setHorizontalHeaderLabels(["Event Name","Target Date/Time", "Timer"])
        
        self.setCentralWidget(self.table)
        
        self.layout = QVBoxLayout()
        self.button_add = QPushButton("Add Event")
        
        self.layout.addWidget(self.button_add)
        self.layout.addWidget(self.table)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        
        def add_row(self):
            row_count = self.table.rowCount()
            
            self.table.insertRow(row_count)
            
def main():
    app = QApplication(sys.argv)  # Initialize the application, using sys.argv
    window = Waiting_list_app()  # Create the main window
    window.show()  # Display the window
    sys.exit(app.exec_())  # Start the event loop

if __name__ == "__main__":
    main()  # Run the application