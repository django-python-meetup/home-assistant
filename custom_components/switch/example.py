import os
from homeassistant.helpers.entity import ToggleEntity


def setup_platform(hass, config, add_device, discover_info=None):
    """Setup the switch platform."""
    add_device([FileSwitch(config['file_path']), ])


class FileSwitch(ToggleEntity):
    """Representation of a Switch."""

    def __init__(self, path):
        self.path = path
        self.update()

    @property
    def name(self):
        """Return the name of the switch."""
        return os.path.basename(self.path)

    @property
    def is_on(self):
        return self._state

    def turn_on(self, **kwargs):
        open(self.path, 'a').close()

    def turn_off(self, **kwargs):
        os.remove(self.path)

    def update(self):
        """
        Fetch new state data for the switch.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = os.path.isfile(self.path)
