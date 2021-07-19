{
    'name': "Nombre Que Se Ve En Apps de Odoo",
    'author': 'Nombre Del Autor',
    # en version, se coloca al inicio la versión de odoo
    'version': '14.0.1.0.0',
    'summary': 'Descripción breve',
    'description': """Descripción larga con más detalles del funcionamiento del módulo""",
    'website': 'redytec.com',
    'depends': [
        'purchase',
    ],
    'data': [
        # Aquí se mandan llamar todos los archivos .xml y .csv, primero se escribe la carpeta
        # en la que están y luego el nombre completo del archivo
        'security/ir.model.access.csv',
        'data/data.xml',
        'wizard/crear_wizard_view.xml',
        'views/modulo_vista.xml',
        'views/purchase_order_herencia_vista.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    # application no es necesario establecerlo, el valor default es falso y solo afecta la vista
    # que tendrá dentro de odoo
    'application': True,
    'auto:install': False,
}