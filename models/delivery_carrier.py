from odoo import _, api, fields, models


class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    delivery_type = fields.Selection(
        selection_add=[('percentage_min', 'Percentuale con Minimo')],
        ondelete={'percentage_min': 'set default'},
    )
    percentage_rate = fields.Float(
        string='Percentuale (%)',
        default=0.04,
        help="Percentuale applicata sul totale dell'ordine (IVA incluse) per calcolare il costo di spedizione.",
    )
    minimum_amount = fields.Monetary(
        string='Importo Minimo',
        default=50.0,
        currency_field='currency_id',
        help="Se il costo calcolato in percentuale è inferiore a questo importo, viene applicato questo importo minimo.",
    )

    def percentage_min_rate_shipment(self, order):
        self.ensure_one()
        if not self._match_address(order.partner_shipping_id):
            return {
                'success': False,
                'price': 0.0,
                'error_message': _('Errore: questo metodo di spedizione non è disponibile per questo indirizzo.'),
                'warning_message': False,
            }

        order_total = order._compute_amount_total_without_delivery()
        order_total = self._compute_currency(order, order_total, 'pricelist_to_company')

        price = order_total * self.percentage_rate
        if price < self.minimum_amount:
            price = self.minimum_amount

        price = self._compute_currency(order, price, 'company_to_pricelist')

        return {
            'success': True,
            'price': price,
            'error_message': False,
            'warning_message': False,
        }

    @api.onchange('delivery_type')
    def _onchange_delivery_type_percentage_min(self):
        if self.delivery_type == 'percentage_min':
            self.invoice_policy = 'estimated'
