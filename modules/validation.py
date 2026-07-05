"""
validation.py

Observation Dataset Validation Module

Performs structural and quality checks on uploaded
SoLEXS and HEL1OS observation datasets before analysis.
"""


def validate_dataset(data):
    """
    Validate uploaded observation dataset.

    Parameters
    ----------
    data : pandas.DataFrame

    Returns
    -------
    dict
        Validation report
    """

    report = {}

    # -------------------------------------------------
    # Required Columns
    # -------------------------------------------------

    required_columns = [
        "Time",
        "Soft_Xray",
        "Hard_Xray"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in data.columns
    ]

    report["missing_columns"] = missing_columns

    # -------------------------------------------------
    # Dataset Size
    # -------------------------------------------------

    report["records"] = len(data)
    report["columns"] = len(data.columns)

    # -------------------------------------------------
    # Missing Values
    # -------------------------------------------------

    report["missing_values"] = int(
        data.isnull().sum().sum()
    )

    # -------------------------------------------------
    # Duplicate Time Stamps
    # -------------------------------------------------

    if "Time" in data.columns:

        report["duplicate_timestamps"] = int(
            data["Time"].duplicated().sum()
        )

    else:

        report["duplicate_timestamps"] = 0

    # -------------------------------------------------
    # Negative Flux Check
    # -------------------------------------------------

    negative_flux = 0

    if "Soft_Xray" in data.columns:

        negative_flux += int(
            (data["Soft_Xray"] < 0).sum()
        )

    if "Hard_Xray" in data.columns:

        negative_flux += int(
            (data["Hard_Xray"] < 0).sum()
        )

    report["negative_flux"] = negative_flux

    # -------------------------------------------------
    # Observation Window
    # -------------------------------------------------

    if (
        "Time" in data.columns
        and len(data) > 0
    ):

        report["start_time"] = data["Time"].iloc[0]
        report["end_time"] = data["Time"].iloc[-1]

    else:

        report["start_time"] = "-"
        report["end_time"] = "-"

    # -------------------------------------------------
    # Validation Score
    # -------------------------------------------------

    score = 100

    score -= len(missing_columns) * 20

    score -= report["missing_values"] * 5

    score -= report["duplicate_timestamps"] * 5

    score -= report["negative_flux"] * 10

    score = max(score, 0)

    report["validation_score"] = score

    # -------------------------------------------------
    # Validation Status
    # -------------------------------------------------

    if score >= 90:

        status = "VALID"

    elif score >= 70:

        status = "VALID WITH WARNINGS"

    else:

        status = "INVALID"

    report["status"] = status

    # -------------------------------------------------
    # Messages
    # -------------------------------------------------

    messages = []

    if not missing_columns:
        messages.append("Required columns verified.")

    else:
        messages.append(
            "Missing columns: "
            + ", ".join(missing_columns)
        )

    if report["missing_values"] == 0:
        messages.append("No missing values detected.")
    else:
        messages.append(
            f'{report["missing_values"]} missing value(s) detected.'
        )

    if report["duplicate_timestamps"] == 0:
        messages.append("No duplicate timestamps detected.")
    else:
        messages.append(
            f'{report["duplicate_timestamps"]} duplicate timestamp(s) detected.'
        )

    if report["negative_flux"] == 0:
        messages.append("Observation values are physically valid.")
    else:
        messages.append(
            f'{report["negative_flux"]} negative flux value(s) detected.'
        )

    report["messages"] = messages

    return report