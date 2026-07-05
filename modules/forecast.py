"""
forecast.py

Operational Outlook Module

This module generates a short-term operational outlook
using recent thermal (SoLEXS) and non-thermal (HEL1OS)
solar observations.

The objective is not long-term flare prediction.
Instead, it provides an explainable estimate of the
expected solar activity trend during the next
observation interval to assist operational decision making.
"""


def generate_forecast(
    soft_change,
    hard_change,
    activity
):
    """
    Generate a short-term operational outlook.

    Parameters
    ----------
    soft_change : float
        Change in Soft X-ray observations.

    hard_change : float
        Change in Hard X-ray observations.

    activity : str
        Current activity classification.

    Returns
    -------
    dict
        Operational outlook information.
    """

    # -------------------------------------------------
    # Base Probability
    # -------------------------------------------------

    probability = 50

    if soft_change > 0:
        probability += 10

    if soft_change >= 0.50:
        probability += 10

    if hard_change > 0:
        probability += 10

    if hard_change >= 0.10:
        probability += 10

    if activity == "PRE-FLARE":
        probability += 10

    elif activity == "BUILD-UP":
        probability += 5

    probability = min(probability, 95)

    # -------------------------------------------------
    # Forecast Trend
    # -------------------------------------------------

    if activity == "PRE-FLARE":

        trend = "Increasing"

        risk_level = "High"

        outlook = (
            "Thermal and non-thermal observations indicate "
            "continued strengthening of solar activity during "
            "the next observation interval. Enhanced operational "
            "monitoring is recommended."
        )

    elif activity == "BUILD-UP":

        trend = "Moderately Increasing"

        risk_level = "Moderate"

        outlook = (
            "Current observations indicate a gradual increase "
            "in solar activity. Continued monitoring is advised "
            "to detect further escalation."
        )

    else:

        trend = "Stable"

        risk_level = "Low"

        outlook = (
            "Current observations suggest relatively stable "
            "solar conditions with no immediate indication "
            "of significant escalation."
        )

    # -------------------------------------------------
    # Forecast Confidence
    # -------------------------------------------------

    confidence = 60

    if soft_change >= 0.50:
        confidence += 20

    if hard_change >= 0.10:
        confidence += 20

    confidence = min(confidence, 100)

    # -------------------------------------------------
    # Forecast Window
    # -------------------------------------------------

    forecast_window = "Next Observation Interval"

    # -------------------------------------------------
    # Return Results
    # -------------------------------------------------

    return {

        "trend": trend,

        "probability": probability,

        "confidence": confidence,

        "risk_level": risk_level,

        "forecast_window": forecast_window,

        "outlook": outlook

    }