import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import json

from src.gui.stylesheet import BODY

class BodyFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.config(BODY)

class HomeFrame(BodyFrame):
    def __init__(self, root):
        super().__init__(root)

class NotesFrame(BodyFrame):
    def __init__(self, root):
        super().__init__(root)

        note = tk.Text(
            self,
            bg=BODY["bg"],
            highlightthickness=BODY["highlightthickness"],
            relief=BODY["relief"]
        )
        note_scoller = tk.Scrollbar(
            self,
            bg=BODY["bg"],
            highlightthickness=BODY["highlightthickness"],
            relief=BODY["relief"]
        )
        note_selection = tk.Listbox(
            self,
            bg=BODY["bg"],
            highlightthickness=BODY["highlightthickness"],
            relief=BODY["relief"]
        )
        note_selection_scoller = tk.Scrollbar(
            self,
            bg=BODY["bg"],
            highlightthickness=BODY["highlightthickness"],
            relief=BODY["relief"]
        )
        button_frame = tk.Frame(
            self,
            bg=BODY["bg"],
            highlightthickness=BODY["highlightthickness"],
            relief=BODY["relief"]
        )
        save = tk.Button(button_frame, text="Save",)
        edit = tk.Button(button_frame, text="Edit")
        delete = tk.Button(button_frame, text="Delete")


        note_selection.config(yscrollcommand=note_selection_scoller.set)
        note_selection_scoller.config(command=note_selection.yview)

        note.config(yscrollcommand=note_scoller.set)
        note_scoller.config(command=note.yview)

        note_selection.grid(row=1, column=1, rowspan=2, sticky="nsew", padx=4, pady=2)
        note_selection_scoller.grid(row=1, column=2, rowspan=2, sticky="ns", padx=4, pady=2)
        note.grid(row=1, column=4, sticky="nsew", padx=4, pady=2)
        note_scoller.grid(row=1, column=5, sticky="ns", padx=4, pady=2)
        button_frame.grid(row=2, column=4, columnspan=2, sticky="nsew", padx=4, pady=2)
        save.grid(row=0, column=0, sticky="nsew", padx=4, pady=2)
        edit.grid(row=0, column=1, sticky="nsew", padx=4, pady=2)
        delete.grid(row=0, column=2, sticky="nsew", padx=4, pady=2)

        self.grid_rowconfigure(0, weight=10) # top padding
        self.grid_rowconfigure(1, weight=65)
        self.grid_rowconfigure(2, weight=15) # buttons
        self.grid_rowconfigure(3, weight=10) # bottom padding

        self.grid_columnconfigure(0, weight=10) # left padding
        self.grid_columnconfigure(1, weight=30) # note selection
        self.grid_columnconfigure(2, weight=5) # note selection scoller
        self.grid_columnconfigure(3, weight=5) # mid padding
        self.grid_columnconfigure(4, weight=35) # note, buttons
        self.grid_columnconfigure(5, weight=5) # note scoller, buttons (cont)
        self.grid_columnconfigure(6, weight=10) # right padding

        button_frame.grid_rowconfigure(0, weight=100)
        
        button_frame.grid_columnconfigure(0, weight=33)
        button_frame.grid_columnconfigure(1, weight=33)
        button_frame.grid_columnconfigure(2, weight=33)

class SettingsFrame(BodyFrame):
    def __init__(self, root):
        super().__init__(root)

        self.settings = self.get_settings()

        # input device
        self.input_device_label = tk.Label(
                self, 
                text="Input Device",
                bg=BODY["bg"],
                highlightthickness=BODY["highlightthickness"],
                relief=BODY["relief"]
            )
        self.input_device_combobox = ttk.Combobox(
                self, 
                values = sr.Microphone.list_microphone_names(), 
                state="readonly",
                background=BODY["bg"]
            )
        self.input_device_combobox.set(self.set_input_device())
        self.input_device_combobox.bind("<<ComboboxSelected>>", self.update_input_device)
        
        # sensitivity
        self.sensitivity_label = tk.Label(
                self, 
                text="Sensitivity",
                bg=BODY["bg"],
                highlightthickness=BODY["highlightthickness"],
                relief=BODY["relief"]
            )
        self.sensitivity_scale = tk.Scale(
                self, 
                from_=0, 
                to=100, 
                orient="horizontal",
                bg=BODY["bg"],
                highlightthickness=BODY["highlightthickness"],
                relief=BODY["relief"]
            )
        self.sensitivity_scale.set(self.settings["sensitivity"])
        self.sensitivity_scale.bind("<ButtonRelease>", self.update_sensitivity)

        # wake phrase
        self.wake_phrase_label = tk.Label(
                self, 
                text="Wake Phrase",
                bg=BODY["bg"],
                highlightthickness=BODY["highlightthickness"],
                relief=BODY["relief"]
            )
        self.wake_phrase = tk.StringVar()
        self.wake_phrase.set(self.settings["wake_phrase"])
        self.wake_phrase_entry = tk.Entry(
                self, 
                textvariable=self.wake_phrase,
                bg=BODY["bg"],
                highlightthickness=BODY["highlightthickness"],
                relief=BODY["relief"]
            )

        # sleep phrase
        self.sleep_phrase_label = tk.Label(
                self, 
                text="Sleep Phrase",
                bg=BODY["bg"],
                highlightthickness=BODY["highlightthickness"],
                relief=BODY["relief"]
            )
        self.sleep_phrase = tk.StringVar()
        self.sleep_phrase.set(self.settings["sleep_phrase"])
        self.sleep_phrase_entry = tk.Entry(
                self, 
                textvariable=self.sleep_phrase,
                bg=BODY["bg"],
                highlightthickness=BODY["highlightthickness"],
                relief=BODY["relief"]
            )

        self.save_button = tk.Button(self, text="Save", state="disabled")
        self.save_button.bind("<Button>", self.save_settings)

        self.input_device_label.grid(row=1, column=1, sticky="ew", padx=4, pady=2)
        self.input_device_combobox.grid(row=1, column=2, sticky="ew", padx=4, pady=2)
        self.sensitivity_label.grid(row=2, column=1, sticky="ew", padx=4, pady=2)
        self.sensitivity_scale.grid(row=2, column=2, sticky="ew", padx=4, pady=2)
        self.wake_phrase_label.grid(row=3, column=1, sticky="ew", padx=4, pady=2)
        self.wake_phrase_entry.grid(row=3, column=2, sticky="ew", padx=4, pady=2)
        self.sleep_phrase_label.grid(row=4, column=1, sticky="ew", padx=4, pady=2)
        self.sleep_phrase_entry.grid(row=4, column=2, sticky="ew", padx=4, pady=2)
        self.save_button.grid(row=5, column=1, columnspan=2, sticky="ew", padx=4, pady=2)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
    
    def set_input_device(self):
        if self.settings["microphone"] in self.input_device_combobox["values"]:
            return self.settings["microphone"]
        return "Select Input Device"
    
    def update_input_device(self, event):
        self.update_settings_value("microphone", self.input_device_combobox.get())
    
    def update_sensitivity(self, event):
        self.update_settings_value("sensitivity", self.sensitivity_scale.get())

    def update_settings_value(self, setting, value):
        self.save_button.config(state="normal")
        if self.settings[setting] != value:
            self.settings[setting] = value
    
    def get_settings(self):
        with open("data/settings.json", "r") as f:
            return json.load(f)
    
    def save_settings(self, event):
        with open("data/settings.json", "w") as f:
            json.dump(self.settings, f)
        self.save_button.config(state="disabled")
        