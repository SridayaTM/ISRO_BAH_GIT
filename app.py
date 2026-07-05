import streamlit as st
import pandas as pd

from modules.activity import detect_activity
from modules.decision_engine import make_decision
from modules.plots import plot_soft_xray, plot_hard_xray
from modules.validation import validate_dataset


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Solar Operations Console",
    page_icon="☀️",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.stApp{
    background:#0F172A;
}

.block-container{
    max-width:1300px;
    padding-top:2rem;
    padding-bottom:2rem;
}

h1,h2,h3{
    color:#F8FAFC;
}

hr{
    border:0;
    border-top:1px solid #334155;
}

.card{
    background:#1E293B;
    border:1px solid #334155;
    border-radius:12px;
    padding:20px;
    margin-bottom:15px;
}

.metric-title{
    color:#94A3B8;
    font-size:14px;
    text-transform:uppercase;
    letter-spacing:1px;
}

.metric-value{
    color:white;
    font-size:32px;
    font-weight:bold;
    margin-top:8px;
}

.metric-desc{
    color:#94A3B8;
    font-size:13px;
    margin-top:10px;
}

.info-box{
    background:#111827;
    border-left:4px solid #38BDF8;
    padding:18px;
    border-radius:8px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

left, right = st.columns([5, 1])

with left:
    st.title("Solar Operations Console")
    st.caption("Physics-Aware Solar Flare Decision Support Prototype")

with right:
    st.markdown("""
**Observation Status**

 Dataset Loaded
""")

st.markdown("---")

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

st.header("Load Observation Dataset")

st.write(
    "Upload a CSV containing synchronized "
    "SoLEXS and HEL1OS observations."
)

uploaded_file = st.file_uploader(
    "Observation Dataset",
    type="csv"
)

run = False

if uploaded_file:

    data = pd.read_csv(uploaded_file)
    validation = validate_dataset(data)
    st.success("Dataset loaded successfully.")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Records", len(data))

    with c2:
        st.metric("Columns", len(data.columns))

    with c3:
        st.metric(
            "Observation Period",
            f"{data['Time'].iloc[0]} - {data['Time'].iloc[-1]}"
        )

    st.markdown("---")
    # --------------------------------------------------
    # DATASET VALIDATION
    # --------------------------------------------------

    st.header("Dataset Validation")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Validation Status", validation["status"])

    with col2:
        st.metric(
            "Validation Score",
            validation["validation_score"]
        )

    for message in validation["messages"]:
        st.write(f"✓ {message}")

    st.markdown("---")

    
    st.header("Analysis Parameters")

    soft_threshold = st.number_input(
        "Soft X-ray Threshold",
        value=0.50,
        step=0.05
    )

    hard_threshold = st.number_input(
        "Hard X-ray Threshold",
        value=0.10,
        step=0.01
    )

    run = st.button(
        "Run Assessment",
        use_container_width=True,
        type="primary"
    )

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if uploaded_file and run:

    activity, soft_change, hard_change = detect_activity(
        data,
        soft_threshold,
        hard_threshold
    )

    decision = make_decision(
        activity,
        soft_change,
        hard_change
    )

    st.markdown("---")
    st.header("Operational Assessment")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
            <div class="metric-title">Current Activity</div>
            <div class="metric-value">{decision["activity"]}</div>
            <div class="metric-desc">
                Current operational classification of solar activity.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <div class="metric-title">Assessment Confidence</div>
            <div class="metric-value">{decision["confidence"]}%</div>
            <div class="metric-desc">
                Confidence Level: {decision["confidence_level"]}
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
            <div class="metric-title">Solar Readiness Index</div>
            <div class="metric-value">{decision["sri"]}</div>
            <div class="metric-desc">
                Overall operational readiness indicator.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # --------------------------------------------------
    # INTEGRATED OBSERVATION ASSESSMENT
    # --------------------------------------------------

    st.header("Integrated Observation Assessment")

    assessment = pd.DataFrame({
        "Parameter": [
            "Thermal Observation",
            "Non-Thermal Observation",
            "Soft X-ray Change",
            "Hard X-ray Change",
            "Overall Assessment"
        ],
        "Result": [
            "Increasing" if soft_change > 0 else "Stable",
            "Increasing" if hard_change > 0 else "Stable",
            f"{soft_change:.2f}",
            f"{hard_change:.2f}",
            decision["activity"]
        ]
    })

    st.dataframe(
        assessment,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # --------------------------------------------------
    # MISSION ADVISORY
    # --------------------------------------------------

    st.header("Mission Advisory")

    st.markdown(f"""
    <div class="info-box">

    <b>Operational Recommendation</b>

    <br><br>

    {decision["recommendation"]}

    <br><br>

    <b>Assessment Basis</b>

    <ul>
    {''.join([f'<li>{r}</li>' for r in decision["reasons"]])}
    </ul>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # --------------------------------------------------
    # OPERATIONAL OUTLOOK
    # --------------------------------------------------

    st.header("Operational Outlook")

    forecast = decision["forecast"]

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Expected Trend", forecast["trend"])

    with c2:
        st.metric("Likelihood", f'{forecast["probability"]}%')

    with c3:
        st.metric("Risk Level", forecast["risk_level"])

    st.info(f"""
**Forecast Window:** {forecast["forecast_window"]}

{forecast["outlook"]}

**Forecast Confidence:** {forecast["confidence"]}%
""")

    st.markdown("---")

    # --------------------------------------------------
    # OBSERVATION TRENDS
    # --------------------------------------------------

    st.header("Observation Trends")

    st.subheader("Thermal Observation (SoLEXS)")
    soft_fig = plot_soft_xray(data)

    st.plotly_chart(
        soft_fig,
        use_container_width=True
    )

    st.subheader("Non-Thermal Observation (HEL1OS)")
    hard_fig = plot_hard_xray(data)

    st.plotly_chart(
        hard_fig,
        use_container_width=True
    )

    st.markdown("---")

    # --------------------------------------------------
    # OBSERVATION DATASET
    # --------------------------------------------------

    st.header("Observation Dataset")

    with st.expander("View Observation Data", expanded=False):
        st.dataframe(
            data,
            use_container_width=True
        )

else:
    st.info("""
    ### Welcome

    This prototype demonstrates a **Physics-Aware Solar Flare Decision Support System**.

    #### Workflow

    1. Upload a synchronized SoLEXS + HEL1OS observation dataset.
    2. Configure analysis parameters.
    3. Run the operational assessment.
    4. Review the recommendation and supporting evidence.
    5. Explore the observation trends.

    Upload a CSV file above to begin.
    """)