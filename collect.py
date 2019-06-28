# This file is part of the payment_collect_afip module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta, Pool
from trytond.pyson import Eval

__all__ = ['Collect']


class Collect(metaclass=PoolMeta):
    __name__ = 'payment.collect'

    pos = fields.Many2One('account.pos', 'Point of Sale',
        domain=[('pos_daily_report', '=', False)],
        states={
            'readonly': Eval('state') != 'processing',
            'invisible': Eval('type') == 'send',
        },
        depends=['state'])
    invoice_type = fields.Many2One('account.pos.sequence', 'Comprobante',
        states={
            'readonly': Eval('state') != 'processing',
            'invisible': Eval('type') == 'send',
        },
        domain=[('pos', '=', Eval('pos'))], depends=['pos'])

    @classmethod
    def __setup__(cls):
        super(Collect, cls).__setup__()
        cls._buttons['create_invoices'].update({
                'pre_validate':
                ['AND',
                    ('invoice_type', '!=', None),
                    ('pos', '!=', None),
                    ],
                })

    @staticmethod
    def default_pos():
        Configuration = Pool().get('payment_collect.configuration')
        config = Configuration(1)
        if config.pos:
            return config.pos.id
        return None
