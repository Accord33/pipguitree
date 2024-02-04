import tkinter
from tkinter import ttk
import subprocess
import json

class App:
    def __init__(self):
        output = subprocess.run(['pipdeptree','--json'],capture_output=True, text=True).stdout
        datas = json.loads(output)

        self.frm = tkinter.Tk()
        self.frm.geometry('500x400')
        tree = ttk.Treeview(self.frm, columns=['installed_version','required_version'], height=400)
        tree.column('#0', width=166)
        tree.column('installed_version', width=166)
        tree.column('required_version', width=167)
        tree.heading('#0', text='Name')
        tree.heading('installed_version', text='installed version')
        tree.heading('required_version', text='required version')
        for n, i in enumerate(datas):
            parent = tree.insert(
                '',
                'end',
                tags=str(n),
                text=i['package']['package_name'],
                values=[i['package']['installed_version'], '']
            )
            if n % 2 == 0:
                tree.tag_configure(n, background='gray90')
            for j in i['dependencies']:
                child = tree.insert(
                    parent,
                    'end',
                    text=j['package_name'],
                    values=[j['installed_version'], j['required_version']]
                )
        tree.pack(fill='both')
    def main(self):
        self.frm.mainloop()
        
def main():
    app = App()
    app.main()
        
if __name__ == "__main__":
    main()
