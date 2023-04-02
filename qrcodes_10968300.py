'''
SENG 207 PROGRAMMING PROJECT 2(b)
GENERATING QR CODE DESKTOP APPLICATION
INDEX NUMBER: 10968300
NAME: NYARKOA PRISCILLA YEBOAH
DEPARTMENT: FOOD PROCESS ENGINEERING
'''
import qrcode
import PySimpleGUI as psg
import os

psg.theme('Topanga')
psg.theme_button_color('black')
psg.theme_input_background_color('white')
psg.theme_input_text_color('black')
psg.theme_element_text_color('yellow')
psg.theme_text_color('white')

layout = [
    [psg.Text('Enter text here:'), psg.InputText(key='text')],
    [psg.Text('Choose QR code size:'), psg.Slider(range=(1, 20), orientation='h', default_value=5, key='size')],
    [psg.Text('Choose QR code color:')],
    [psg.Radio('Yellow',"COLOR", default=True, key='color_yellow'), psg.Radio('Red', "COLOR", key='color_red')],
    [psg.Button('Generate QR Code')],
    [psg.Image(key='image')],
    [psg.Text('Designed by Priscilla Nyarkoa Yeboah')]
]

window = psg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()
    if event == psg.WINDOW_CLOSED:
        break

    if event == 'Generate QR Code':
        qr = qrcode.QRCode(version=1, box_size=values['size'], border=4)
        qr.add_data(values['text'])
        qr.make(fit=True)
        img = qr.make_image(fill_color='Yellow' if values['color_yellow'] else 'Red', back_color='white')
    
        img_file = 'qrcodg' + '.png'
        path = os.path.join(os.getcwd(),img_file)
        img.save(path)

        window['image'].update(filename=path)

window.close()