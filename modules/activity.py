def detect_activity(
    data,
    soft_threshold=0.50,
    hard_threshold=0.10
):
    """
    Detect the current solar activity level based on
    changes in Soft X-ray and Hard X-ray observations.

    Returns:
        activity (str): PRE-FLARE, BUILD-UP, or QUIET
        soft_change (float)
        hard_change (float)
    """

    # -----------------------------
    # Verify required columns
    # -----------------------------
    required_columns = ["Soft_Xray", "Hard_Xray"]

    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    # -----------------------------
    # First and last observations
    # -----------------------------
    soft_start = data["Soft_Xray"].iloc[0]
    soft_end = data["Soft_Xray"].iloc[-1]

    hard_start = data["Hard_Xray"].iloc[0]
    hard_end = data["Hard_Xray"].iloc[-1]

    # -----------------------------
    # Calculate change
    # -----------------------------
    soft_change = soft_end - soft_start
    hard_change = hard_end - hard_start

    # -----------------------------
    # Activity Classification
    # -----------------------------
    if (
        soft_change >= soft_threshold
        and hard_change >= hard_threshold
    ):
        activity = "PRE-FLARE"

    elif soft_change >= (soft_threshold * 0.5):
        activity = "BUILD-UP"

    else:
        activity = "QUIET"

    # -----------------------------
    # Return results
    # -----------------------------
    return (
        activity,
        soft_change,
        hard_change
    )