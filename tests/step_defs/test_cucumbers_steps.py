# coding=utf-8
"""Cucumber Basket feature tests."""

from pytest_bdd import (
    given,
    parsers,
    scenario,
    then,
    when,
)

from cucumbers import CucumberBasket


@scenario("../features/cucumbers.feature", "Add cucumbers to a basket")
def test_add_cucumbers_to_a_basket():
    """Add cucumbers to a basket."""


@scenario("../features/cucumbers.feature", "Remove cucumbers from a basket")
def test_remove_cucumbers_from_a_basket():
    """Remove cucumbers from a basket."""


@given(
    parsers.cfparse(
        'the basket has "{initial:Number}" cucumbers', extra_types=dict(Number=int)
    )
)
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(
    parsers.cfparse(
        '"{some:Number}" cucumbers are added to the basket',
        extra_types=dict(Number=int),
    )
)
def add_cucumbers(basket, some):
    basket.add(some)


@when(
    parsers.cfparse(
        '"{some:Number}" cucumbers are removed from the basket',
        extra_types=dict(Number=int),
    )
)
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(
    parsers.cfparse(
        'the basket contains "{total:Number}" cucumbers', extra_types=dict(Number=int)
    )
)
def basket_has_total(basket, total):
    assert basket.count == total
