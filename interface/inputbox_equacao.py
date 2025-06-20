from interface.input_box import InputBox

class InputBoxEquacao(InputBox):
    def interpretar_equacao(self):
        import re

        texto = self.texto.replace(' ', '').lower().replace('x²', 'x^2')
        match = re.findall(r'([+-]?\d*\.?\d*)x\^2|([+-]?\d*\.?\d*)x(?!\^)|([+-]?\d+\.?\d*)', texto)

        a = b = c = 0.0
        for grupo in match:
            if grupo[0]:
                a = float(grupo[0] or '1' if grupo[0] in ('+', '') else '-1' if grupo[0] == '-' else grupo[0])
            elif grupo[1]:
                b = float(grupo[1] or '1' if grupo[1] in ('+', '') else '-1' if grupo[1] == '-' else grupo[1])
            elif grupo[2]:
                c = float(grupo[2])

        return a, b, c
