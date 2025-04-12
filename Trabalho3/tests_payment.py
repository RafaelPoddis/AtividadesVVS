"""
Trabalho 3 feito em grupo por:
João Paulo Paixão Rocha          RA 156408
Rafael Poddis
Thiago Cortez Cursino dos Santos RA 163997
"""

from process_payment import process_payment as pp
from process_payment import InvalidPaymentDetails, PaymentGatewayError
import pytest
from unittest.mock import patch

def foo():
    return 0.2

@patch("random.random", foo)
def test_should_have_conection():
    with pytest.raises(PaymentGatewayError):
        payment = pp('1234', 1)

def test_pass():
    payment = pp('1234', 80)
    assert payment

def test_should_have_user_id():
    with pytest.raises(InvalidPaymentDetails):
        payment = pp(None, 80)


def test_should_have_amount():
    with pytest.raises(InvalidPaymentDetails):
        payment = pp('1234', -5)


def test_should_have_known_currency():
    with pytest.raises(InvalidPaymentDetails):
        payment = pp('1234', 80, "BRL")
