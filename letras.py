import wx


def ValoresLetras(letra) -> list:
    valores = {
        'A': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 0, 0, 0, 0, 0],
        'B': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'C': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 1, 0,
              0, 0, 0, 0, 0, 0, 0],
        'D': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'E': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 0, 0, 0, 0, 0, 0],
        'F': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'G': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 0, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'H': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 0, 0, 0, 0, 0],
        'I': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'J': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 1, 0, 1, 0, 0, 0,
              0, 0, 1, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'K': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 1, 0, 0,
              0, 1, 0, 1, 0, 0, 0,
              0, 1, 1, 0, 0, 0, 0,
              0, 1, 0, 1, 0, 0, 0,
              0, 1, 0, 0, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'L': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'M': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 1, 0, 1, 1, 0,
              0, 1, 0, 1, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 0, 0, 0, 0, 0],
        'N': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 1, 0, 0, 1, 0,
              0, 1, 0, 1, 0, 1, 0,
              0, 1, 0, 0, 1, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 0, 0, 0, 0, 0],
        'O': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'P': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'Q': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 1, 1, 0,
              0, 0, 1, 1, 1, 1, 0,
              0, 0, 0, 0, 0, 0, 1],
        'R': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 0, 0, 0, 0, 0],
        'S': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'T': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'U': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'V': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 0, 1, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'X': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 0, 1, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 1, 0, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 0, 0, 0, 0, 0],
        'Y': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 0, 1, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        'Z': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 0, 0, 0, 1, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 1, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 0, 0, 0, 0, 0, 0],
        '0': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 1, 1, 0,
              0, 1, 0, 1, 0, 1, 0,
              0, 1, 1, 0, 0, 1, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        '1': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 1, 1, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        '2': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 1, 0, 0,
              0, 0, 0, 1, 0, 0, 0,
              0, 0, 1, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        '3': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        '4': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 1, 1, 0, 0,
              0, 0, 1, 0, 1, 0, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 0, 0, 0, 1, 0, 0,
              0, 0, 0, 0, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        '5': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        '6': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 1, 0,
              0, 1, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        '7': [0, 0, 0, 0, 0, 0, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 1, 0, 0,
              0, 0, 0, 1, 1, 1, 0,
              0, 0, 0, 0, 1, 0, 0,
              0, 0, 0, 0, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        '8': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0],
        '9': [0, 0, 0, 0, 0, 0, 0,
              0, 0, 1, 1, 1, 0, 0,
              0, 1, 0, 0, 0, 1, 0,
              0, 0, 1, 1, 1, 1, 0,
              0, 0, 0, 0, 0, 1, 0,
              0, 1, 1, 1, 1, 0, 0,
              0, 0, 0, 0, 0, 0, 0]
    }
    return valores[letra]


class Caracteres(wx.Panel):

    def __init__(self, parent=wx.Frame, letra=' '):
        super().__init__(parent)
        self.letra = letra
        self.paneles = []
        self.InitUI()

    def InitUI(self):
        grid = wx.GridSizer(7, 7, 1, 1)

        for i in range(49):
            self.paneles.append(wx.Panel(self, size=wx.Size(10, 10)))

        for value, panel in zip(ValoresLetras(self.letra), self.paneles):
            if value == 1:
                panel.SetBackgroundColour('green')
            else:
                panel.SetBackgroundColour('black')
            grid.Add(panel, 0, wx.EXPAND)
        self.SetSizer(grid)
