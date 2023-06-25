import random
from tkinter import *

top = Tk()
top.title("Lotto Numbers Gen")

L0 = Label(top, text="Number of times: ")
L0.place(relx=0.08, rely=0.1)
global E1
E1 = Entry(top, bd=5)
E1.place(relx=0.35, rely=0.1)
num_gen = []

def random_gen():
    n = random.randint(1, 37)
    if n in num_gen:
        while n in num_gen:
            n = random.randint(1, 37)
    return n

def gen_numbers():
    num_gen = []

    L1 = Listbox(top, selectmode=SINGLE, height=8, font=10, width=25)
    L1.place(relx=0.30, rely=0.3)
    # L2 = Listbox(top, selectmode=SINGLE, height=8, font=10, width=2)
    # L2.place(relx=0.78, rely=0.3)
    for x in range(int(E1.get())):
        num_gen.clear()
        for i in range(6):
            to_add = random_gen()
            num_gen.append(to_add)
        num_gen = sorted(num_gen)
        extra_num = random.randint(1, 8)

        L1.insert(x, f"{num_gen}  [{extra_num}]")
        # L2.insert(x, extra_num)

B = Button(top, text="Generate", command=gen_numbers)
B.place(relx=0.75, rely=0.1, height=27, width=70)

top.wm_minsize(width=450, height=250)
top.wm_maxsize(width=450, height=250)

top.mainloop()