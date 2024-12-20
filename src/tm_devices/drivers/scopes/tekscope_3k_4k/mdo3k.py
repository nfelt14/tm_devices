"""MDO3K device driver module."""

from tm_devices.commands import MDO3KMixin
from tm_devices.drivers.scopes.tekscope_3k_4k.tekscope_3k_4k import TekScope3k4k


class MDO3K(MDO3KMixin, TekScope3k4k):
    """MDO3K device driver."""

    ################################################################################################
    # Magic Methods
    ################################################################################################

    ################################################################################################
    # Properties
    ################################################################################################

    ################################################################################################
    # Public Methods
    ################################################################################################

    ################################################################################################
    # Private Methods
    ################################################################################################
