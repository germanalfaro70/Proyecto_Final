# EcoTech Solutions: Proyecto Final Integrador

Proyecto organizado en tres carpetas independientes, una por ejercicio.

```
proyecto_final_ecotech/
├── README.md
├── requirements.txt
├── ejercicio_1_sensores/
│   ├── sensores.py
│   └── test_sensores.py
├── ejercicio_2_productos/
│   ├── productos.py
│   ├── test_productos.py
│   └── catalogo_ecotech.json        (se genera al ejecutar productos.py)
└── ejercicio_3_auditoria_web/
    ├── manage.py
    ├── pytest.ini
    ├── config/                      (settings y urls del proyecto Django)
    ├── data/registros_consumo.csv   (datos simulados de consumo)
    ├── templates/sustentabilidad/panel.html
    └── sustentabilidad/
        ├── emisiones.py             (cálculo de huella de carbono)
        ├── metricas.py              (obtener_metricas_consumo)
        ├── views.py                 (vista_panel_sustentabilidad, FBV)
        ├── urls.py
        └── tests/
            ├── test_emisiones.py    (unittest)
            ├── test_metricas.py
            └── test_vistas.py
```

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

**Ejercicio 1**
```bash
cd ejercicio_1_sensores
python sensores.py
python -m unittest -v test_sensores.py
```

**Ejercicio 2**
```bash
cd ejercicio_2_productos
python productos.py
python -m unittest -v test_productos.py
```

**Ejercicio 3**
```bash
cd ejercicio_3_auditoria_web
pytest -v                       # tests unitarios y de integración
python manage.py runserver      # luego abrir http://127.0.0.1:8000/sustentabilidad/panel/
```
