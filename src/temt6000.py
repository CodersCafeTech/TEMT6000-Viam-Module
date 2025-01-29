from typing import ClassVar, Mapping, Sequence, Any, Dict, Optional, Tuple, Final, List, cast
from typing_extensions import Self

from typing import Any, Final, Mapping, Optional


from viam.utils import SensorReading

from viam.module.types import Reconfigurable
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName, Vector3
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily

from viam.components.sensor import Sensor
from viam.logging import getLogger

import Adafruit_ADS1x15

import time
import asyncio

LOGGER = getLogger(__name__)

class temt6000(Sensor, Reconfigurable):
    """
    TEMT6000 represents a light sensor that can calculate light intensity
    (percentage) and illuminance (lux) based on analog input values from ADS1115.
    """
    MODEL: ClassVar[Model] = Model(ModelFamily("coderscafe", "sensor"), "temt6000")

    def __init__(self, name: str):
        super().__init__(name)
        self.ads1115 = Adafruit_ADS1x15.ADS1115(address=0x48, busnum=1)  # Initialize the ADS1115 ADC
        self.channel = None  # The channel parameter for the ADC
        LOGGER.info(f"{self.__class__.__name__} initialized.")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]) -> Self:
        instance = cls(config.name)
        instance.reconfigure(config, dependencies)
        return instance

    @classmethod
    def validate(cls, config: ComponentConfig):
        # Ensure 'channel' is in the configuration
        if "channel" not in config.attributes.fields:
            raise Exception("'channel' must be defined in the configuration.")
        return

    def reconfigure(self, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        # Get the channel from the configuration
        self.channel = int(config.attributes.fields["channel"].number_value)
        LOGGER.info(f"TEMT6000 reconfigured with ADS1115 channel: {self.channel}")

    async def get_readings(
        self, *, extra: Optional[Mapping[str, Any]] = None, timeout: Optional[float] = None, **kwargs
    ) -> Mapping[str, Any]:
        """
        Calculate readings based on the analog value read from the ADS1115.

        Args:
            No arguments needed since we read directly from the ADC.

        Returns:
            Mapping[str, Any]: A mapping of calculated readings (light intensity and illuminance).
        """
        # Read the analog value from the specified channel (assuming 16-bit ADC)
        analog_value = self.ads1115.read_adc(self.channel, gain=1)
        LOGGER.debug(f"Raw ADC value from channel {self.channel}: {analog_value}")

        # Calculate light intensity as a percentage (scale to 0-1023 range)
        light_intensity = analog_value * 0.00305

        # Calculate illuminance in lux
        volts = analog_value * 5.0 / 32767.0  # ADS1115 provides 16-bit range (-32768 to 32767)
        amps = volts / 10000.0  # Assuming a 10,000-ohm resistor
        microamps = amps * 1e6
        lux = microamps * 2.0

        # Log the calculated values
        LOGGER.info(f"Analog Value: {analog_value}, Light Intensity: {light_intensity:.2f}%, Illuminance: {lux:.2f} lux")

        # Return the readings
        return {
            "light_intensity": light_intensity,
            "illuminance": lux,
        }
