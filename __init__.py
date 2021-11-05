"""The seeed4relay component."""
import logging
from homeassistant.const import EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
import threading
from . import relay_lib_seeed

DOMAIN = "seeed4relay"

#CONF_I2S_ADRESS = "address"
#CONF_I2S_BUS = "bus"

#CONFIG_SCHEMA = vol.Schema(
	#{
		#DOMAIN: vol.Schema({
			#vol.Required(CONF_I2S_BUS, default=1): cv.positive_int,
			#vol.Optional(CONF_I2S_ADRESS, default=21): cv.positive_int,
		#})
	#},

def setup(hass, config):

    board = relay_lib_seeed
    hass.data[DOMAIN] = board

    return True
