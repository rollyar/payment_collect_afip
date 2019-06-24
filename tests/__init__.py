# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.payment_colllect_afip.tests.test_payment_collect_afip import suite
except ImportError:
    from .test_payment_collect_afip import suite

__all__ = ['suite']
