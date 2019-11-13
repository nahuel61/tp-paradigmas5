import datetime
import os
import wx
import wx.lib.inspection


class VentanaPrincipal(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(800, 685))
        self.panel = wx.Panel(self)
        frame = wx.GridBagSizer()

        '''# Cuadro para cargar el texto'''

        self.titulo = wx.StaticText(self, -1, label='Ingrese el texto aqui:')
        frame.Add(self.titulo, (0, 0), border=50)
        self.entrada = wx.TextCtrl(self, -1, value='', style=wx.TE_PROCESS_ENTER)
        frame.Add(self.entrada, (1, 0), (1, 7), wx.EXPAND)
        self.entrada.Bind(wx.EVT_TEXT_ENTER, self.SiPulsaEnter)
        frame.AddGrowableCol(1)

        '''# panel que muestra las palabras en texto'''

        self.etiqueta = wx.StaticText(self, -1, label='Bienvenido!')
        self.etiqueta.SetBackgroundColour('grey')
        self.etiqueta.SetForegroundColour('green')
        frame.Add(self.etiqueta, (2, 0), (1, 7), wx.EXPAND)
        frame.AddGrowableCol(0)

        '''# panel q mostraria los leds'''

        self.tablero = wx.GridSizer(rows=6, cols=6, hgap=1, vgap=1)
        self.paneles = []
        for i in range(36):
            nuevopanel = wx.Panel(self, size=wx.Size(50, 100))
            self.tablero.Add(nuevopanel, 0, wx.EXPAND)
            self.paneles.append(nuevopanel)
            self.paneles[i].SetBackgroundColour('black')
            # self.paneles.Refresh()
        frame.Add(self.tablero, (3, 0), (7, 7), wx.EXPAND)

        '''botones que muestran la hora y cambian colores del texto'''
        botonhora = wx.Button(self, -1, label="Mostrar Hora")
        frame.Add(botonhora, (12, 0), (1, 7), wx.EXPAND)
        botonhora.Bind(wx.EVT_BUTTON, self.ClickBoton)

        botonrojo = wx.Button(self, -1, label='Letras Rojas')
        frame.Add(botonrojo, (13, 0), (1, 7), wx.EXPAND)
        botonrojo.Bind(wx.EVT_BUTTON, self.SetColorRojo)

        botonazul = wx.Button(self, -1, label='Letras Azules')
        frame.Add(botonazul, (14, 0), (1, 7), wx.EXPAND)
        botonazul.Bind(wx.EVT_BUTTON, self.SetColorAzul)

        botonverde = wx.Button(self, -1, label='Letras Verdes')
        frame.Add(botonverde, (15, 0), (1, 7), wx.EXPAND)
        botonverde.Bind(wx.EVT_BUTTON, self.SetColorVerde)

        self.SetSizerAndFit(frame)

        self.InitUI()
        # wx.lib.inspection.InspectionTool().Show()

    def InitUI(self):

        # creo barra de menu
        menubar = wx.MenuBar()

        # menu de opciones
        opcionesmenu = wx.Menu()
        menubar.Append(opcionesmenu, 'Opciones')
        archivoitem = opcionesmenu.Append(-1, 'Abrir archivo')
        horaitem = opcionesmenu.Append(-1, 'Mostrar hora')
        saliritem = opcionesmenu.Append(-1, 'Salir')

        # menu de texto
        textomenu = wx.Menu()
        menubar.Append(textomenu, 'Texto')
        textoitem = textomenu.Append(-1, 'Insertar texto')

        # submenu de seleccion de color
        colortexto = wx.Menu()
        rojo = colortexto.Append(wx.ID_ANY, 'Rojo')
        verde = colortexto.Append(wx.ID_ANY, 'Verde')
        azul = colortexto.Append(wx.ID_ANY, 'Azul')
        textomenu.AppendSubMenu(colortexto, 'Seleccion color')

        # submenu de seleccion de velocidad
        velocidadtextoitem = textomenu.Append(-1, 'Seleccion de velocidad')

        # menu de ayuda
        ayudamenu = wx.Menu()
        menubar.Append(ayudamenu, 'Ayuda')
        ayudaitem = ayudamenu.Append(wx.ID_ABOUT, 'Autor')

        self.SetMenuBar(menubar)

        # operaciones de cada menu
        self.Bind(wx.EVT_MENU, self.Salir, saliritem)
        self.Bind(wx.EVT_MENU, self.ClickBoton, horaitem)
        self.Bind(wx.EVT_MENU, self.AbrirArchivo, archivoitem)
        self.Bind(wx.EVT_MENU, self.SiPulsaEnter, textoitem)
        self.Bind(wx.EVT_MENU, self.SetColorRojo, rojo)
        self.Bind(wx.EVT_MENU, self.SetColorVerde, verde)
        self.Bind(wx.EVT_MENU, self.SetColorAzul, azul)
        self.Bind(wx.EVT_MENU, self.MostrarAutor, ayudaitem)

        self.SetSize((800, 600))
        self.Centre()
        self.Show(True)

    def Salir(self, e):
        self.Close()

    def ClickBoton(self, e):
        """muestra la hora actual al pulsar el boton hora"""
        dt = datetime.datetime.now()
        fecha = "{:02d}:{:02d}".format(dt.hour, dt.minute)
        self.etiqueta.SetLabel(fecha)
        self.etiqueta.Refresh()
        self.entrada.Clear()

    def SiPulsaEnter(self, e):
        """inserta el texto cargado y lo muestra en la etiqueta"""
        self.etiqueta.SetLabel(self.entrada.GetValue())
        self.etiqueta.Refresh()
        self.entrada.Clear()

    def AbrirArchivo(self, e):
        """desde el menu opciones abre un archivo y lee el texto"""
        tipo = "TXT files (*.txt)|*.txt"
        dialog = wx.FileDialog(self, "Open Text Files", wildcard=tipo)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return
        path = dialog.GetPath()

        if os.path.exists(path):
            with open(path) as archivo:
                for linea in archivo:
                    self.entrada.WriteText(linea)

    def SetColorRojo(self, e):
        self.etiqueta.SetForegroundColour('red')

    def SetColorAzul(self, e):
        self.etiqueta.SetForegroundColour('blue')

    def SetColorVerde(self, e):
        self.etiqueta.SetForegroundColour('green')

    def MostrarAutor(self, e):
        """muestra autor del trabajo desde el menu ayuda"""
        autor = VentanaAutor(self)
        autor.ShowModal()
        autor.Destroy()


class VentanaAutor(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title='Autor', size=(250, 80))
        wx.StaticText(self, label='CT Nahuel Daniel Salazar Gomez')
        self.Centre()


class MyApp(wx.App):
    def __init__(self):
        super().__init__()
        self.frame = VentanaPrincipal(parent=None, title="LED OBJECTS")

        self.frame.Show()


if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
