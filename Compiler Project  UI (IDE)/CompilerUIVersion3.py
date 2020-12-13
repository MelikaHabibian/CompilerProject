import PySimpleGUI as sh

sh.theme('DarkPurple7')


menu_def = [['&Settings', ['View', ['Themes',[ '&Dark Grey', '&Light Blue']], 
             'Perfences', [ 'Auto Complete', 'Color Code']]],
            ['&Start', ['Run', 'Debug', 'Clear Terminal', ' Clear Code Box']],
            ['&Guide', '&Cheet Sheet'], ]

play_ic = b'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'
text1 = sh.Multiline(size=(30, 5), key='textbox')
text2 = sh.Multiline(size=(15, 5), key='console' )
button_run = sh.Button('Run',border_width=0, image_size=(50,20),button_color=(sh.theme_background_color(),sh.theme_background_color()),  image_data= play_ic,font=("Verdana", 10) ),sh.Button('Debug',font=("Verdana", 10) ),sh.Button('Clean All', font=("Verdana", 10))
layout = [[sh.Menu(menu_def, tearoff=True)],
        [ sh.Text('Simple IDE Version2', size=(30, 1), 
        justification='center', font=("Verdana", 15), relief=sh.RELIEF_RIDGE)],
    
          [sh.Text('You type your code here:',  font=("Verdana", 10) )],
           
          [text1],
          [sh.Button('Run',border_width=0, image_size=(50,20),button_color=(sh.theme_background_color(),sh.theme_background_color()),  image_data= play_ic,font=("Verdana", 10) ),sh.Button('Debug',font=("Verdana", 10) ),sh.Button('Clean All', font=("Verdana", 10))],
          [sh.Text('Terminal',font=("Verdana", 10), relief=sh.RELIEF_GROOVE)],
          [text2],
          [sh.Button('Clean Terminal', font=("Verdana", 10)), sh.Button('Exit', font=("Verdana", 10))]]



window = sh.Window('compilerUIVersion1', layout,size=(1350, 599), resizable=True, finalize=True )
window['textbox'].expand(expand_x=True, expand_y=True)
window['console'].expand(expand_x=True, expand_y=True)


while True:  # Event Loop
    event, values = window.read()
  
    if event == sh.WIN_CLOSED or event == 'Exit':
        break
        print(event, values) 
    if event == 'Light Blue' :
         window.TKroot.config(background='LightBlue')
         text1.update(background_color='White')
         text2.update(background_color='White')
         
    if event == 'Dark Grey' :
        window.TKroot.config(background='#222831')
        text1.update(background_color='#222831')
        text2.update(background_color='#222831')
        
        
        
        
        
         
    
        
        

window.close()