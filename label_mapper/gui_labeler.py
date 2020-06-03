from tkinter import *
from tkinter.ttk import Combobox, Separator

main_window = None
comboboxes = {}
mappings = {}


def build_comboboxes(activities, events):
    """
    Builds comboboxes incl. Separators for all activities for one model and one event log
    :param activities: All activities that are passed down by the model importer
    :param events: All events that are passed down by the log importer
    :return: None
    """
    global comboboxes
    # For each activity set up a selector for an event

    for activity in activities:

        # Setup frame for better display in gui
        frame = Frame(main_window)
        frame.configure(background="gray30")
        Scrollbar(frame).grid(column=2)

        # Label the left column as activity in a model + "beautify gui"
        text = "Activity name (model):"
        Label(frame, text=text, bg="gray30", fg="white", padx=5).grid(column=0, row=0)
        Label(frame, text=activity, bg="gray30", fg="white").grid(column=0, row=1)

        # Set up the combobox for an event
        combo = Combobox(frame)
        combo['values'] = events

        # If activity is in events preselect the current one
        if activity in events:
            combo.current(events.index(activity))

        # Label the combobox and place label and box in frame
        Label(frame, text="Event name (log):", bg="gray30", fg="white", padx=5).grid(column=1, row=0)
        combo.grid(column=1, row=1)
        # If the last activity in the graph is handled then do not write a separator
        if activity != activities[-1]:
            Separator(frame, orient="horizontal").grid(row=2, columnspan=2, sticky="ew", pady=10)

        comboboxes[activity] = combo
        # place the frame in the main_window
        frame.grid(column=0)


def set_mapping_cb():
    """
    Function for the button remap which copies a process model and remaps chosen events
    :return: None
    """
    global mappings
    for key, value in comboboxes.items():
        mappings[key] = value.get()
    main_window.destroy()


def build_main_window(activities, events):
    """
    Sets up the main window
    :return: None
    """
    # Import global to write the main_window
    global main_window

    # Set up main window basics
    main_window = Tk()
    scrollbar = Scrollbar(main_window)
    scrollbar.grid(column=4, rowspan=1)
    main_window.configure(background="gray30")
    main_window.title("Label Mapper")

    # Advise user to remap the activities
    Label(main_window, text="Please map the activities of the process model\n to the events in the log",
          bg="gray30", fg="white", font=("Arial Bold", 15)).grid(pady=10, padx=20)

    # Separate heading from the main selection frames
    Separator(main_window, orient="horizontal").grid(sticky="ew", pady=1)
    Separator(main_window, orient="horizontal").grid(sticky="ew", pady=1)

    # build add button
    Label(main_window, bg="gray30", fg="white", text="Add another output model").grid()
    button = Button(main_window, text="+", bg="black", fg="white", command=lambda: build_comboboxes(activities, events))
    button.grid()

    Separator(main_window, orient="horizontal").grid(sticky="ew", pady=1)
    Separator(main_window, orient="horizontal").grid(sticky="ew", pady=1)

    no = 0

    # Build comboboxes from the lists
    build_comboboxes(activities, events)

    # Separate selection frames from the remap button
    Separator(main_window, orient="horizontal").grid(sticky="ew", pady=1)
    Separator(main_window, orient="horizontal").grid(sticky="ew", pady=1)

    # Remaps the dcr graphs labels and quits the gui
    button1 = Button(main_window, text="Remap & Quit", bg="black", fg="white", command=set_mapping_cb)
    button1.grid(sticky="ew")

    # Start GUI
    main_window.mainloop()

    # Return the mappings that were created during gui action
    return mappings


if __name__ == '__main__':
    """
    Only for test purposes should be called from outer space
    """
    activities = ['a', 'b', 'd']
    events = ['a', 'b', 'c']
    build_main_window(activities, events)