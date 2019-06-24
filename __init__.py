# This file is part of the payment_collect_afip module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import collect
from . import configuration


def register():
    Pool.register(
        collect.Collect,
        configuration.Configuration,
        configuration.ConfigurationPaymentCollectAccount,
        module='payment_collect', type_='model')
