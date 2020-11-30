import PySimpleGUI as sh

sh.theme('DarkPurple4')


menu_def = [['&Settings', ['View', ['Themes',[ 'Dark Blue', 'Tan Blue']], 
             'Perfences', [ 'Auto Complete', 'Color Code']]],
            ['&Start', ['Run', 'Debug', 'Clear Terminal', ' Clear Code Box']],
            ['&Guide', '&Cheet Sheet'], ]



layout = [[sh.Menu(menu_def, tearoff=True)],
        [ sh.Text('Simple IDE Version2', size=(30, 1), 
        justification='center', font=("Verdana", 15), relief=sh.RELIEF_RIDGE)],
    
          [sh.Text('You type your code here:',  font=("Verdana", 10) )],
           
          [sh.Multiline(size=(30, 5), key='textbox')],
          [sh.Button('Run',font=("Verdana", 10) ),sh.Button('Debug',font=("Verdana", 10) ),sh.Button('Clean All', font=("Verdana", 10))],
          [sh.Text('Terminal',font=("Verdana", 10), relief=sh.RELIEF_GROOVE)],
          [sh.Multiline(size=(15, 5), key='terminal', )],
          [sh.Button('Clean Terminal', font=("Verdana", 10)), sh.Button('Exit', font=("Verdana", 10))]]



window = sh.Window('compilerUIVersion1', layout,size=(1350, 599), resizable=True,finalize=True)
window['textbox'].expand(expand_x=True, expand_y=True)
window['terminal'].expand(expand_x=True, expand_y=True)

while True:  # Event Loop
    event, values = window.read()
    print(event, values['textbox'])
    if event == sh.WIN_CLOSED or event == 'Exit':
        break
    
        
        

window.close()