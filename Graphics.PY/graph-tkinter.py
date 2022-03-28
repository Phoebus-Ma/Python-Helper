###
# Python tkinter test example.
# 
# License - MIT.
###

import os
import tkinter


# tk_calcnum - digital computation.
def tk_calcnum(str_v1, str_v2, str_v3):
# {
    ret = int(str_v1.get()) + int(str_v2.get())

    str_v3.set(str(ret))
# }


# tk_isdigital - Verify the digital.
def tk_isdigital(content):
# {
    return content.isdigit()
# }


# tk_calculator - Create UI.
def tk_calculator(frame, verify_digital):
# {
    str_v1 = tkinter.StringVar()
    str_v2 = tkinter.StringVar()
    str_v3 = tkinter.StringVar()

    # Create textbox.
    tbox_num1 = tkinter.Entry(
        frame,
        width = 10,
        textvariable = str_v1,
        validate = 'key',
        validatecommand = (verify_digital, '%P')
    )

    tbox_num2 = tkinter.Entry(
        frame,
        width = 10,
        textvariable = str_v2,
        validate = 'key',
        validatecommand = (verify_digital, '%P')
    )

    tbox_result = tkinter.Entry(
        frame,
        width = 10,
        textvariable = str_v3,
        state = 'readonly'
    )

    # Create label.
    lbl_operator    = tkinter.Label(frame, text = '+')
    lbl_result      = tkinter.Label(frame, text = '=')

    # Create button.
    btn_result = tkinter.Button(
        frame,
        text = 'Run',
        command = lambda: tk_calcnum(str_v1, str_v2, str_v3)
    )

    ### ----------------------Layout---------------------- ###

    tbox_num1.grid(row = 0, column = 0)

    lbl_operator.grid(row = 0, column = 1)

    tbox_num2.grid(row = 0, column = 2)

    lbl_result.grid(row = 0, column = 3)

    tbox_result.grid(row = 0, column = 4)

    btn_result.grid(row = 1, column = 2, pady = 5)
# }


# Main function.
def main():
# {
    # Create MainWindow.
    MainWindow = tkinter.Tk()

    # Set Title.
    MainWindow.title('Calculator')

    # Create Frame.
    frame = tkinter.Frame(MainWindow)

    # Set frame size.
    frame.pack(padx = 100, pady = 50)

    # Register a method.
    verify_digital = frame.register(tk_isdigital)

    tk_calculator(frame, verify_digital)

    tkinter.mainloop()
# }


# Program entry.
if '__main__' == __name__:
    main()
