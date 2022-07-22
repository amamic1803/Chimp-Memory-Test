from tkinter import *
from random import randint

vrijeme_secs = 5

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

def klik(tipka):
	global run_num, curr_num, kocke
	run_num += 1
	if curr_num == 1:
		brisi(run_num)
	if curr_num == tipka:
		kocke[tipka - 1].config(text=f"{tipka}", background="#00c90d", activebackground="#00c90d")
		curr_num += 1
	elif curr_num < tipka < 11:
		for broj in range(curr_num - 1, 10):
			kocke[broj].config(text=f"{broj + 1}", background="#f0000c", activebackground="#f0000c")
		curr_num = 11

def start_clk(vrijeme):
	global kocke, run_num, curr_num
	run_num += 1
	curr_num = 1
	while len(kocke) != 0:
		kocke[0].place_forget()
		kocke[0].destroy()
		kocke.pop(0)
	koord_kocke = []
	i = 1
	while i <= 10:
		x_koord = randint(0, 455)
		y_koord = randint(100, 555)
		if not preklop(x_koord, y_koord, koord_kocke):
			koord_kocke.append([x_koord, y_koord])
			kocke.append(Button(root, text=str(i), font=("Helvetica", 25, "bold"), borderwidth=0, command=lambda vrsta=i: klik(vrsta)))
			kocke[-1].place(x=x_koord, y=y_koord, height=45, width=45)
			i += 1
	root.after(int(vrijeme * 1000), brisi, run_num)


if __name__ == '__main__':
	root = Tk()
	root.title("Chimp Memory Test")
	root.geometry(f"500x600+{root.winfo_screenwidth() // 2 - 250}+{root.winfo_screenheight() // 2 - 300}")
	root.resizable(False, False)
	root.config(background="#000000")

	start_btn = Button(root, text="START", font=("Helvetica", 20, "bold"), borderwidth=0, relief="flat", background="#03fce3", activebackground="#03fce3", command=lambda: start_clk(vrijeme_secs))
	start_btn.place(x=0, y=0, height=80, width=100)
	run_num = 0
	kocke = []
	root.mainloop()
