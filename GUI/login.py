from tkinter import *
from tkinter import messagebox
import ast
import os
import json

main = Tk()
main.title("Login")
main.geometry('950x500+300+150')
main.configure(bg='#737CA1')
main.resizable(False, False)

img = PhotoImage(file='health.png')
Label(main, image=img, bg='#737CA1').place(x=50, y=50)

frame1 = Frame(main, width=500, height=950, bg='white')
frame1.place(x=480, y=0)
frame = Frame(main, width=500, height=950, bg='white')
frame.place(x=480, y=70)

heading1 = Label(text='Welcome to the Pacemaker Controller', fg='white', bg='#737CA1',
                 font=('Microsoft YaHei UI Light', 16, 'bold'))
heading1.place(x=35, y=10)

heading = Label(frame, text='Login', fg='#737CA1', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=175, y=5)


## LOGIN
def signin():
    global username
    username = user.get()
    password = pw.get()
    try:
        file = open('database.txt', 'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()
        # print(r.keys())
        # print(r.values())
        if username in r.keys() and password == r[username]:
            main.destroy()
            app = Tk()
            app.title("App")
            app.geometry('950x500+300+150')
            app.configure(bg='white')
            app.resizable(False, False)

            heading1 = Label(app, text='Choose Pacemaker Mode', fg='#737CA1', bg='white',
                             font=('Microsoft YaHei UI Light', 16, 'bold'))
            heading1.place(x=35, y=20)
            ## MODE SELECTION
            modes = [
                "AOO",
                "VOO",
                "AAI",
                "VVI",
            ]
            menuFrame = Frame(app, width=150, height=25, bg='white')
            menuFrame.place(x=310, y=0)
            displayFrame = Frame(app, width=900, height=425, bg='white')
            displayFrame.place(x=20, y=50)

            deviceStatus = Label(app, text='Device Status:', fg='black', bg='white',
                                 font=('Microsoft YaHei UI Light', 16, 'bold'))
            deviceStatus.place(x=500, y=20)
            deviceStatus1 = Label(app, text='Disconnected...', fg='black', bg='white',
                                  font=('Microsoft YaHei UI Light', 14))
            deviceStatus1.place(x=650, y=21)
            Label(app, text='User: '+username, fg='#342D7E', bg='white',font=('Microsoft YaHei UI Light', 9)).place(x=1,y=1)

            # def about():
            #     pop = Toplevel(app)
            #     pop.title = ("About DCM")
            #     pop.geometry("170x100+700+300")
            #     pop.config(bg='white')
            #     aboutInfo = Label(pop,
            #                       text='Application model #ABC123\nSoftware Version 1.0\nSerial #100555213\nMcMaster University',
            #                       fg='black', bg='white').place(x=10, y=10)
            #
            # aboutButton = Button(app, text='About', bg='#737CA1', fg='white', width=10, command=about)
            # aboutButton.place(x=850, y=20)

            def clear_frame():
                for widgets in displayFrame.winfo_children():
                    widgets.destroy()

            def selected(x):
                clear_frame()
                setButton()
                loadPrev()
                if x == 'AOO' or x == 'VOO':
                    LRL_slider()
                    URL_slider()
                    AA_slider()
                    APW_slider()
                elif x == 'AAI':
                    LRL_slider()
                    URL_slider()
                    AA_slider()
                    APW_slider()
                    ARP_slider()
                    A_sens()
                    PVARP()
                    hyst()
                    rateSm()
                elif x == 'VVI':
                    LRL_slider()
                    URL_slider()
                    AA_slider()
                    APW_slider()
                    VRP_slider()
                    V_sens()
                    hyst()
                    rateSm()
                global currentMode
                print(x)
                currentMode = x
                return currentMode

            clicked = StringVar()
            clicked.set(modes[0])
            dropdown = OptionMenu(menuFrame, clicked, *modes, command=selected)
            dropdown.config(bg='white', width=10, fg='black', activebackground='white', activeforeground='#737CA1')
            dropdown["menu"].config(bg="white", fg="black", activebackground="white", activeforeground="#737CA1")
            dropdown.pack(side='left')
            dropdown.pack(pady=20)

            ## SLIDER

            # def selectedLRL(x):
            #     global LRL_value
            #     LRL_value=IntVar()
            #     LRL_value=x
            def LRL_slider():
                LRL_modes = [
                    "30", "35", "40", "45", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61",
                    "62", "63", "64", "65", "66", "67", "68", "69", "70",
                    "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85",
                    "86", "87", "88", "89",
                    "90", "95", "105", "110", "115", "120", "125", "130", "135", "140", "145", "150", "155", "160",
                    "165", "170", "175",
                ]
                global clickedLRL
                clickedLRL = StringVar()
                clickedLRL.set(LRL_modes[14])
                dropdownLRL = OptionMenu(displayFrame, clickedLRL, *LRL_modes)
                dropdownLRL.config(bg='white', width=10, fg='black', activebackground='white',
                                   activeforeground='#737CA1')
                dropdownLRL["menu"].config(bg="white", fg="black", activebackground="white", activeforeground="#737CA1")
                dropdownLRL.place(x=200, y=50)

                # s1 = Scale(displayFrame, from_=30, to=175, orient=HORIZONTAL, length=250, resolution=5, background='white',troughcolor='#737CA1',activebackground='white')
                # s1.place(x=200, y=50)
                # s1.set(60)
                Label(displayFrame, text='Lower Rate Limit (ppm):', bg='white', fg='#737CA1',
                      font=('Helvetica bold', 12)).place(x=0, y=50)

            def URL_slider():
                global URL_value
                URL_value = IntVar()
                s2 = Scale(displayFrame, from_=50, to=175, orient=HORIZONTAL, length=250, resolution=5,
                           background='white', troughcolor='#737CA1', activebackground='white', variable=URL_value)
                s2.place(x=200, y=120)
                s2.set(120)
                Label(displayFrame, text='Upper Rate Limit (ppm):', bg='white', fg='#737CA1',
                      font=('Helvetica bold', 12)).place(x=0, y=120)

            def AA_slider():
                # var0=IntVar()
                # c0 = Checkbutton(displayFrame, text="Set Amplitude OFF", bg='white',variable=var0)
                # c0.place(x=465,y=200)
                # s3 = Scale(displayFrame, from_=0.5, to=3.2, orient=HORIZONTAL, length=250, resolution=0.1, background='white',troughcolor='#737CA1',activebackground='white')
                # s3.place(x=200, y=190)
                AA_modes = [
                    "0", "0.5", "0.6", "0.7", "0.8", "0.9", "1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6",
                    "1.7", "1.8", "1.9", "2.0", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8", "2.9",
                    "3.0", "3.1", "3.2", "3.5", "4.0", "4.5", "5.0", "5.5", "6.0", "6.5", "7.0", "7.5",
                ]
                global clickedAA
                clickedAA = StringVar()
                clickedAA.set(AA_modes[-9])
                dropdownAA = OptionMenu(displayFrame, clickedAA, *AA_modes)
                dropdownAA.config(bg='white', width=10, fg='black', activebackground='white',
                                  activeforeground='#737CA1')
                dropdownAA["menu"].config(bg="white", fg="black", activebackground="white", activeforeground="#737CA1")
                dropdownAA.place(x=200, y=190)
                Label(displayFrame, text='Amplitude (Volts):', bg='white', fg='#737CA1',
                      font=('Helvetica bold', 12)).place(x=0, y=190)

            def APW_slider():
                global PW_value
                PW_value = DoubleVar()
                s4 = Scale(displayFrame, from_=0.1, to=1.9, orient=HORIZONTAL, length=250, resolution=0.1,
                           background='white', troughcolor='#737CA1', activebackground='white', variable=PW_value)
                s4.place(x=200, y=260)
                Label(displayFrame, text='Pulse Width (ms):', bg='white', fg='#737CA1',
                      font=('Helvetica bold', 12)).place(x=0, y=260)

            def ARP_slider():
                global ARP_value
                ARP_value = IntVar()
                s5 = Scale(displayFrame, from_=150, to=500, orient=HORIZONTAL, length=250, resolution=10,
                           background='white', troughcolor='#737CA1', activebackground='white', variable=ARP_value)
                s5.place(x=620, y=200)
                s5.set(250)
                Label(displayFrame, text='Atrial Refactory \n Period (ms):', padx=6, bg='white', fg='#737CA1',
                      font=('Helvetica bold', 12)).place(x=460, y=200)

            def VRP_slider():
                global VRP_value
                VRP_value = IntVar()
                s6 = Scale(displayFrame, from_=150, to=500, orient=HORIZONTAL, length=250, resolution=10,
                           background='white', troughcolor='#737CA1', activebackground='white', variable=VRP_value)
                s6.place(x=620, y=200)
                s6.set(320)
                Label(displayFrame, text='Ventricular Refactory \nPeriod (ms):', bg='white', fg='#737CA1',
                      font=('Helvetica bold', 12)).place(x=460, y=200)

            def hyst():
                global hyst_value
                hyst_value = IntVar()
                c1 = Checkbutton(displayFrame, text="Hysteresis Rate Limit (Same as LRL)", bg='white',
                                 variable=hyst_value)
                c1.place(x=0, y=330)

            def rateSm():
                global smoothingRate
                smoothingRate = IntVar()
                s6 = Scale(displayFrame, from_=0, to=25, orient=HORIZONTAL, length=250, resolution=3.07,
                           background='white', troughcolor='#737CA1', activebackground='white', variable=smoothingRate)
                s6.place(x=620, y=260)
                Label(displayFrame, text='Rate Smoothing (%):', bg='white', fg='#737CA1',
                      font=('Helvetica bold', 12)).place(x=460, y=260)

            def V_sens():
                # s7 = Scale(displayFrame, from_=1, to=10, orient=HORIZONTAL, length=250, resolution=0.5, background='white',troughcolor='#737CA1', activebackground='white')
                # s7.place(x=620, y=50)
                # s7.set(2.5)
                V_sens_modes = [
                    "0.25", "0.5", "0.75", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0", "4.5", "5.0", "5.5",
                    "6.0", "6.5", "7.0", "7.5", "8.0", "8.5", "9.0", "9.5", "10.0",
                ]
                global V_clicked_sens
                V_clicked_sens = StringVar()
                V_clicked_sens.set(V_sens_modes[6])
                V_dropdown_sens = OptionMenu(displayFrame, V_clicked_sens, *V_sens_modes)
                V_dropdown_sens.config(bg='white', width=10, fg='black', activebackground='white',
                                       activeforeground='#737CA1')
                V_dropdown_sens["menu"].config(bg="white", fg="black", activebackground="white",
                                               activeforeground="#737CA1")
                V_dropdown_sens.place(x=620, y=50)
                Label(displayFrame, text='Sensitivity (mV):', bg='white', fg='#737CA1',
                      font=('Helvetica bold', 12)).place(x=480, y=50)

            def A_sens():
                # s8 = Scale(displayFrame, from_=0.25, to=0.75,digits=2, orient=HORIZONTAL, length=250, resolution=0.25, background='white',troughcolor='#737CA1', activebackground='white')
                # s8.place(x=620, y=50)
                # s8.set(0.75)
                A_sens_modes = [
                    "0.25", "0.5", "0.75", "1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0", "4.5", "5.0", "5.5",
                    "6.0", "6.5", "7.0", "7.5", "8.0", "8.5", "9.0", "9.5", "10.0",
                ]
                global A_clicked_sens
                A_clicked_sens = StringVar()
                A_clicked_sens.set(A_sens_modes[2])
                A_dropdown_sens = OptionMenu(displayFrame, A_clicked_sens, *A_sens_modes)
                A_dropdown_sens.config(bg='white', width=10, fg='black', activebackground='white',
                                       activeforeground='#737CA1')
                A_dropdown_sens["menu"].config(bg="white", fg="black", activebackground="white",
                                               activeforeground="#737CA1")
                A_dropdown_sens.place(x=620, y=50)
                Label(displayFrame, text='Sensitivity (mV):', bg='white', fg='#737CA1',
                      font=('Helvetica bold', 12)).place(x=480, y=50)

            def PVARP():
                global PVARP1
                PVARP1 = IntVar()
                s9 = Scale(displayFrame, from_=150, to=500, orient=HORIZONTAL, length=250, resolution=10,
                           background='white', troughcolor='#737CA1', activebackground='white', variable=PVARP1)
                s9.place(x=620, y=130)
                s9.set(250)
                Label(displayFrame, text='PVARP (ms):', bg='white', fg='#737CA1', font=('Helvetica bold', 12)).place(
                    x=480, y=130)
                Label(displayFrame, text='(Post Ventricular Atrial Refractory Period)', bg='white', fg='#737CA1',
                      font=('Helvetica bold', 9)).place(x=635, y=175)
            # def setValues():
            #     if currentMode=='AOO':
            #         AOO_LRL=clickedLRL.get()
            #         AOO_URL=str(URL_value.get())
            #         AOO_AA=clickedAA.get()
            #         AOO_APW=PW_value.get()
            #         f = open("data.json", "r+")
            #         data = json.load(f)
            #         for i in data:
            #             if i["username"] == username:
            #                 i["AOO"]["LRL"] = AOO_LRL
            #                 i["AOO"]["URL"] = AOO_URL
            #                 i["AOO"]["AA"] = AOO_AA
            #                 i["AOO"]["APW"] = AOO_APW
            #         open("data.json", "w").write(
            #             json.dumps(data, indent=4, separators=(',', ': '))
            #         )
            #     elif currentMode=='AAI':
            #         AAI_LRL=clickedLRL.get()
            #         AAI_URL=str(URL_value.get())
            #         AAI_AA=clickedAA.get()
            #         AAI_APW=str(PW_value.get())
            #         AAI_ARP=str(ARP_value.get())
            #         AAI_AS=A_clicked_sens.get()
            #         AAI_PVARP=str(PVARP1.get())
            #         if int(hyst_value.get()) == 1:
            #             AAI_H=clickedLRL.get()
            #         else:
            #             AAI_H='0'
            #         AAI_S=str(smoothingRate.get())
            #
            #         f = open("data.json", "r+")
            #         data = json.load(f)
            #         for i in data:
            #             if i["username"] == username:
            #                 i["AAI"]["LRL"] = AAI_LRL
            #                 i["AAI"]["URL"] = AAI_URL
            #                 i["AAI"]["AA"] = AAI_AA
            #                 i["AAI"]["APW"] = AAI_APW
            #                 i["AAI"]["ARP"] = AAI_ARP
            #                 i["AAI"]["AS"] = AAI_AS
            #                 i["AAI"]["PVARP"] = AAI_PVARP
            #                 i["AAI"]["H"] = AAI_H
            #                 i["AAI"]["S"] = AAI_S
            #         open("data.json", "w").write(
            #             json.dumps(data, indent=4, separators=(',', ': '))
            #         )
            #     elif currentMode=='VOO':
            #         VOO_LRL=clickedLRL.get()
            #         VOO_URL=str(URL_value.get())
            #         VOO_VA=clickedAA.get()
            #         VOO_VPW=str(PW_value.get())
            #         f = open("data.json", "r+")
            #         data = json.load(f)
            #         for i in data:
            #             if i["username"] == username:
            #                 i["VOO"]["LRL"] = VOO_LRL
            #                 i["VOO"]["URL"] = VOO_URL
            #                 i["VOO"]["VA"] = VOO_VA
            #                 i["VOO"]["VPW"] = VOO_VPW
            #         open("data.json", "w").write(
            #             json.dumps(data, indent=4, separators=(',', ': '))
            #         )
            #     elif currentMode=='VVI':
            #         VVI_LRL=clickedLRL.get()
            #         VVI_URL=str(URL_value.get())
            #         VVI_VA=clickedAA.get()
            #         VVI_VPW=str(PW_value.get())
            #         VVI_VRP=str(ARP_value.get())
            #         VVI_VS=A_clicked_sens.get()
            #         if int(hyst_value.get()) == 1:
            #             VVI_H=clickedLRL.get()
            #         else:
            #             VVI_H='0'
            #         VVI_S=str(smoothingRate.get())
            #
            #         f = open("data.json", "r+")
            #         data = json.load(f)
            #         for i in data:
            #             if i["username"] == username:
            #                 i["VVI"]["LRL"] = VVI_LRL
            #                 i["VVI"]["URL"] = VVI_URL
            #                 i["VVI"]["VA"] = VVI_VA
            #                 i["VVI"]["VPW"] = VVI_VPW
            #                 i["VVI"]["VRP"] = VVI_VRP
            #                 i["VVI"]["VS"] = VVI_VS
            #                 i["VVI"]["H"] = VVI_H
            #                 i["VVI"]["S"] = VVI_S
            #         open("data.json", "w").write(
            #             json.dumps(data, indent=4, separators=(',', ': '))
            #         )
            def outputVal():
                if currentMode=='AOO':
                    AOO_LRL=clickedLRL.get()
                    AOO_URL=str(URL_value.get())
                    AOO_AA=clickedAA.get()
                    AOO_APW=str(PW_value.get())
                    f = open("data.json", "r+")
                    data = json.load(f)
                    for i in data:
                        if i["username"] == username:
                            i["AOO"]["LRL"] = AOO_LRL
                            i["AOO"]["URL"] = AOO_URL
                            i["AOO"]["AA"] = AOO_AA
                            i["AOO"]["APW"] = AOO_APW
                    open("data.json", "w").write(
                        json.dumps(data, indent=4, separators=(',', ': '))
                    )
                elif currentMode=='AAI':
                    AAI_LRL=clickedLRL.get()
                    AAI_URL=str(URL_value.get())
                    AAI_AA=clickedAA.get()
                    AAI_APW=str(PW_value.get())
                    AAI_ARP=str(ARP_value.get())
                    AAI_AS=A_clicked_sens.get()
                    AAI_PVARP=str(PVARP1.get())
                    if int(hyst_value.get()) == 1:
                        AAI_H=clickedLRL.get()
                    else:
                        AAI_H='0'
                    AAI_S=str(smoothingRate.get())

                    f = open("data.json", "r+")
                    data = json.load(f)
                    for i in data:
                        if i["username"] == username:
                            i["AAI"]["LRL"] = AAI_LRL
                            i["AAI"]["URL"] = AAI_URL
                            i["AAI"]["AA"] = AAI_AA
                            i["AAI"]["APW"] = AAI_APW
                            i["AAI"]["ARP"] = AAI_ARP
                            i["AAI"]["AS"] = AAI_AS
                            i["AAI"]["PVARP"] = AAI_PVARP
                            i["AAI"]["H"] = AAI_H
                            i["AAI"]["S"] = AAI_S
                    open("data.json", "w").write(
                        json.dumps(data, indent=4, separators=(',', ': '))
                    )
                elif currentMode=='VOO':
                    VOO_LRL=clickedLRL.get()
                    VOO_URL=str(URL_value.get())
                    VOO_VA=clickedAA.get()
                    VOO_VPW=str(PW_value.get())
                    f = open("data.json", "r+")
                    data = json.load(f)
                    for i in data:
                        if i["username"] == username:
                            i["VOO"]["LRL"] = VOO_LRL
                            i["VOO"]["URL"] = VOO_URL
                            i["VOO"]["VA"] = VOO_VA
                            i["VOO"]["VPW"] = VOO_VPW
                    open("data.json", "w").write(
                        json.dumps(data, indent=4, separators=(',', ': '))
                    )
                elif currentMode=='VVI':
                    VVI_LRL=clickedLRL.get()
                    VVI_URL=str(URL_value.get())
                    VVI_VA=clickedAA.get()
                    VVI_VPW=str(PW_value.get())
                    VVI_VRP=str(VRP_value.get())
                    VVI_VS=V_clicked_sens.get()
                    if int(hyst_value.get()) == 1:
                        VVI_H=clickedLRL.get()
                    else:
                        VVI_H='0'
                    VVI_S=str(smoothingRate.get())

                    f = open("data.json", "r+")
                    data = json.load(f)
                    for i in data:
                        if i["username"] == username:
                            i["VVI"]["LRL"] = VVI_LRL
                            i["VVI"]["URL"] = VVI_URL
                            i["VVI"]["VA"] = VVI_VA
                            i["VVI"]["VPW"] = VVI_VPW
                            i["VVI"]["VRP"] = VVI_VRP
                            i["VVI"]["VS"] = VVI_VS
                            i["VVI"]["H"] = VVI_H
                            i["VVI"]["S"] = VVI_S
                    open("data.json", "w").write(
                        json.dumps(data, indent=4, separators=(',', ': '))
                    )
                print('------------------------------')
                print(currentMode)
                if currentMode == 'AOO' or currentMode == 'VOO':
                    print('Lower Rate Limit', clickedLRL.get() + 'ppm')
                    print('Upper Rate Limit', str(URL_value.get()) + 'ppm')
                    print('Amplitude: ', clickedAA.get(), 'V')
                    print('Pulse Width: ', PW_value.get(), 'V')
                elif currentMode == 'AAI':
                    print('Lower Rate Limit', clickedLRL.get() + 'ppm')
                    print('Upper Rate Limit', str(URL_value.get()) + 'ppm')
                    print('Amplitude: ', clickedAA.get(), 'V')
                    print('Pulse Width: ', PW_value.get(), 'V')
                    print('Refractory Period: ', str(ARP_value.get()) + 'ms')
                    print('A Sensitivity: ', A_clicked_sens.get(), 'mV')
                    print('PVARP: ' + str(PVARP1.get()) + 'ms')
                    if int(hyst_value.get()) == 1:
                        print('Hysterisis Rate Limit, same as LRL=', clickedLRL.get(), 'ppm')
                    else:
                        print('Hysteresis is OFF')
                    print('Smoothing Rate: ', str(smoothingRate.get()) + '%')
                elif currentMode == 'VVI':
                    print('Lower Rate Limit', clickedLRL.get() + 'ppm')
                    print('Upper Rate Limit', str(URL_value.get()) + 'ppm')
                    print('Amplitude: ', clickedAA.get(), 'V')
                    print('Pulse Width: ', PW_value.get(), 'V')
                    print('Refractory Period: ', str(VRP_value.get()) + 'ms')
                    print('V Sensitivity: ', V_clicked_sens.get(), 'mV')
                    print('Hysteresis', hyst_value.get())
                    print('Smoothing Rate: ', str(smoothingRate.get()) + '%')

            def loadValues():
                popUser = Toplevel(app)
                popUser.title = ("Confirm")
                popUser.geometry("550x300+500+250")
                popUser.config(bg='white')
                userInfo = Label(popUser, text='Load Previous Settings for \"' + username + '\" for the ' + currentMode + ' mode?',
                                 fg='#737CA1', bg='white', font=('Microsoft YaHei UI Light', 16, 'bold'))
                userInfo.pack()
                valuesInfo = Label(popUser, text='Previous Settings:', fg='black', bg='white')
                valuesInfo.pack()
                # print(username)
                # print(currentMode)
                f = open("data.json", "r+")
                data = json.load(f)
                if currentMode=='AOO':
                    for i in data:
                        if i["username"] == username:
                            if i["AOO"]["LRL"] == "":
                                print("No previous parameters saved")
                            else:
                                AOO_LRL = i["AOO"]["LRL"]
                                AOO_URL = i["AOO"]["URL"]
                                AOO_AA = i["AOO"]["AA"]
                                AOO_APW = i["AOO"]["APW"]
                                # print('the value obtained: ' + AOO_LRL)
                                aoo_val = Label(popUser, text='LRL: '+AOO_LRL+'\nURL: '+AOO_URL+'\nAmplitude: '+AOO_AA+'\nPulse Width: '+AOO_APW,
                                                   fg='black',font=('Microsoft YaHei UI Light', 12), bg='white')
                                aoo_val.pack()
                elif currentMode=='AAI':
                    f = open("data.json", "r+")
                    data = json.load(f)
                    for i in data:
                        if i["username"] == username:
                            if i["AAI"]["LRL"] == "":
                                print("No previous parameters saved")
                            else:
                                AAI_LRL=i["AAI"]["LRL"]
                                AAI_URL=i["AAI"]["URL"]
                                AAI_AA=i["AAI"]["AA"]
                                AAI_APW=i["AAI"]["APW"]
                                AAI_ARP=i["AAI"]["ARP"]
                                AAI_AS=i["AAI"]["AS"]
                                AAI_PVARP=i["AAI"]["PVARP"]
                                AAI_H=i["AAI"]["H"]
                                AAI_S=i["AAI"]["S"]
                                aai_val = Label(popUser, text='LRL: '+AAI_LRL+'\nURL: '+AAI_URL+'\nAmplitude: '+AAI_AA+'\nPulse Width: '+AAI_APW+
                                                '\nRefactory Period: '+AAI_ARP+'\nSensitivity: '+AAI_AS+'\nPVARP: '+AAI_PVARP+'\nHysterysis: '+AAI_H+'\nSmoothing: '+AAI_S,
                                                   fg='black',font=('Microsoft YaHei UI Light', 12), bg='white')
                                aai_val.pack()
                elif currentMode=='VOO':
                    f = open("data.json", "r+")
                    data = json.load(f)
                    for i in data:
                        if i["username"] == username:
                            if i["VOO"]["LRL"] == "":
                                print("No previous parameters saved")
                        else:
                            VOO_LRL = i["VOO"]["LRL"]
                            VOO_URL = i["VOO"]["URL"]
                            VOO_VA = i["VOO"]["VA"]
                            VOO_VPW = i["VOO"]["VPW"]
                            voo_val = Label(popUser,
                                            text='LRL: ' + VOO_LRL + '\nURL: ' + VOO_URL + '\nAmplitude: ' + VOO_VA + '\nPulse Width: ' + VOO_VPW,
                                            fg='black', font=('Microsoft YaHei UI Light', 12), bg='white')
                            voo_val.pack()
                elif currentMode=='VVI':
                    f = open("data.json", "r+")
                    data = json.load(f)
                    for i in data:
                        if i["username"] == username:
                            if i["VVI"]["LRL"] == "":
                                print("No previous parameters saved")
                            else:
                                VVI_LRL = i["VVI"]["LRL"]
                                VVI_URL = i["VVI"]["URL"]
                                VVI_AA = i["VVI"]["VA"]
                                VVI_APW = i["VVI"]["VPW"]
                                VVI_ARP = i["VVI"]["VRP"]
                                VVI_AS = i["VVI"]["VS"]
                                VVI_H = i["VVI"]["H"]
                                VVI_S = i["VVI"]["S"]
                            vvi_val = Label(popUser, text='LRL: '+VVI_LRL+'\nURL: '+VVI_URL+'\nAmplitude: '+VVI_AA+'\nPulse Width: '+VVI_APW+
                                            '\nRefactory Period: '+VVI_ARP+'\nSensitivity: '+VVI_AS+'\nHysterysis: '+VVI_H+'\nSmoothing: '+VVI_S,
                                               fg='black',font=('Microsoft YaHei UI Light', 12), bg='white')
                            vvi_val.pack()
                def noLoad():
                    popUser.destroy()
                def yesLoad():
                    if currentMode=='AOO':
                        print('LRL: '+AOO_LRL+'\nURL: '+AOO_URL+'\nAmplitude: '+AOO_AA+'\nPulse Width: '+AOO_APW)
                    elif currentMode=='AAI':
                        print('LRL: '+AAI_LRL+'\nURL: '+AAI_URL+'\nAmplitude: '+AAI_AA+'\nPulse Width: '+AAI_APW+
                                                '\nRefactory Period: '+AAI_ARP+'\nSensitivity: '+AAI_AS+'\nPVARP: '+AAI_PVARP+'\nHysterysis: '+AAI_H+'\nSmoothing: '+AAI_S)
                    elif currentMode=='VOO':
                        print('LRL: ' + VOO_LRL + '\nURL: ' + VOO_URL + '\nAmplitude: ' + VOO_VA + '\nPulse Width: ' + VOO_VPW)
                    elif currentMode=='VVI':
                        print('LRL: '+VVI_LRL+'\nURL: '+VVI_URL+'\nAmplitude: '+VVI_AA+'\nPulse Width: '+VVI_APW+
                                            '\nRefactory Period: '+VVI_ARP+'\nSensitivity: '+VVI_AS+'\nHysterysis: '+VVI_H+'\nSmoothing: '+VVI_S)
                    popUser.destroy()

                o1=Button(popUser, width=20, pady=8, text="Yes", bg='#737CA1', fg='white', border=0,command=yesLoad)
                o1.place(x=20,y=250)
                o2=Button(popUser, width=20, pady=8, text="No", bg='#737CA1', fg='white', border=0,command=noLoad)
                o2.place(x=380,y=250)
            def setButton():
                Button(displayFrame, width=30, pady=8, text="Set Values", bg='#737CA1', fg='white', border=0,
                       command=outputVal).place(x=375, y=375)

            def loadPrev():
                Button(displayFrame, width=25, pady=8, text="Load Previous Values", bg='#737CA1', fg='white', border=0,
                       command=loadValues).place(x=0, y=375)

            app.mainloop()
        else:
            messagebox.showerror("Invalid Entry", "Invalid username or password!")
    except:
        messagebox.showerror("Error", "No users found, please register first!")


## SIGN UP POP-UP
def registerPopup():
    window = Toplevel(main)
    window.title("Register")
    window.geometry('300x400+850+200')
    window.configure(bg='#fff')
    window.resizable(False, False)

    Label(window, text='Register', fg='#737CA1', bg='white', font=('Microsoft YaHei UI', 24)).place(x=75, y=20)

    ## REGISTER
    def register():
        username = user.get()
        password = pw.get()
        passwordConfirm = pwConfirm.get()
        specialCharacters = "!@#$%^&*()-+?_+=,<>:;\'\"|[]{}`~/\ "

        if password == passwordConfirm:
            if username != '' and username != 'Username':
                if not(any(c in specialCharacters for c in username)):
                    try:
                        file = open('database.txt', 'r+')
                        d = file.read()
                        r = ast.literal_eval(d)
                        dict1 = {username: password}
                        if username in r.keys():
                            messagebox.showerror('Error', 'User Already Exists!')
                            window.destroy()
                        else:
                            if len(r) <= 10:
                                r.update(dict1)
                                file.truncate(0)
                                file.close()
                                file = open('database.txt', 'w')
                                w = file.write(str(r))
                                try:
                                    f = open("data.json", "r+")
                                    data = json.load(f)
                                    newUserData = {"username": f"{username}",
                                                     "AOO": {
                                                         "LRL": "",
                                                         "URL": "",
                                                         "AA": "",
                                                         "APW": ""
                                                     },
                                                     "AAI": {
                                                         "LRL": "",
                                                         "URL": "",
                                                         "AA": "",
                                                         "APW": "",
                                                         "ARP": "",
                                                         "AS": "",
                                                         "PVARP": "",
                                                         "H": "",
                                                         "S": ""
                                                     },
                                                     "VOO": {
                                                         "LRL": "",
                                                         "URL": "",
                                                         "VA": "",
                                                         "VPW": ""
                                                     },
                                                     "VVI": {
                                                         "LRL": "",
                                                         "URL": "",
                                                         "VA": "",
                                                         "VPW": "",
                                                         "VRP": "",
                                                         "VS": "",
                                                         "H": "",
                                                         "S": ""
                                                     }}
                                    data.append(newUserData)
                                    f.seek(0)
                                    json.dump(data, f, indent=4)
                                    f.close()
                                except:
                                    messagebox.showerror("Critical Error!",
                                                         "Critical Error, do not alter data files! Delete database.txt and restart to continue!")
                                messagebox.showinfo('Success', 'Registered Successfully!')
                                window.destroy()
                            else:
                                messagebox.showerror('Error', 'User Capacity Reached!')
                    except:
                        file = open('database.txt', 'w')
                        pp = str({'Username': 'password'})
                        file.write(pp)
                        file.close()
                        # created txt file^ now add user:
                        file = open('database.txt', 'r+')
                        d = file.read()
                        r = ast.literal_eval(d)
                        dict1 = {username: password}
                        if len(r) <= 10:
                            r.update(dict1)
                            file.truncate(0)
                            file.close()
                            file = open('database.txt', 'w')
                            w = file.write(str(r))
                            try:
                                pp1=[{"username": " ",
                                                     "AOO": {
                                                         "LRL": "",
                                                         "URL": "",
                                                         "AA": "",
                                                         "APW": ""
                                                     },
                                                     "AAI": {
                                                         "LRL": "",
                                                         "URL": "",
                                                         "AA": "",
                                                         "APW": "",
                                                         "ARP": "",
                                                         "AS": "",
                                                         "PVARP": "",
                                                         "H": "",
                                                         "S": ""
                                                     },
                                                     "VOO": {
                                                         "LRL": "",
                                                         "URL": "",
                                                         "VA": "",
                                                         "VPW": ""
                                                     },
                                                     "VVI": {
                                                         "LRL": "",
                                                         "URL": "",
                                                         "VA": "",
                                                         "VPW": "",
                                                         "VRP": "",
                                                         "VS": "",
                                                         "H": "",
                                                         "S": ""
                                                     }}]
                                with open('data.json','w') as f:
                                    json.dump(pp1,f,indent=4)
                                f.close()
                                f = open("data.json", "r+")
                                data = json.load(f)
                                newUserData = {"username": f"{username}",
                                               "AOO": {
                                                   "LRL": "",
                                                   "URL": "",
                                                   "AA": "",
                                                   "APW": ""
                                               },
                                               "AAI": {
                                                   "LRL": "",
                                                   "URL": "",
                                                   "AA": "",
                                                   "APW": "",
                                                   "ARP": "",
                                                   "AS": "",
                                                   "PVARP": "",
                                                   "H": "",
                                                   "S": ""
                                               },
                                               "VOO": {
                                                   "LRL": "",
                                                   "URL": "",
                                                   "VA": "",
                                                   "VPW": ""
                                               },
                                               "VVI": {
                                                   "LRL": "",
                                                   "URL": "",
                                                   "VA": "",
                                                   "VPW": "",
                                                   "VRP": "",
                                                   "VS": "",
                                                   "H": "",
                                                   "S": ""
                                               }}
                                data.append(newUserData)
                                f.seek(0)
                                json.dump(data, f, indent=4)
                                f.close()
                            except:
                                messagebox.showerror("Critical Error!",
                                                     "Critical Error, do not alter data files! Delete database.txt and data.json and restart to continue!")
                            messagebox.showinfo('Success', 'Registered Successfully!')
                            window.destroy()
                        else:
                            messagebox.showerror('Error', 'User Capacity Reached!')
                else:
                    messagebox.showerror('Error', 'No Special Characters or Spaces Allowed!')
            else:
                messagebox.showerror('Error', 'Username cannot be blank!')
        else:
            messagebox.showerror('Error', 'Passwords do not match!')

    ## CLEAR DATABASE
    def deleteDatabase():
        try:
            os.remove('database.txt')
            file = open('database.txt', 'w')
            pp = str({'Username': 'password'})
            file.write(pp)
            file.close()
            os.remove('data.json')
            pp1 = [{"username": " ",
                    "AOO": {
                        "LRL": "",
                        "URL": "",
                        "AA": "",
                        "APW": ""
                    },
                    "AAI": {
                        "LRL": "",
                        "URL": "",
                        "AA": "",
                        "APW": "",
                        "ARP": "",
                        "AS": "",
                        "PVARP": "",
                        "H": "",
                        "S": ""
                    },
                    "VOO": {
                        "LRL": "",
                        "URL": "",
                        "VA": "",
                        "VPW": ""
                    },
                    "VVI": {
                        "LRL": "",
                        "URL": "",
                        "VA": "",
                        "VPW": "",
                        "VRP": "",
                        "VS": "",
                        "H": "",
                        "S": ""
                    }}]
            with open('data.json', 'w') as f:
                json.dump(pp1, f, indent=4)
            f.close()

        except:
            messagebox.showinfo('Info', 'Database has been removed.')

    Button(window, text="X", bg='white', fg='#E5E4E2', border=0, command=deleteDatabase).place(x=0, y=380)

    ## USERNAME FIELD
    def onEnter(e):
        user.delete(0, 'end')

    def onExit(e):
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(window, width=25, fg='#737CA1', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    user.place(x=30, y=110)
    user.insert(0, 'Username')
    user.bind("<FocusIn>", onEnter)
    user.bind("<FocusOut>", onExit)
    Frame(window, width=250, height=2, bg='#737CA1').place(x=25, y=137)

    ## PASSWORD FIELD
    def onEnter(e):
        pw.delete(0, 'end')

    def onExit(e):
        if pw.get() == '':
            pw.insert(0, 'Password')

    pw = Entry(window, width=25, fg='#737CA1', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    pw.place(x=30, y=170)
    pw.insert(0, 'Password')
    pw.bind("<FocusIn>", onEnter)
    pw.bind("<FocusOut>", onExit)
    Frame(window, width=250, height=2, bg='#737CA1').place(x=25, y=197)

    ## CONFIRM PASSWORD FIELD
    def onEnter(e):
        pwConfirm.delete(0, 'end')

    def onExit(e):
        if pwConfirm.get() == '':
            pwConfirm.insert(0, 'Confirm Password')

    pwConfirm = Entry(window, width=25, fg='#737CA1', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
    pwConfirm.place(x=30, y=230)
    pwConfirm.insert(0, 'Confirm Password')
    pwConfirm.bind("<FocusIn>", onEnter)
    pwConfirm.bind("<FocusOut>", onExit)
    Frame(window, width=250, height=2, bg='#737CA1').place(x=25, y=257)

    ## SIGN UP BUTTON
    Button(window, width=30, pady=8, text="Sign Up", bg='#737CA1', fg='white', border=0, command=register).place(x=40,y=335)
    ## NOTE
    Label(window, text="Note: Special characters and spaces\n are not allowed for username", fg='#737CA1', bg='white', font=('Microsoft YaHei UI Light', 8)).place(x=50, y=275)

    window.mainloop()



## USERNAME BOX
def onEnter(e):
    user.delete(0, 'end')

def onExit(e):
    if user.get() == '':
        user.insert(0, 'Username')


user = Entry(frame, width=36, fg='#737CA1', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=75, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', onEnter)
user.bind('<FocusOut>', onExit)
Frame(frame, width=295, height=2, bg='#737CA1').place(x=70, y=110)


## PASSWORD BOX
def onEnter1(e):
    pw.delete(0, 'end')


def onExit1(e):
    if pw.get() == '':
        pw.insert(0, 'Password')


pw = Entry(frame, width=36, fg='#737CA1', border=0, bg='white', font=('Microsoft YaHei UI Light', 11), show='')
pw.place(x=75, y=150)
pw.insert(0, 'Password')
pw.bind('<FocusIn>', onEnter1)
pw.bind('<FocusOut>', onExit1)
Frame(frame, width=295, height=2, bg='#737CA1').place(x=70, y=180)


## PASSWORD HIDER
def hidePass():
    if pw.cget('show') == '*':
        pw.config(show='')
    else:
        pw.config(show='*')


checkButton = Checkbutton(main, text="Hide Password", bg='white', command=hidePass)
checkButton.place(x=550, y=260)
## SIGN IN BUTTON
Button(frame, width=30, pady=8, text='Sign in', bg='#737CA1', fg='white', border=0, command=signin).place(x=110, y=225)
# SIGN UP
Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 10)).place(x=120,y=265)
Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=registerPopup).place(
    x=270, y=267)

main.mainloop()
