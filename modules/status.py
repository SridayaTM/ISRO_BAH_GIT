"""
status.py

Mission Status Module

Determines the overall operational status of the
current solar observations.
"""


def get_system_status(activity, sri, confidence):
    """
    Generate overall mission status.

    Returns
    -------
    dict
    """

    if activity == "PRE-FLARE":

        level = "ALERT"

        icon = "🔴"

        description = (
            "Elevated solar activity detected. "
            "Enhanced monitoring is recommended."
        )

    elif activity == "BUILD-UP":

        level = "MONITOR"

        icon = "🟡"

        description = (
            "Solar activity is increasing. "
            "Continue observation."
        )

    else:

        level = "NORMAL"

        icon = "🟢"

        description = (
            "Solar conditions remain stable."
        )

    return {

        "icon": icon,

        "level": level,

        "description": description,

        "confidence": confidence,

        "sri": sri

    }