"""
Decision Engine

Combines activity classification, confidence estimation,
Solar Readiness Index (SRI), and operational recommendations
to generate the final assessment.
"""
from modules.sri import calculate_sri
from modules.forecast import generate_forecast
from modules.status import get_system_status
def make_decision(activity, soft_change, hard_change):

    # -----------------------------
    # Calculate Confidence
    # -----------------------------
    confidence = 50

    if soft_change > 0.5:
        confidence += 20

    if hard_change > 0.1:
        confidence += 20

    if activity == "PRE-FLARE":
        confidence += 10

    # -----------------------------
    # Confidence Level
    # -----------------------------
    if confidence >= 85:
        confidence_level = "High"
    elif confidence >= 70:
        confidence_level = "Moderate"
    else:
        confidence_level = "Low"

    # -----------------------------
    # Solar Readiness Index
    # -----------------------------
    sri = calculate_sri(
    soft_change,
    hard_change,
    activity
)

    # -----------------------------
    # Recommendation
    # -----------------------------
    if activity == "PRE-FLARE":
        recommendation = (
            "Increase monitoring frequency and prepare for elevated solar activity."
        )

    elif activity == "BUILD-UP":
        recommendation = (
            "Continue monitoring. Solar activity is increasing."
        )

    else:
        recommendation = (
            "Solar conditions remain stable."
        )

    # -----------------------------
    # Evidence
    # -----------------------------
    reasons = []

    if soft_change > 0:
        reasons.append("Soft X-ray trend is increasing.")

    if hard_change > 0:
        reasons.append("Hard X-ray trend is increasing.")

    if soft_change > 0.5:
        reasons.append("Rapid increase detected in Soft X-ray observations.")

    if hard_change > 0.1:
        reasons.append("Elevated Hard X-ray activity detected.")

    # -----------------------------
    # Return
    # -----------------------------
    forecast = generate_forecast(
    soft_change,
    hard_change,
    activity
)
    status = get_system_status(
    activity,
    sri,
    confidence
)
    return {
    "activity": activity,
    "confidence": confidence,
    "confidence_level": confidence_level,
    "sri": sri,
    "recommendation": recommendation,
    "reasons": reasons,
    "status": status,
    "forecast": forecast
}