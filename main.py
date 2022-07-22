import time
from tkinter import *
from random import randint


def preklop(x, y, koordinate):
	for i in koordinate:
		if ((i[0] - 45) <= x <= (i[0] + 45)) and ((i[1] - 45) <= y <= (i[1] + 45)):
			return True
	return False

def brisi(x):
	global run_num
	if run_num == x:
		for kocka in kocke:
			kocka.config(text="")

def klik(event, tipka):
	global run_num, curr_num, kocke, start_time
	run_num += 1
	if curr_num == 1:
		brisi(run_num)
		start_time = time.time()
	if curr_num == tipka:
		kocke[tipka - 1].config(text=f"{tipka}", background="#00c90d", activebackground="#00c90d")
		curr_num += 1
	elif curr_num < tipka < 11:
		for broj in range(curr_num - 1, 10):
			kocke[broj].config(text=f"{broj + 1}", background="#f0000c", activebackground="#f0000c")
		curr_num = 11

def start_clk(event):
	global kocke, run_num, curr_num
	try:
		vrijeme = float(ent.get())
	except ValueError:
		vrijeme = 5

	run_num += 1
	curr_num = 1
	while len(kocke) != 0:
		kocke[0].destroy()
		kocke.pop(0)
	koord_kocke = []
	i = 1
	while i <= 10:
		x_koord = randint(0, 455)
		y_koord = randint(100, 555)
		if not preklop(x_koord, y_koord, koord_kocke):
			koord_kocke.append([x_koord, y_koord])
			kocke.append(Label(root, text=str(i), font=("Helvetica", 25, "bold"), justify=CENTER, borderwidth=0, highlightthickness=0, background="#ffffff", activebackground="#ffffff", foreground="#000000", activeforeground="#000000"))
			kocke[-1].bind("<ButtonRelease-1>", lambda event=event, vrsta=i: klik(event, vrsta))
			kocke[-1].place(x=x_koord, y=y_koord, height=45, width=45)
			i += 1
	root.after(int(vrijeme * 1000), brisi, run_num)

def change_thickness(event, widget, typ, thickness_l, thickness_h):
	if typ:
		widget.config(highlightthickness=thickness_l)
	else:
		widget.config(highlightthickness=thickness_h)

def validate_input(full_text):
	if " " in full_text or "-" in full_text or full_text.count(".") > 1 or len(full_text) > 5:
		return False
	elif full_text == "" or full_text == ".":
		return True
	else:
		try:
			float(full_text)
			return True
		except ValueError:
			return False


if __name__ == '__main__':
	root = Tk()
	root.title("Chimp Memory Test")
	root.geometry(f"500x600+{root.winfo_screenwidth() // 2 - 250}+{root.winfo_screenheight() // 2 - 300}")
	root.resizable(False, False)
	root.config(background="#000000")

	start_btn = Label(root, text="START", font=("Helvetica", 20, "bold"), borderwidth=0, highlightthickness=0, highlightcolor="red", highlightbackground="red", background="#03fce3", activebackground="#03fce3")
	start_btn.place(x=0, y=0, height=80, width=120)
	start_btn.bind("<Enter>", lambda event: change_thickness(event, start_btn, False, 0, 5))
	start_btn.bind("<Leave>", lambda event: change_thickness(event, start_btn, True, 0, 5))
	start_btn.bind("<ButtonRelease-1>", start_clk)

	reg = root.register(validate_input)
	ent = Entry(root, justify=CENTER, validate="key", validatecommand=(reg, "%P"), background="white", foreground="#000000", highlightthickness=3, highlightcolor="blue", highlightbackground="blue", borderwidth=0, font=("Helvetica", 11))
	ent.insert(0, "5")
	ent.place(x=270, y=20, width=55, height=25)
	ent_lbl = Label(root, text="Time visible (s):", font=("Helvetica", 12, "bold"), borderwidth=0, highlightthickness=0, background="#000000", activebackground="#000000", foreground="#ffffff", activeforeground="#ffffff")
	ent_lbl.place(x=150, y=20, width=120, height=25)

	run_num = 0
	kocke = []
	start_time = 0
	root.mainloop()
