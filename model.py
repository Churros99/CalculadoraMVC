class Model:
    
    
    def __init__(self):
        self.prevValue = '0'
        self.value = '0'
        self.operator = ''
    
    def calculate(self, caption):
        if caption == 'C':
            # Volvemos a valor 0
            self.prevValue = '0'
            self.value = '0'
        elif caption == '+/-':
            #  Convertimos el valor a positivo o negativo
            self.value = self.value[1:] if self.value[0]=='-'else '-'+self.value
        elif caption =='%':
            # Proceso de porcentaje
            value = float(self.value) if '.' in self.value else int(self.value)
            self.value = str(value/100)
        elif caption =='=':
            # Proceso de igual
            value = str(self._evaluate())
            if('.0' in value):
                value = int(value)
            
            self.value = str(value)  
                
        elif isinstance(caption, int) or caption =='.':
            # Acumulamos todos los valores numericos
            if self.value == '0':
                self.value = str(caption)
            elif caption == '.':
                if not caption in self.value:
                    self.value += caption
            else:
                self.value += str(caption)
        else:
            if self.value:
                self.operator = caption
                self.prevValue = self.value
                self.value = '0'
            
            
        return self.value
    
    def _evaluate(self):
        return eval(self.prevValue+self.operator+self.value)
    