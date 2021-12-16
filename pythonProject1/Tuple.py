import PySimpleGUI as sg

# This is the normal print that comes with simple GUI
sg.Print('Re-routing the stdout', do_not_reroute_stdout=False)

# this is clobbering the print command, and replacing it with sg's Print()
print = sg.Print

# this will now output to the sg display.
print('This is a normal print that has been re-routed.')