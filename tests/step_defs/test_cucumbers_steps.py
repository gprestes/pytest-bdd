# coding=utf-8
"""Cucumber Basket feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

from cucumbers import CucumberBasket


@scenario("../features/cucumbers.feature", "Add cucumbers to a basket")
def test_add_cucumbers_to_a_basket():
    """Add cucumbers to a basket."""
    pass


@given("the basket has 2 cucumbers")
def basket():
    """the basket has 2 cucumbers."""
    return CucumberBasket(initial_count=2)


@when("4 cucumbers are added to the basket")
def add_cucumbers(basket):
    """4 cucumbers are added to the basket."""
    basket.add(4)


@then("the basket contains 6 cucumbers")
def basket_has_total(basket):
    """the basket contains 6 cucumbers."""
    assert basket.count == 6

