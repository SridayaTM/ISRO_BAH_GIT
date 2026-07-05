"""
Solar Readiness Index (SRI)

The Solar Readiness Index provides a simple operational indicator
(0–100) representing the current level of preparedness required
based on complementary thermal and non-thermal solar observations.
"""


def calculate_sri(
    soft_change,
    hard_change,
    activity
):
    """
    Calculate Solar Readiness Index.

    Parameters
    ----------
    soft_change : float
        Change in Soft X-ray observations.

    hard_change : float
        Change in Hard X-ray observations.

    activity : str
        Current solar activity classification.

    Returns
    -------
    int
        Solar Readiness Index (0–100)
    """

    # Base readiness
    sri = 40

    # -----------------------------
    # Thermal Contribution
    # -----------------------------
    if soft_change > 0:
        sri += 15

    if soft_change >= 0.50:
        sri += 20

    # -----------------------------
    # Non-Thermal Contribution
    # -----------------------------
    if hard_change > 0:
        sri += 10

    if hard_change >= 0.10:
        sri += 10

    # -----------------------------
    # Activity Contribution
    # -----------------------------
    if activity == "PRE-FLARE":
        sri += 5

    elif activity == "BUILD-UP":
        sri += 3

    # Keep within operational range
    sri = max(0, min(sri, 100))

    return sri