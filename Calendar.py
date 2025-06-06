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
        self.frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
        self.frame.pack()
    def on_date_click(self, event, day):
        if day != 0:
            print(f"Clicked date: {self.current_year}-{self.current_month:02d}-{day:02d}")

    frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
    frame.pack()
    def draw_line():
            for i in range(7):
                frame.columnconfigure(i, weight=1)
            for i in range(7):
                frame.rowconfigure(i, weight=1)

    def start_Calendar(self):
        def get_day_color(day):
            return "red" if day in ["Sun", "Sat"] else "black"
       

        cal = calendar.Calendar(firstweekday=6)  
        month_days = cal.monthdayscalendar(self.current_year, self.current_month)
        while len(month_days) < 6:
            month_days.append([0] * 7)

        root = tk.Tk()
        root.title("Calendar - {:04d}-{:02d}".format(self.current_year, self.current_month))
        root.configure(bg=BG_COLOR)

        frame = tk.Frame(root, bg=BG_COLOR, padx=20, pady=20)
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

        for row in range(6):  # 0 ~ 5
            for col in range(7):  # 0 ~ 6
                day_num = month_days[row][col]
                text = str(day_num) if day_num != 0 else ""
                cell = tk.Label(
                    frame,
                    text=text,
                    font=("Helvetica", 16),
                    bg="white",
                    width=10,
                    height=4,
                    relief="solid",
                    bd=1
                )
                cell.grid(row=row + 1, column=col, sticky="nsew")
                cell.bind("<Button-1>", lambda e, d=day_num: self.on_date_click(e, d))

        root.mainloop()
        
a = Calendar()
a.start_Calendar()