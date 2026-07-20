{
    'name': 'Spedizione a Percentuale con Minimo',
    'version': '1.0.0',
    'category': 'Sales/Delivery',
    'summary': 'Metodo di consegna calcolato in percentuale sul totale ordine, con importo minimo',
    'description': """
        Aggiunge un nuovo metodo di consegna (Delivery Carrier) che calcola il costo
        di spedizione come percentuale del totale ordine (IVA incluse), applicando
        un importo minimo se il risultato calcolato è inferiore alla soglia configurata.

        Esempio con i valori di default (percentuale 4%, minimo 50):
        - Totale ordine 2000 -> 2000 * 4% = 80 -> costo spedizione = 80
        - Totale ordine 500  -> 500 * 4% = 20  -> costo spedizione = 50 (minimo)

        Funziona automaticamente su e-commerce, ordini di vendita e preventivi,
        poiché si integra con il meccanismo standard dei metodi di consegna (delivery.carrier).
    """,
    'author': 'EVM Srl',
    'depends': ['delivery', 'sale'],
    'data': [
        'views/delivery_carrier_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'LGPL-3',
}
