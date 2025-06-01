class Diary:
    def __init__(self, date, start_time, end_time, to_do):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.to_do = to_do
        with open("./diary.txt", mode = "a", encoding="utf-8") as file:
            new_schedule = str(date) + " " + str(start_time) + '~' + str(end_time) + " " + str(to_do)
            file.write(new_schedule + "\n")


    def append_diarys(self, date, start_time, end_time, to_do):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.to_do = to_do
        with open("./diary.txt", mode = "a", encoding="utf-8") as file:
            new_schedule = str(date) + " " + str(start_time) + '~' + str(end_time) + " " + str(to_do)
            file.write(new_schedule + "\n")
    
    def get_diarys(self):
        with open("./diary.txt", mode = "r", encoding="utf-8") as file:
            schedule = file.read()
            diarys = schedule.split('\n')
            diarys.pop(-1)
        for i in range(len(diarys)):
            print(diarys[i])

    
    def correct_diarys(self, date, start_time, end_time, to_do):
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.to_do = to_do
        with open("diary.txt", "r+", encoding="utf-8") as file:
            diarys = file.readlines()  
            correct_index = int(input("몇번째 일정을 수정할까요?"))
            diarys[correct_index-1] = str(date) + " " + str(start_time) + '~' + str(end_time) + " " + str(to_do) 
            file.seek(0)  
            file.writelines(diarys)

    def delete_diarys(self):
        with open("diary.txt", "r+", encoding="utf-8") as file:
            diarys = file.readlines()  
            correct_index = int(input("몇번째 일정을 삭제할까요?"))
            diarys[correct_index-1] = " " 
            file.seek(0)  
            file.writelines(diarys)
    
    def sort_diarys(self):
        with open("diary.txt", "r+", encoding="utf-8") as file:
            diarys = file.readlines()  
            diarys = sorted(diarys) 
            file.seek(0)  
            file.writelines(diarys)  
            file.truncate()

