{
    "name": "Campus_Management",
    "version": "16.0.1.0.0",
    "author": "Dhafi Alfaridzi.",
    "category": "Extra Tools",
    "license": "LGPL-3",
    "website": "https://arkana.co.id",
    "depends": ["contacts"],
    "data": [
        'security/ir.model.access.csv',
        'views/training_class_view.xml',
        'views/menu.xml',
        'views/pelajaran_admin.xml',
    ],
    "auto_install": False,
    'application': True, #wajib
    "installable": True,
}
