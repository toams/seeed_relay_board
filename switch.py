"""Support for Seeed 4 relay hat."""
import voluptuous as vol
import logging

from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity
from homeassistant.const import CONF_NAME, CONF_SWITCHES
import homeassistant.helpers.config_validation as cv
from . import DOMAIN
from . import relay_lib_seeed

_LOGGER = logging.getLogger(__name__)

CONF_PORTS = "ports"

_SWITCHES_SCHEMA = vol.Schema({cv.positive_int: cv.string})

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_PORTS): _SWITCHES_SCHEMA,
        #vol.Optional(CONF_INVERT_LOGIC, default=DEFAULT_INVERT_LOGIC): cv.boolean,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    port = hass.data[DOMAIN]

    switches =  []
    ports = config.get(CONF_PORTS)
    for port, name in ports.items():
        switches.append(seeed_relay_boardSwitch(name, port))
    add_entities(switches)


class seeed_relay_boardSwitch(SwitchEntity):

    def __init__(self, name, port):
        self._name = name
        self._state = False
        self._port = port
        #self._state = options[CONF_INITIAL]

    @property
    def name(self):
        return self._name

    @property
    def is_on(self):
        return self._state


    def turn_on(self, **kwargs):
        relay_lib_seeed.relay_on(self._port)
        self._state = True

    def turn_off(self, **kwargs):
        relay_lib_seeed.relay_off(self._port)
        self._state = False
