import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    PAD = 10
    MAX_BUTTONS_PER_ROW = 4
    button_captions = ['C','+/-','%','/',
                       7,8,9,'*',
                       4,5,6,'-',
                       1,2,3,'+',
                       0,'.','='
                       ]
    
    def __init__(self, controller):
        super().__init__()
        self.title('PyCalc1.0')
        self.controller = controller
        
        self.value_var = tk.StringVar()
        self.config(bg='black')
        self.configure_button_styles()
        
        self._make_main_frame()
        self._make_label()
        self._make_buttons()
        self._center_window()
    
    def configure_button_styles(self):
        style = ttk.Style()
        style.theme_use('alt')
        # Style for number buttons
        style.configure('N.Tbutton',foreground='white', background='gray')

        # Style for operator buttons
        style.configure('O.TButton', foreground='white', background='orange')
    
        # Style for miscellaneous button
        style.configure('M.TButton', background='white')
    
    def main(self):
        self.mainloop()
        
    def _make_main_frame(self):
        self.main_frm = tk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
    
    def _make_label(self):
        lbl = tk.Label(self.main_frm, anchor='e', textvariable = self.value_var, bg='black', fg='white', font=('Arial',30))
        lbl.pack(fill='x')
        
    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()
        
        is_first_row = True
        BUTTONS_IN_ROW = 0
        
        for caption in self.button_captions:
            if (is_first_row or BUTTONS_IN_ROW == self.MAX_BUTTONS_PER_ROW):
                is_first_row = False
                
                frm = ttk.Frame(outer_frm)
                frm.pack(fill='x')
                BUTTONS_IN_ROW = 0
            
            if (isinstance(caption, int)):
                style_prefix = 'N'
            elif (self._is_operator(caption)):
                style_prefix = 'O'
            else:
                style_prefix = 'M'
            
            style_name = f'{style_prefix}.TButton'
            btn= ttk.Button(frm, text=caption, style=style_name, command= (lambda button = caption: self.controller.on_button_click(button)), width=10)
            if caption == 0:
                fill = 'x'
                expand = 1
            else:
                fill = 'x'
                expand = 0
                
            btn.pack(side='left', expand= expand, fill=fill)
            BUTTONS_IN_ROW += 1
    
    def _is_operator(self, button_caption):
        return button_caption in ['/','*','-', '+', '=']
    
    def _center_window(self):
        self.update()
        
        width = self.winfo_width()
        height = self.winfo_height()
        
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        
        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
    