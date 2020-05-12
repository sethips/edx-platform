"""
This module contains various configuration settings via
waffle switches for the course_details view.
"""


from openedx.core.djangoapps.waffle_utils import WaffleFlagNamespace, WaffleSwitchNamespace

WAFFLE_NAMESPACE = u'course_detail'
COURSE_DETAIL_WAFFLE_FLAG_NAMESPACE = WaffleFlagNamespace(name=WAFFLE_NAMESPACE)
WAFFLE_SWITCHES = WaffleSwitchNamespace(name=WAFFLE_NAMESPACE)

# Waffle switches
COURSE_DETAIL_UPDATE_CERTIFICATE_DATE = u'course_detail_update_certificate_date'


def course_detail_update_certificate_date():
    """
    Returns True if course_detail_update_certificate_date switch is enabled, otherwise False.
    """
    return WAFFLE_SWITCHES.is_enabled(COURSE_DETAIL_UPDATE_CERTIFICATE_DATE)
