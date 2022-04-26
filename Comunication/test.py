from cgitb import text
import Serial_Comunication_ISUS
import tkinter as tk
ISUS_UART = Serial_Comunication_ISUS.Uart_ISUS()
ISUS_UART.setupUart()
window = tk.Tk()
window.rowconfigure(0, minsize=50, weight=1) 
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

window.title("ISUS CHESS ROBOT")

window.geometry('500x700')


name = ["Joint 1","Joint 2","Joint 3","Joint 4", "Gripper"]
var_unit = ["[0.00-360.00] Degree","[0.00-360.00] Degree","[0.00-250.00] mm","[0.00-360.00] Degree"]
name_xyz = ["x", "y", "z", "roll"]
var_unit_xyz = ["[0.00-660.00] mm","[0.00-660.00] mm","[0.00-250.00] mm","[0.00-360.00] Degree"]
var_x = tk.DoubleVar()
var_y = tk.DoubleVar()
var_z = tk.DoubleVar()
var_roll = tk.DoubleVar()
var_xyz = [var_x,var_y,var_z,var_roll]
var_joint1 = tk.DoubleVar()
var_joint2 = tk.DoubleVar()
var_joint3 = tk.DoubleVar()
var_joint4 = tk.DoubleVar()
var_Joint = [var_joint1,var_joint2,var_joint3,var_joint4]
var_startstop1 = tk.DoubleVar()
var_startstop2 = tk.DoubleVar()
var_startstop3 = tk.DoubleVar()
var_startstop4 = tk.DoubleVar()
var_startstop5 = tk.DoubleVar()
var_StartStop = [var_startstop1,var_startstop2,var_startstop3,var_startstop4, var_startstop5]

var_filed1 = tk.StringVar()
var_filed2 = tk.IntVar()

def send_command_startstop():
    ISUS_UART.StartStop_Move(var_startstop1.get(),var_startstop2.get(),var_startstop3.get(),var_startstop4.get(), var_startstop5.get())

def send_command_joint():
    ISUS_UART.Joint_Move(var_joint1.get(),var_joint2.get(),var_joint3.get(),var_joint4.get())

def send_command_grip_open():
    ISUS_UART.Grip_Chess(0)

def send_command_grip_close():
    ISUS_UART.Grip_Chess(55)

def send_command_home():
    ISUS_UART.Home_Configulation(1,1,1,1)

def send_command_XYZ():
    ISUS_UART.XYZ_Move(var_x.get(),var_y.get(),var_z.get(),var_roll.get())

def send_command_field_pick():
    ISUS_UART.Chess_Pick(var_filed1.get(), var_filed2.get())

def send_command_field_place():
    ISUS_UART.Chess_Place(var_filed1.get(), var_filed2.get())

if __name__ == '__main__':

    txt_startstop = tk.Label(master=window, text="Start/Stop")
    txt_startstop.place(relx=0.13, rely=0.04)
    txt_value = tk.Label(master=window, text="Unit")
    txt_value.place(relx=0.3, rely=0.04)
    for i in range(5):
        txt = tk.Label(master=window, text=name[i])
        txt.place(relx=0.05, rely=0.1+0.05*i)
        st = tk.Checkbutton(window,variable=var_StartStop[i])
        st.place(relx=0.17, rely=0.1+0.05*i)
        if i != 4:
            jv = tk.Entry(window, width=10,textvariable = var_Joint[i])
            jv.place(relx=0.27, rely=0.1+0.05*i)
            txt_unit = tk.Label(master=window, text=var_unit[i])
            txt_unit.place(relx=0.4, rely=0.1+0.05*i)

    for i in range(4):
        txt = tk.Label(master=window, text=name_xyz[i])
        txt.place(relx=0.05, rely=0.4+0.05*i)
        jv = tk.Entry(window, width=10,textvariable = var_xyz[i])
        jv.place(relx=0.27, rely=0.4+0.05*i)
        txt_unit = tk.Label(master=window, text=var_unit_xyz[i])
        txt_unit.place(relx=0.4, rely=0.4+0.05*i)
    
    send_command2 = tk.Button(master=window, text="send_startstop", command=send_command_startstop)
    send_command2.place(relx=0.05, rely=0.85)

    send_command5 = tk.Button(master=window, text="send_home", command=send_command_home)
    send_command5.place(relx=0.05, rely=0.92)

    send_command1 = tk.Button(master=window, text="send_joint", command=send_command_joint)
    send_command1.place(relx=0.255, rely=0.85)

    send_command1 = tk.Button(master=window, text="send_xyz", command=send_command_XYZ)
    send_command1.place(relx=0.43, rely=0.85)

    send_command3 = tk.Button(master=window, text="send_grip_open", command=send_command_grip_open)
    send_command3.place(relx=0.6, rely=0.85)

    send_command4 = tk.Button(master=window, text="send_grip_close", command=send_command_grip_close)
    send_command4.place(relx=0.8, rely=0.85)

    send_command5 = tk.Button(master=window, text="Chess_Pick", command=send_command_field_pick)
    send_command5.place(relx=0.4, rely=0.92)

    send_command5 = tk.Button(master=window, text="Chess_Place", command=send_command_field_place)
    send_command5.place(relx=0.6, rely=0.92)

    # row = ["A", "B", "C", "D", "E", "F", "G", "H"]
    # for i, key in enumerate(row):
    #     for j in range(8, 0, -1):
    #         tt = "send_command"+key+str(j)
    #         tt = tk.Button(master=window, text=key+str(j), textvariable=var_field[i][j], command=send_command_field)
    #         tt.place(relx=0.6 + 0.04 * i, rely=0.6 - 0.05 * j)

    txt = tk.Label(master=window, text="row")
    txt.place(relx=0.05, rely=0.7)
    jv = tk.Entry(window, width=10,textvariable = var_filed1)
    jv.place(relx=0.27, rely=0.7)

    txt = tk.Label(master=window, text="column")
    txt.place(relx=0.05, rely=0.75)
    jv = tk.Entry(window, width=10,textvariable = var_filed2)
    jv.place(relx=0.27, rely=0.75)
    
    window.mainloop()

# print(ISUS_UART.Field_Move("h", 8, 1)) #[x, y, r]
    

# while(True):
#     ISUS_UART.Uart_Read()