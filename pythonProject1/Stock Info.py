import PySimpleGUI as sg

# Design pattern 2 - First window does remain active
layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)], # I want the output of win2 to show up here, so value of "chosenWell" str
          [sg.Text('', key='_OUTPUT_')],
          [sg.Button('Launch 2'), sg.Button('Exit')]]

win1 = sg.Window('Window 1').Layout(layout)
win2_active=False
while True:
    ev1, vals1 = win1.Read(timeout=100)
    win1.FindElement('_OUTPUT_').Update(vals1[0])
    if ev1 is None or ev1 == 'Exit':
        break

    if ev1 == 'Launch 2' and not win2_active:
        cols=7
        sg.theme('BluePurple')
        win2_active = True
        layout2 = [[sg.Text('Window 2 - for diagram/selection of spot on consumable')],
                   [sg.B('\u20DD',size=(6,2),button_color=('orange','#223344'),key=(1,f'{i+1}'),pad=(0,0)) for i in range(cols)]+[sg.T(' ')],
                   [sg.T(' ')]+[sg.B('\u20DD',size=(6,2),button_color=('orange','#223344'),key=(2,f'{i+1}'),pad=(0,0)) for i in range(cols)],
                   [sg.B('\u20DD',size=(6,2),button_color=('orange','#223344'),key=(3,f'{i+1}'),pad=(0,0)) for i in range(cols)]+[sg.T(' ')],
                   [sg.T(' ')]+[sg.B('\u20DD',size=(6,2),button_color=('orange','#223344'),key=(4,f'{i+1}'),pad=(0,0)) for i in range(cols)],
                   [sg.B('\u20DD',size=(6,2),button_color=('orange','#223344'),key=(5,f'{i+1}'),pad=(0,0)) for i in range(cols)]+[sg.T(' ')]
                  ]
        win2 = sg.Window('',no_titlebar=True,alpha_channel=.9,grab_anywhere=True,element_justification='c').Layout(layout2)

    if win2_active:
        ev2, vals2 = win2.Read()
        if ev2 is None or ev2 == 'Exit':
            win2.Close()
            win2_active = False
        chosenWell=ev2
        print(chosenWell)
        win2.close()

win1.close()