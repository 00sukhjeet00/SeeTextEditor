#!/usr/bin/env python3
import sys,os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
filename=''
def open_file(event):
    filepath = askopenfilename(
        filetypes=[("All Files", "*.*")]
    )
    if not filepath:
        return
    textArea.delete(1.0,END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        textArea.insert(END,text)
    root.title(f"See Text Editor - {filepath}")
    global filename
    filename=filepath
def save_file(event):
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("All Files", "*.*")],
    )
    if not filepath:
        return
    else:
    	File=open(filepath,'w')
    	File.write(textArea.get(1.0,END))
    	File.close()
    root.title(f"See Text Editor - {filepath}")
def extensionFileComplier(event):
	global filename
	file_name,file_extension=os.path.splitext(filename)
	if file_extension=='.py':
		os.system('chmod +x '+filename)
		os.system('python3 '+filename)
	if file_extension=='.cpp':
		os.system('g++ '+filename+' -o '+file_name)
		os.system('.'+filename[:5])
	if file_extension=='.html':
		os.system('firefox '+filename)
def select_all(event):
    textArea.tag_add(SEL, "1.0", END)
    textArea.mark_set(INSERT, "1.0")
    textArea.see(INSERT)
    return 'break'
root=Tk()
root.title('See Text Editor')
textArea=Text(root,background='gray80')
textArea.pack(side=LEFT,fill=Y)
textArea.bind('<Control-Key-a>',select_all)
root.bind('<Control-o>',open_file)
root.bind('<Control-s>',save_file)
root.bind('<Control-b>',extensionFileComplier)
root.bind('<Alt_L><f>',sys.exit)
root.mainloop()