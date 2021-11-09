# This file is part of the payment_collect_afip module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import Pool, PoolMeta

__all__ = ['Configuration', 'ConfigurationPaymentCollectAccount']

class Configuration(metaclass=PoolMeta):
    __name__ = 'payment_collect.configuration'
    pos = fields.MultiValue(fields.Many2One('account.pos', "Point of Sale",
            domain=[('pos_daily_report', '=', False)]))

    @classmethod
    def multivalue_model(cls, field):
        pool = Pool()
        if field == 'pos':
            return pool.get('payment_collect.configuration.account')
        return super().multivalue_model(field)

    @classmethod
    def default_pos(cls, **pattern):
        return cls.multivalue_model(
            'pos').default_pos()


class ConfigurationPaymentCollectAccount(metaclass=PoolMeta):
    __name__ = 'payment_collect.configuration.account'
    pos = fields.Many2One('account.pos', "Point of Sale",
        domain=[('pos_daily_report', '=', False)])

    @staticmethod
    def default_pos():
        return None
