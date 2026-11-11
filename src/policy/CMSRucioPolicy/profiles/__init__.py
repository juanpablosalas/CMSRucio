"""rse-decommissioner profiles for the CMS policy package.
"""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable

    from rucio.daemons.rsedecommissioner.profiles.types import DecommissioningProfile

ALGORITHM_TYPE = 'rse_decommisioner_profile_plugin'


def cms_decommissioner(rse: dict[str, Any], config: dict[str, Any]) -> 'DecommissioningProfile':
    from CMSRucioPolicy.profiles.cms import cms_decommissioner as _cms_decommissioner
    return _cms_decommissioner(rse, config)


def get_profiles() -> dict[str, 'Callable[[dict[str, Any], dict[str, Any]], DecommissioningProfile]']:
    """Return the decommissioning profiles, or {} if this Rucio can't load them.
    """
    from rucio.common.constants import POLICY_ALGORITHM_TYPES

    if ALGORITHM_TYPE not in POLICY_ALGORITHM_TYPES:
        return {}
    return {'cms_decommissioner': cms_decommissioner}
