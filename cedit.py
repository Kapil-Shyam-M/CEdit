#!/usr/bin/python3.8


"""
CEDIT-A Python-Based Text Editor
"""
#########################################################################
#  Project           		:   CEDIT-A PYTHON BASED TEXT EDITOR
#  Name of the file	     	:   cedit.py
#  Brief Description of file   :   Main File for CEdit
#  Name                        :   KAPIL SHYAM.M 
#  Email ID                    :   cedit.ceo@gmail.com
#                                                                       #
#                                                                       #
#########################################################################

"""

CEDIT-A Python-Based Text Editor, is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CEDIT-A Python-Based Text Editor, is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import os
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
from cemodules import ceterm

PROGRAM_NAME = "CEdit"
file_name = None

root = Tk()
root.geometry('1200x700+200+150')
root.title(PROGRAM_NAME)

def show_popup_menu(event):
    popup_menu.tk_popup(event.x_root, event.y_root)


def show_cursor_info_bar():
    show_cursor_info_checked = show_cursor_info.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')
    else:
        cursor_info_bar.pack_forget()


def update_cursor_info_bar(event=None):
    row, col = content_text.index(INSERT).split('.')
    line_num, col_num = str(int(row)), str(int(col) + 1)
    infotext = "Line: {0} | Column: {1}".format(line_num, col_num)
    cursor_info_bar.config(text=infotext)


def change_theme(event=None):
    selected_theme = theme_choice.get()
    fg_bg_colors = color_schemes.get(selected_theme)
    foreground_color, background_color = fg_bg_colors.split('.')
    content_text.config(
        background=background_color, fg=foreground_color)


def update_line_numbers(event=None):
    line_numbers = get_line_numbers()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0', 'end')
    line_number_bar.insert('1.0', line_numbers)
    line_number_bar.config(state='disabled')


def highlight_line(interval=100):
    content_text.tag_remove("active_line", 1.0, "end")
    content_text.tag_add(
        "active_line", "insert linestart", "insert lineend+1c")
    content_text.after(interval, toggle_highlight)


def undo_highlight():
    content_text.tag_remove("active_line", 1.0, "end")


def toggle_highlight(event=None):
    if to_highlight_line.get():
        highlight_line()
    else:
        undo_highlight()


def on_content_changed(event=None):
    update_line_numbers()
    update_cursor_info_bar()


def get_line_numbers():
    output = ''
    if show_line_number.get():
        row, col = content_text.index("end").split('.')
        for i in range(1, int(row)):
            output += str(i) + '\n'
    return output


def display_about_messagebox(event=None):
    tkinter.messagebox.showinfo("About", "{}{}".format(PROGRAM_NAME, "\n\nIt is an Open-Source Initiative by thhe student of Meenakshi College of Engineering.\n\n +This can be used as a notepad also.\n\n +This is a project made fully using Python.\n\n +This is available for Unix/linux and Windows Systems having Python installed on them.."))


def display_contactus_messagebox(event=None):
    tkinter.messagebox.showinfo("Contact Us", "{}{}".format(PROGRAM_NAME, "\n You Can Always Contact Us using the email address given below....\n\n\tcedit.ceo@gmail.com"))


def display_download_messagebox(event=None):
    tkinter.messagebox.showinfo("Download", "{}{}".format(PROGRAM_NAME, "\n\nYou Can Always Download CEDIT from the following Repository:\n\thttps://bitbucket.org/Kapil_Shyam_M/cedit/src/master/\n\n STEPS:\n\n 1. Go to Downloads tab in CEdit repository.\n\n 2. Download the file named Download Repository.\n\n 3. Now you have successfully downloaded the project\n"))        


def display_contribute_messagebox(event=None):
    tkinter.messagebox.showinfo("Contribute", "{}{}".format(PROGRAM_NAME, "\n\nYou Can Always Contribute to CEDIT by creating a Pull Request or an Issue from the following Repository:\n\n https://bitbucket.org/Kapil_Shyam_M/cedit/src/master/\n"))


def display_help_messagebox(event=None):
    tkinter.messagebox.showinfo("Help", "Help Book: \n Page will be updated\n\tsoon", icon='question')
        
        
def exit_editor(event=None):
    if tkinter.messagebox.askokcancel("Quit?", "Do you want to QUIT for sure?\n"):
        root.destroy()


def new_file(event=None):
    root.title("Untitled")
    global file_name
    file_name = None
    content_text.delete(1.0, END)
    on_content_changed()


def open_file(event=None):
    input_file_name = tkinter.filedialog.askopenfilename(defaultextension=".txt",
                                                         filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"), ("Python","*.py"), ("HTML","*.html"), ("Bash","*.sh"), ("Assembly","*.S"), ("Go","*.go"), ("C","*.c"), ("C++","*.cpp"), ("Java", "*.java"), ("Rust","*.rs"), ("Ruby","*.RUBY")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
        content_text.delete(1.0, END)
        with open(file_name) as _file:
            content_text.insert(1.0, _file.read())
        on_content_changed()


def write_to_file(file_name):
    try:
        content = content_text.get(1.0, 'end')
        with open(file_name, 'w') as the_file:
            the_file.write(content)
    except IOError:
        tkinter.messagebox.showwarning("Save", "Could not save the file.")


def save_as(event=None):
    input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension=".txt",
                                                           filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"), ("Python","*.py"), ("HTML","*.html"), ("Bash","*.sh"), ("Assembly","*.S"), ("Go","*.go"), ("C","*.c"), ("C++","*.cpp"), ("Java", "*.java"), ("Rust","*.rs"), ("Ruby","*.RUBY")])
    if input_file_name:
        global file_name
        file_name = input_file_name
        write_to_file(file_name)
        root.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
    return "break"


def save(event=None):
    global file_name
    if not file_name:
        save_as()
    else:
        write_to_file(file_name)
    return "break"


def select_all(event=None):
    content_text.tag_add('sel', '1.0', 'end')
    return "break"


def find_text(event=None):
    search_toplevel = Toplevel(root)
    search_toplevel.title('Find Text')
    search_toplevel.transient(root)

    Label(search_toplevel, text="Find All:").grid(row=0, column=0, sticky='e')

    search_entry_widget = Entry(
        search_toplevel, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_toplevel, text='Ignore Case', variable=ignore_case_value).grid(
        row=1, column=1, sticky='e', padx=2, pady=2)
    Button(search_toplevel, text="Find All", underline=0,
           command=lambda: search_output(
               search_entry_widget.get(), ignore_case_value.get(),
               content_text, search_toplevel, search_entry_widget)
           ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

    def close_search_window():
        content_text.tag_remove('match', '1.0', END)
        search_toplevel.destroy()
    search_toplevel.protocol('WM_DELETE_WINDOW', close_search_window)
    return "break"


def search_output(needle, if_ignore_case, content_text,
                  search_toplevel, search_box):
    content_text.tag_remove('match', '1.0', END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos,
                                            nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break
            end_pos = '{}+{}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config(
            'match', foreground='red', background='yellow')
    search_box.focus_set()
    search_toplevel.title('{} matches found'.format(matches_found))

def ceterminal():
    ceterm.ceterm()
    return "break"


def cut():
    content_text.event_generate("<<Cut>>")
    on_content_changed()
    return "break"


def copy():
    content_text.event_generate("<<Copy>>")
    return "break"


def paste():
    content_text.event_generate("<<Paste>>")
    on_content_changed()
    return "break"


def undo():
    content_text.event_generate("<<Undo>>")
    on_content_changed()
    return "break"


def redo(event=None):
    content_text.event_generate("<<Redo>>")
    on_content_changed()
    return 'break'
    
def callback(selection):
    var=selection
    
    if var=="Select Language":
        program=' Please Select an Appropriate Language...'
        content_text.delete(1.0,END)
        content_text.insert(END, program)
        
    elif var=="Assembly":
        program='''section	.text
   global_start   ;must be declared for linker (ld)
	
_start:	          ;tells linker entry point
   mov	edx,len   ;message length
   mov	ecx,msg   ;message to write
   mov	ebx,1     ;file descriptor (stdout)
   mov	eax,4     ;system call number (sys_write)
   int	0x80      ;call kernel
	
   mov	eax,1     ;system call number (sys_exit)
   int	0x80      ;call kernel

section	.data
msg db 'Hello World program in CEdit', 0xa  ;string to be printed
len equ $ - msg     ;length of the string'''
        content_text.delete(1.0,END)
        content_text.insert(END, program)
        
        
    elif var=="Bash":
        program='echo "Hello World program in CEdit";'
        content_text.delete(1.0,END)
        content_text.insert(END, program)
                
    elif var=="C":
        program='''#include <stdio.h>

int main() {
   printf("Hello World program in CEdit");
   return 0;
}'''
        content_text.delete(1.0,END)
        content_text.insert(END, program)
                
    elif var=="C++":
        program='''// Your First C++ Program

#include <iostream>

int main() {
    std::cout << "Hello World program in CEdit";
    return 0;
}
'''
        content_text.delete(1.0,END)
        content_text.insert(END, program)
                
    elif var=="Java":
        program='''
    class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World program in CEdit"); 
    }
}'''
        content_text.delete(1.0,END)
        content_text.insert(END, program)
                
    elif var=="Python3":
        program='print("Hello World program in CEdit")'
        content_text.delete(1.0,END)
        content_text.insert(END, program)
                
    elif var=="Rust":
        program='''fn
main(){
   println!("Hello World program in CEdit");
}'''
        content_text.delete(1.0,END)
        content_text.insert(END, program)
                
    elif var=="Go":
        program='''// First Go program
package main

import "fmt"

// Main function
func main() {

	fmt.Println("Hello World program in CEdit")
}
'''
        content_text.delete(1.0,END)
        content_text.insert(END, program)
                 
    elif var=="Ruby":
        program='puts "Hello World program in CEdit" '
        content_text.delete(1.0,END)
        content_text.insert(END, program)
                 
    elif var=="Text Document":
        program='Hello World program in CEdit'
        content_text.delete(1.0,END)
        content_text.insert(END, program)
                
    else:
        program='Select Appropriate Language'
        content_text.delete(1.0,END)
        content_text.insert(END, program)
                

    
clicked = StringVar()

new_file_icon = PhotoImage(file='icons/new_file.png')
open_file_icon = PhotoImage(file='icons/open_file.png')
save_file_icon = PhotoImage(file='icons/save.png')
saveas_file_icon = PhotoImage(file='icons/saveas.png')
cut_icon = PhotoImage(file='icons/cut.png')
copy_icon = PhotoImage(file='icons/copy.png')
find_icon = PhotoImage(file='icons/find_text.png')
paste_icon = PhotoImage(file='icons/paste.png')
undo_icon = PhotoImage(file='icons/undo.png')
redo_icon = PhotoImage(file='icons/redo.png')
about_icon = PhotoImage(file='icons/about.png')
contactus_icon = PhotoImage(file='icons/contactus.png')
download_icon = PhotoImage(file='icons/downloadicon.png')
contribute_icon = PhotoImage(file='icons/contribute.png')
help_icon = PhotoImage(file='icons/help.png')


menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='New', accelerator='Ctrl+N', compound='left', image=new_file_icon, underline=0, command=new_file)
file_menu.add_command(label='Open', accelerator='Ctrl+O', compound='left', image=open_file_icon, underline=0, command=open_file)
file_menu.add_command(label='Save', accelerator='Ctrl+S', compound='left', image=save_file_icon, underline=0, command=save)
file_menu.add_command(label='Save as', accelerator='Shift+Ctrl+S', compound='left', image=saveas_file_icon, underline=0, command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt+F4', command=exit_editor)
menu_bar.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label='Undo', accelerator='Ctrl+Z', compound='left', image=undo_icon, command=undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', compound='left', image=redo_icon, command=redo)
edit_menu.add_command(label='Terminal', accelerator='Ctrl+T', command=ceterminal)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl+X', compound='left', image=cut_icon, command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl+C', compound='left', image=copy_icon, command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl+V', compound='left', image=paste_icon, command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='Find', underline=0, accelerator='Ctrl+F', compound='left', image=find_icon, command=find_text)
edit_menu.add_separator()
edit_menu.add_command(label='Select All', underline=0, accelerator='Ctrl+A', command=select_all)                      
menu_bar.add_cascade(label='Edit', menu=edit_menu)


view_menu = Menu(menu_bar, tearoff=0)
show_line_number = IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label='Show Line Number', variable=show_line_number,
                          command=update_line_numbers)
show_cursor_info = IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(
    label='Show Cursor Location at Bottom', variable=show_cursor_info, command=show_cursor_info_bar)
to_highlight_line = BooleanVar()
view_menu.add_checkbutton(label='Highlight Current Line', onvalue=1,
                          offvalue=0, variable=to_highlight_line, command=toggle_highlight)
themes_menu = Menu(menu_bar, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu)

color_schemes = {
    'Default': '#09203F.#537895',
    'Greygarious': '#434343.#000000',
    'Aquamarine': '#00B4DB.#0083B0',
    'Blood Red': '#F05F57.#360940',
    'Cobalt Blue': '#97ABFF.#123597',
    'Olive Green': '#FFE000.#799F0C',
    'Night Mode': '#536976.#292E49',
    'Pinkalicious': '#C33764.#1D2671'
}

theme_choice = StringVar()
theme_choice.set('Default')
for k in sorted(color_schemes):
    themes_menu.add_radiobutton(
        label=k, variable=theme_choice, command=change_theme)
menu_bar.add_cascade(label='View', menu=view_menu)

about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(label='About', compound='left', image=about_icon, command=display_about_messagebox)
about_menu.add_command(label='Contact Us', compound='left', image=contactus_icon, command=display_contactus_messagebox)
about_menu.add_command(label='Download', compound='left', image=download_icon, command=display_download_messagebox)
about_menu.add_command(label='Contribute', compound='left', image=contribute_icon, command=display_contribute_messagebox)
about_menu.add_command(label='Help', compound='left', image=help_icon, command=display_help_messagebox)
menu_bar.add_cascade(label='About',  menu=about_menu)
root.config(menu=menu_bar)

shortcut_bar = Frame(root,  height=25, background='#6A11CB')
shortcut_bar.pack(expand='no', fill='x')


#clicked.trace_add('write', lambda *args: print(clicked.get()))

icons = ('new_file', 'open_file', 'save', 'cut', 'copy', 'paste',
         'undo', 'redo', 'find_text')
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.png'.format(icon))
    cmd = eval(icon)
    tool_bar = Button(shortcut_bar, image=tool_bar_icon, command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side='left')
tool_bar= OptionMenu(root, clicked, "Select Language", "Assembly", "Bash", "C", "C++", "Java", "Python3", "Rust", "Go", "Ruby", "Text Document", command=callback)
tool_bar.pack()
clicked.set("Select Language")

line_number_bar = Text(root, width=4, padx=3, takefocus=0,  border=0, background='#6A11CB', state='disabled',  wrap='none')
line_number_bar.pack(side='left',  fill='y')

content_text = Text(root, wrap='word', undo=1)
content_text.pack(expand='yes', fill='both')
scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')
cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1')
cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')


content_text.bind('<KeyPress-F1>', display_help_messagebox)
content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-S>', save)
content_text.bind('<Control-s>', save)
content_text.bind('<Control-f>', find_text)
content_text.bind('<Control-F>', find_text)
content_text.bind('<Control-A>', select_all)
content_text.bind('<Control-a>', select_all)
content_text.bind('<Control-y>', redo)
content_text.bind('<Control-Y>', redo)
content_text.bind('<Control-t>', ceterminal)
content_text.bind('<Control-T>', ceterminal)
content_text.bind('<Any-KeyPress>', on_content_changed)
content_text.tag_configure('active_line', background='#A71D31')


popup_menu = Menu(content_text)
for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
    cmd = eval(i)
    popup_menu.add_command(label=i, compound='left', command=cmd)
popup_menu.add_separator()
popup_menu.add_command(label='Select All', underline=7, command=select_all)
content_text.bind('<Button-3>', show_popup_menu)


content_text.bind('<Button-3>', show_popup_menu)
content_text.focus_set()

root.protocol('WM_DELETE_WINDOW', exit_editor)

icon = PhotoImage(file='icons/CEdit_Icon.png')
root.tk.call('wm', 'iconphoto', root._w, icon)
root.mainloop()
