import plotly.express as px


def plot_soft_xray(data):
    """
    Creates an interactive Soft X-ray graph.
    """

    fig = px.line(
        data,
        x="Time",
        y="Soft_Xray",
        title="Soft X-ray Trend",
        markers=True
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Time",
        yaxis_title="Soft X-ray Flux",
        paper_bgcolor="#0F172A",
        plot_bgcolor="#0F172A",
        font=dict(color="white")
    )

    return fig


def plot_hard_xray(data):
    """
    Creates an interactive Hard X-ray graph.
    """

    fig = px.line(
        data,
        x="Time",
        y="Hard_Xray",
        title="Hard X-ray Trend",
        markers=True
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Time",
        yaxis_title="Hard X-ray Flux",
        paper_bgcolor="#0F172A",
        plot_bgcolor="#0F172A",
        font=dict(color="white")
    )

    return fig