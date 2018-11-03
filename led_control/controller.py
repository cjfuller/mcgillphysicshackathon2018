import abc
from typing import Tuple

class LEDController(metaclass=abc.ABCMeta):
    """Abstract interface for a device that controls some LEDs."""
    @abc.abstractmethod
    def can_handle(self, coord_xy: Tuple[int, int]) -> bool:
        """Does this controller handle the LED at coord_xy?"""
        pass

    @abc.abstractmethod
    def set_state(self, coord_xy: Tuple[int, int], on: bool) -> None:
        """Turn on or off the LED at coord_xy.

        This is a no-op if we don't know how to handle the given LED, but
        should not throw an exception.
        """
        pass
