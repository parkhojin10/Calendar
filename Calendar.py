import tkinter as tk
import calendar
from datetime import datetime

BG_COLOR = "#f2f2f2"
WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]


class Calendar:  
    def __init__(self):  
        now = datetime.now()  
        self.current_year = now.year  
        self.current_month = now.month  
        self.root = tk.Tk()  
        self.root.title("Calendar - {:04d}-{:02d}".format(self.current_year, self.current_month))  
        self.root.configure(bg=BG_COLOR)  
        
    def on_date_click(self, day):  
        if day != 0:  
            print(f"Clicked date: {self.current_year}-{self.current_month:02d}-{day:02d}")  

    def start_Calendar(self):  
        def get_day_color(day):  
            return "red" if day in ["Sun", "Sat"] else "black"  
        
        def on_button_click():
            label.config(text="일정 추가")
        
        cal = calendar.Calendar(firstweekday=6)  
        month_days = cal.monthdayscalendar(self.current_year, self.current_month)  

        while len(month_days) < 6:  
            month_days.append([0] * 7)  

        frame = tk.Frame(self.root, bg=BG_COLOR, padx=20, pady=20)  
        frame.pack()  

        for col, day in enumerate(WEEKDAYS):  
            label = tk.Label(  
                frame,  
                text=day,  
                font=("Helvetica", 18, "bold"),  
                fg=get_day_color(day),  
                bg="white",  
                width=10,  
                height=2,  
                relief="solid",  
                bd=1  
            )  
            label.grid(row=0, column=col, sticky="nsew")  

        for row in range(6):  
            for col in range(7):  
                day_num = month_days[row][col]  
                text = str(day_num) if day_num != 0 else ""  
                cell = tk.Button(  
                    frame,  
                    text=text,  
                    font=("Helvetica", 16),  
                    bg="white",  
                    width=10,  
                    height=4,  
                    relief="solid",  
                    bd=1,  
                    command= on_button_click   
                )  
                cell.grid(row=row + 1, column=col, sticky="nsew")  

        self.root.mainloop()  

a = Calendar()  
a.start_Calendar()
