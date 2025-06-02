from typing import Iterable

from gemseo.core.discipline import Discipline
from gemseo.typing import StrKeyMapping


def update_default_inputs(disciplines: Iterable[Discipline], input_names_to_default_values: StrKeyMapping) -> None:
    """Update some default input values of a collection of disciplines.

    Args:
        disciplines: The disciplines.
        input_names_to_default_values: The map
            between the input names and default input values.
    """
    for discipline in disciplines:
        input_grammar = discipline.io.input_grammar
        defaults = input_grammar.defaults
        for input_name, input_value in input_names_to_default_values.items():
            if input_name in input_grammar:
                defaults[input_name] = input_value
