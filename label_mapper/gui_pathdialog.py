# encoding=utf-8
from tkinter import *
from tkinter.ttk import Separator
from tkinter.filedialog import askopenfilename, asksaveasfilename

model_path = None
log_path = None
out_path = None

model_checked = False
log_checked = False
out_checked = False

root = None


def open_dialog_model():
    """
    Opens a file chooser dialog for a process model
    :return: None
    """
    global model_checked, model_path
    name = askopenfilename(initialdir=".",
                           filetypes=(("XML File", "*.xml"), ("All Files", "*.*")),
                           title="Choose the process model.")
    try:
        with open(name, 'r'):
            model_checked = True
            model_path.set(name)
    except:
        print("No file exists")


def open_dialog_log():
    """
    Opens a file chooser dialog for an event log
    :return: None
    """
    global log_checked, log_path
    name = askopenfilename(initialdir=".",
                           filetypes=(("XES File", "*.xes"), ("All Files", "*.*")),
                           title="Choose the event log."
                           )
    try:
        with open(name, 'r'):
            log_checked = True
            log_path.set(name)
    except:
        print("No file exists")


def open_dialog_out():
    """
    User can define a path where the tool should write the remapped process model
    :return: None
    """
    global out_checked, out_path
    name = asksaveasfilename(initialdir=".", initialfile="remapped_dcr.xml",
                             filetypes=(("XML File", "*.xml"), ("All Files", "*.*")),
                             title="Choose the output model path.")
    try:
        with open(name, 'w'):
            out_checked = True
            out_path.set(name)
    except:
        print("No permissions")

def save_quit():
    root.destroy()


def get_file_names():
    """
    Opens a window with two file chooser dialogs
    :return: model_path, log_path, out_path
    """
    # import globals
    global model_path, log_path, out_path, root

    # Setup root window
    root = Tk()
    root.title("Choose model and log files")
    root.configure(background='gray30')

    # Setup string variables
    # Process model
    model_path = StringVar()
    model_path.set("Model.xml")

    # Event log
    log_path = StringVar()
    log_path.set("Log.xes")

    # Remapped model
    out_path = StringVar()
    out_path.set("Out.xml")

    # Create file path heading
    Label(root, text="Choose a process model and the event log that\n"
                     " contains the events you want to map to the activities",
          bg="gray30", fg="white", font=("Arial Bold", 20)).grid()

    # Separate header from inputs
    Separator(root, orient="horizontal").grid(sticky="ew")
    Separator(root, orient="horizontal").grid(sticky="ew")

    frame = Frame(root)
    frame.configure(background="gray30")
    Label(frame, bg="gray30", fg="white", text="Inputs", font=("Arial Bold", 17)).grid(sticky="ew")

    # Build input_frame to contain all the input paths
    input_frame = Frame(frame)
    input_frame.configure(background='gray30')

    lbl_model = Label(input_frame, bg="gray30", fg="white", textvar=model_path,
                      font=("Arial Bold", 15))
    lbl_model.grid(column=0, row=0)

    btn_model = Button(input_frame, bg="black", fg="white", text="Choose", command=open_dialog_model)
    btn_model.grid(column=1, row=0)
    Separator(input_frame, orient="horizontal").grid(row=1, columnspan=2, pady=10, sticky="ew")

    lbl_log = Label(input_frame, bg="gray30", fg="white", textvar=log_path,
                    font=("Arial Bold", 15))
    lbl_log.grid(column=0, row=2)
    btn_log = Button(input_frame, bg="black", fg="white", text="Choose", command=open_dialog_log)
    btn_log.grid(column=1, row=2)
    input_frame.grid(pady=15)

    Separator(frame, orient="horizontal").grid(sticky="ew")
    Separator(frame, orient="horizontal").grid(sticky="ew")

    output_frame = Frame(frame)
    output_frame.configure(background="gray30")

    Label(frame, text="Output", fg="white", bg="gray30", font=("Arial Bold", 17)).grid(pady=5)
    Label(output_frame, textvar=out_path, bg="gray30", fg="white", font=("Arial Bold", 15)).grid(column=0, row=0)
    Button(output_frame, bg="black", fg='white', text='Choose', command=open_dialog_out).grid(column=1, row=0)
    output_frame.grid()
    frame.grid()

    Separator(root, orient="horizontal").grid(sticky="ew")
    Separator(root, orient="horizontal").grid(sticky="ew")
    
    Button(text="Save & Quit", bg="black", fg="white", command=save_quit).grid(sticky="ew", pady=15)

    root.mainloop()

    if log_checked and model_checked and out_checked:
        return model_path.get(), log_path.get(), out_path.get()
    else:
        raise TypeError()


if __name__ == '__main__':
    """
    Only for test purposes
    """
    log_path, model_path, out_path = get_file_names()
    print("log_path: {}\nmodel_path: {}\nout_path: {}".format(log_path, model_path, out_path))
