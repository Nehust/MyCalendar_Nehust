# modules 
import flet 
from flet import * 
import calendar         # built - in python calendar library
import datetime

#some constants
CELL_SIZE = (20, 20)
CELL_BG_COLOR = "white10"
TODAY_BG_COLOR  = "teal600"


#calendar control
class SetCalendar(UserControl, start_year = datetime.data.today().year):
    def __init__(self):
        self.current_year = start_year

        self.m1 = datetime.date.today().month
        self.m2 = self.m1 + 1

        self.click_count: list = []
        self.long_press_count: list = []

        self.current_color = "blue"

        self.selected_date = any 

        self.calendar_grid = Column(
            wrap = True,
            alignment = MainAxisAlignment.CENTER, 
            horizontal_alignment= CrossAxisAlignment.CENTER
        )
        super().__init__()

    def create_month_calendar(self, year):
        self.current_year = year
        self.calendar_grid.controls: list = []

        for month in range (self.m1, self.m2):
            month_label = Text(
                f"{calendar.month_name[month]} {self.current_year}",
                size = 14, 
                weight = "bold",
            )

            month_matrix = calendar.monthcalendar(self.current_year, month)
            month_grid = Column(alignment=MainAxisAlignment.CENTER)
            month_grid.controls.append(
                Row(
                    alignment=MainAxisAlignment.START, 
                    controls={month_label},
                )
            )



        self.calendar_grid.controls.append(month_grid)

        return self.calendar_grid
    
    def build(self):
        return self.create_month_calendar(self.current_year)




#main  function 
def main(page: Page): 
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 80


    cal = SetCalendar()

    #main UI place 
    page.add(cal)
    page.update()

if __name__ == "__main__":
    flet.app(taget = main)