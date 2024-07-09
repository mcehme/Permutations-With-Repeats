import tkinter as tk
from tkinter import messagebox
import csv
import permute
from concurrent.futures import ThreadPoolExecutor

def command():
    def threaded():
        root.unbind("<Return>")
        btn["state"] = "disabled"
        input = []
        try:
            for row in csv.reader([list_var.get()]):
                input.extend(row)
            input = (x.strip() for x in input)
            input = (x for x in input if x != "")
            results = permute.permute_with_repeats(*input)
            result = '\n'.join(results[:4_000_000])
        except Exception as e:
            messagebox.showerror("Error", e)
        output_text['state'] = 'normal'
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", result)
        output_text['state'] = 'disabled'
        btn["state"] = "normal"
        root.bind('<Return>', bound_command)
    executor.submit(threaded)
def bound_command(event):
    command()

executor = ThreadPoolExecutor()

    

root = tk.Tk()
root.title("Permutation calculator")
root.bind('<Return>', bound_command)
list_var = tk.StringVar(root)

list_frame = tk.Frame(root)
list_entry = tk.Entry(list_frame, textvariable=list_var, width=30)
scrollbar_x = tk.Scrollbar(list_frame, command=list_entry.xview, orient='horizontal')
list_entry.config(xscrollcommand=scrollbar_x.set)
list_label = tk.Label(list_frame, text="Please enter the values to permute in CSV form:")
note_label = tk.Label(list_frame, text="Note: output is capped at 4,000,000 rows")
btn = tk.Button(list_frame, text="generate", command=command)
list_label.grid(row=0, column=1)
list_entry.grid(row=0, column=2, padx=5)
btn.grid(row=0, column=3)
note_label.grid(row=1, column=1)
scrollbar_x.grid(row=1, column=2)


output_frame = tk.Frame(root)
scroll_frame = tk.Frame(output_frame)
output_text = tk.Text(scroll_frame, height=30, width=70, state="disabled")
scrollbar_y = tk.Scrollbar(scroll_frame, command=output_text.yview)
output_text.config(yscrollcommand=scrollbar_y.set)
output_text.pack(side="left")
scrollbar_y.pack(side="right", fill="y")
scroll_frame.pack(side="top")



list_frame.pack(side="top",pady=5)
output_frame.pack(side="top")
root.mainloop()