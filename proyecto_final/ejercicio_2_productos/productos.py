import json
from pathlib import Path

class StockInvalidoError(Exception):
    pass

class DispositivoEcologico:

    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, valor):
        if valor < 0:
            raise StockInvalidoError(f'El stock no puede ser negativo (recibido: {valor})')
        self._stock = valor

    def ficha_tecnica(self):
        return f'{self.nombre} | Precio: ${self.precio} | Stock: {self.stock}'

    def to_dict(self):
        return {'tipo': self.__class__.__name__, 'nombre': self.nombre, 'precio': self.precio, 'stock': self.stock}

class PanelSolar(DispositivoEcologico):

    def __init__(self, nombre, precio, stock, potencia_w, eficiencia):
        super().__init__(nombre, precio, stock)
        self.potencia_w = potencia_w
        self.eficiencia = eficiencia

    def ficha_tecnica(self):
        return f'[PANEL SOLAR] {self.nombre}\n  Potencia: {self.potencia_w} W\n  Eficiencia: {self.eficiencia}%\n  Precio: ${self.precio} | Stock: {self.stock}'

    def to_dict(self):
        datos = super().to_dict()
        datos.update({'potencia_w': self.potencia_w, 'eficiencia': self.eficiencia})
        return datos

class GestorInventario:

    def guardar_catalogo_json(self, lista_dispositivos, ruta_archivo):
        datos = [dispositivo.to_dict() for dispositivo in lista_dispositivos]
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
if __name__ == '__main__':
    gestor = GestorInventario()
    catalogo = []
    intentos = [('Panel Solar Pro', 150000, 10, 450, 21.5), ('Panel Solar Lite', 90000, -5, 300, 18.0), ('Panel Solar Max', 210000, 3, 550, 22.8)]
    print('=== Alta de productos ===')
    for nombre, precio, stock, potencia, eficiencia in intentos:
        try:
            panel = PanelSolar(nombre, precio, stock, potencia, eficiencia)
            catalogo.append(panel)
            print(panel.ficha_tecnica())
            print('-' * 30)
        except StockInvalidoError as error:
            print(f"⚠️  No se pudo crear '{nombre}': {error}")
            print('-' * 30)
    ruta = Path(__file__).resolve().parent / 'catalogo_ecotech.json'
    gestor.guardar_catalogo_json(catalogo, ruta)
    print(f'✅ Se guardaron {len(catalogo)} productos en {ruta.name}')
