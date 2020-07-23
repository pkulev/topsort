"""Unit tests for pytopsort module."""

import pytest

from pytopsort import topsort


def test_topsort():
    """This recipe contains no cycles and can be sorted."""

    # fmt: off
    recipe = [{
        "action": "spread peanut butter on bread",
        "after": ["slice bread"],
    }, {
        "action": "slice bread",
        "after": [],
    }, {
        "action": "eat the delicious breakfast!",
        "after": ["spread jam on top", "make a cup of coffee"],
    }, {
        "action": "make a cup of coffee",
        "after": [],
    }, {
        "action": "spread jam on top",
        "after": ["spread peanut butter on bread"],
    }]
    # fmt: on

    recipe = topsort(
        recipe, deptest=lambda self, other: self["action"] in other["after"],
    )

    # fmt: off
    assert list(recipe) == [{
        "action": "make a cup of coffee",
        "after": [],
    }, {
        "action": "slice bread",
        "after": [],
    }, {
        "action": "spread peanut butter on bread",
        "after": ["slice bread"],
    }, {
        "action": "spread jam on top",
        "after": ["spread peanut butter on bread"],
    }, {
        "action": "eat the delicious breakfast!",
        "after": ["spread jam on top", "make a cup of coffee"],
    }]
    # fmt: on


def test_cycles():
    """This recipe contains a cycle (two actions depend on each other)."""

    # fmt: off
    recipe = [{
        "action": "spread peanut butter on bread",
        "after": ["slice bread"],
    }, {
        "action": "slice bread",
        "after": ["spread peanut butter on bread"],
    }, {
        "action": "eat the delicious breakfast!",
        "after": ["spread jam on top", "make a cup of coffee"],
    }, {
        "action": "make a cup of coffee",
        "after": [],
    }, {
        "action": "spread jam on top",
        "after": ["spread peanut butter on bread"],
    }]
    # fmt: on

    with pytest.raises(ValueError) as exc:
        recipe = topsort(
            recipe, deptest=lambda self, other: self["action"] in other["after"],
        )

    assert str(exc.value) == "Dependency graph has a cycle"
