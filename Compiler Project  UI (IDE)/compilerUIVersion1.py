import PySimpleGUI as sh
sh.theme('DarkPurple4')

#TanBlue



sh.set_options(text_color='white', background_color='#311D3f', text_element_background_color='#522546')

layout = [[ sh.Text('Simple IDE Version1', size=(
        30, 1), justification='center', font=("Helvetica", 15), relief=sh.RELIEF_RIDGE)],
    
          [sh.Text('You type your code here:'),],
           
          [sh.Multiline(size=(30, 5), key='textbox')],
          [sh.Button('Run'), sh.Button('Exit')]]

window = sh.Window('compilerUIVersion1', layout,size=(1350, 599), resizable=True,finalize=True)
window['textbox'].expand(expand_x=True, expand_y=True)

while True:  # Event Loop
    event, values = window.read()
    print(event, values['textbox'])
    if event == sh.WIN_CLOSED or event == 'Exit':
        break
    
        
        

window.close()