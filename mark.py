import PySimpleGUI as sg

layout = [
    [sg.Button('Tombol 1'), sg.Button('Tombol 2')],
    [sg.Text('', key='-OUTPUT-')]
]

window = sg.Window('Contoh Mendapatkan Teks Tombol', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event.startswith('Tombol'):
        tombol_teks = event  # event berisi teks tombol yang ditekan
        window['-OUTPUT-'].update(f'Anda menekan tombol: {tombol_teks}')

window.close()
