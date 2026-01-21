"""Primitivas de configuración del Command Center.

Command center configuration primitives for Command Center.
"""

from .master_switch import MasterSwitch
from .endpoints import Endpoint, EndpointRegistry
from .rules_config import RuleConfig, RuleRegistry
from .settings import CommandCenterSettings

__all__ = [
    "CommandCenterSettings",
    "Endpoint",
    "EndpointRegistry",
    "MasterSwitch",
    "RuleConfig",
    "RuleRegistry",
]
