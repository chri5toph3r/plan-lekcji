from tkinter import *
import main


class Window(main.Plan):
    def __init__(self):
        super().__init__()
        self.win_title = 'Plan Lekcji'
        # 1080x2340
        # 415x900
        # 277x600
        self.win_width = 415
        self.win_height = 900

        # create window
        self.root = Tk()
        self.root.title(self.win_title)
        self.root.geometry(f'{self.win_width}x{self.win_height}')

        # main frame idk if I need it, it'll be here for now
        # maybe I'll delete it later
        self.main_frame = Frame()
        self.main_frame.grid()

        self.read_plan()

        self.selected_day = StringVar()
        self.selected_hour = StringVar()
        self.selected_subject = StringVar()
        self.selected_classroom = StringVar()

        self.default_view()

    def clear_frame(self):
        for widgets in self.main_frame.winfo_children():
            widgets.destroy()
        self.menulist_clear_all()
        return

    def top_bar_create(self, toggle_btn=None, edit_btn=None):
        if toggle_btn is None:
            # toggle view button
            toggle_view_btn = Button(self.main_frame, text=f'toggle view')
            toggle_view_btn.grid(column=0, row=0)
        elif toggle_btn == 'add_hour':
            # add hour clear form
            add_hour_clear_btn = Button(self.main_frame, text=f'[+]', command=self.add_hour_view)
            add_hour_clear_btn.grid(column=0, row=0)

        if edit_btn is not None:
            # edit plan button
            edit_btn = Button(self.main_frame, text=edit_btn, command=self.edit_plan_view)
            edit_btn.grid(column=1, row=0)
        else:
            # exit edit plan view button
            edit_btn = Button(self.main_frame, text=f'[X]', command=self.default_view)
            edit_btn.grid(column=1, row=0)
        return

    def default_view(self):

        self.clear_frame()
        self.top_bar_create(edit_btn='edit')

        plan_labels = {}

        for day in self.plan:
            # define day label
            plan_labels[day] = Label(self.main_frame, text=day)
            plan_labels[day].grid(column=0)

            for hour in self.plan[day]:
                # define lesson hour label
                hour_desc = f'{hour} | {self.plan[day][hour][0]} ({self.plan[day][hour][1]})'
                plan_labels[day, hour] = Label(self.main_frame, text=hour_desc)
                plan_labels[day, hour].grid(column=0)
        return

    def edit_plan_view(self):

        self.clear_frame()
        self.top_bar_create(toggle_btn='add_hour')

        plan_labels = {}
        add_btns = {}

        for day in self.plan:
            # define day label
            plan_labels[day] = Label(self.main_frame, text=day)
            plan_labels[day].grid(column=0)

            last_hour = 0
            school = 'normalna'
            for hour in self.plan[day]:
                # define lesson hour label
                hour_desc = f'{hour} | {self.plan[day][hour][0]} ({self.plan[day][hour][1]})'
                plan_labels[day, hour] = Label(self.main_frame, text=hour_desc)
                plan_labels[day, hour].grid(column=0)
                last_hour += 1

            if last_hour > 10:
                school = 'muzyczna'
                last_hour = 0

            # add hour button
            add_btns[day] = Button(self.main_frame,
                                   text=f'{self.hours[school][last_hour]} [+]',
                                   command=lambda: self.add_hour_view(day, self.hours[school][last_hour]))
            add_btns[day].grid(column=0)
        return

    def add_menulist(self, menu_label, menu_list, menu_variable):
        selection = Menubutton(self.main_frame, text=menu_label, activebackground='light grey')
        selection.menu = Menu(selection, tearoff=0)

        for d in menu_list:
            selection.menu.add_radiobutton(label=d, value=d, variable=menu_variable)

        selection['menu'] = selection.menu
        selection.grid(column=0)

        return selection

    def menulist_clear_all(self):
        self.selected_day.set('')
        self.selected_hour.set('')
        self.selected_subject.set('')
        self.selected_classroom.set('')
        return

    def add_hour(self):

        # self.write_in_plan(self.selected_day, self.selected_hour, self.selected_subject, self.selected_classroom)

        # clear all variables
        self.menulist_clear_all()

        return

    def add_hour_view(self, day=None, hour=None, subject_classroom=(None, None)):
        self.clear_frame()
        self.top_bar_create(edit_btn='[X]', toggle_btn=False)

        if day is not None:
            self.selected_day.set(day)
        if hour is not None:
            self.selected_hour.set(hour)
        if subject_classroom != (None, None):
            self.selected_subject.set(str(subject_classroom[0]))
            self.selected_classroom.set(str(subject_classroom[1]))

        day_menu = self.add_menulist('day', self.days, self.selected_day)
        hour_menu = self.add_menulist('hour', self.hours['normalna'], self.selected_hour)
        subject_menu = self.add_menulist('subject', self.subjects['normalna'], self.selected_subject)
        classroom_menu = self.add_menulist('classroom', self.classrooms['normalna'], self.selected_classroom)

        add_hour_btn = Button(self.main_frame, text='add hour', command=self.add_hour)
        add_hour_btn.grid(column=0)

        return


if __name__ == '__main__':
    win = Window()
    win.root.mainloop()
