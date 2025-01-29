"""
This file registers the model with the Python SDK.
"""

from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration

from .temt6000 import temt6000

Registry.register_resource_creator(Sensor.SUBTYPE, temt6000.MODEL, ResourceCreatorRegistration(temt6000.new, temt6000.validate))
