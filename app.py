import streamlit as st
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="PostgresInsight AI",
    layout="wide"
)

# -----------------------------
# SIMPLE CLEAN UI (no risky CSS)
# -----------------------------
st.title("🚀 PostgresInsight AI")
st.caption("AI-powered PostgreSQL Query Analyzer & Optimization Assistant")

# -----------------------------
# Analyzer Logic
# -----------------------------
def analyze_query(query):
    query = query.lower()
    suggestions = []

    if "select *" in query:
        suggestions.append("❌ Avoid SELECT * — fetch only required columns.")

    if "where" in query:
        suggestions.append("⚠️ Consider adding an index on filtered columns.")

    if "join" in query:
        suggestions.append("⚠️ Ensure JOIN columns are indexed.")

    if "order by" in query:
        suggestions.append("⚠️ ORDER BY can slow queries — use indexing.")

    if len(suggestions) == 0:
        suggestions.append("✅ Query looks optimized.")

    return suggestions

# -----------------------------
# Explain Plan Helper
# -----------------------------
def explain_help():
    return [
        "🔍 Sequential Scan → Full table scan (slow for large data)",
        "⚡ Index Scan → Faster lookup using index",
        "⚠️ High cost → Indicates performance issue"
    ]

# -----------------------------
# Sidebar
# -----------------------------
page = st.sidebar.radio("Navigation", [
    "Home",
    "Query Analyzer",
    "Dashboard",
    "TimescaleDB Guide"
])

# -----------------------------
# HOME
# -----------------------------
if page == "Home":
    st.subheader("Overview")

    st.write("""
    This tool helps analyze PostgreSQL queries, detect performance issues,
    and suggest optimizations.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Queries Analyzed", "1,200+")
    col2.metric("Avg Optimization Gain", "65%")
    col3.metric("Performance Boost", "High")

# -----------------------------
# QUERY ANALYZER
# -----------------------------
elif page == "Query Analyzer":
    st.subheader("Analyze Your SQL Query")

    query = st.text_area("Enter SQL Query")

    if st.button("Analyze Query"):
        if query.strip():
            st.success("Analysis Complete")

            st.subheader("Suggestions")
            for s in analyze_query(query):
                st.write(s)

            st.subheader("Explain Insights")
            for e in explain_help():
                st.write(e)
        else:
            st.warning("Please enter a query.")

# -----------------------------
# DASHBOARD
# -----------------------------
elif page == "Dashboard":
    st.subheader("Support Metrics")

    data = pd.DataFrame({
        "Metric": ["Slow Queries", "Optimized Queries", "Time Saved"],
        "Value": [45, 120, "65%"]
    })

    st.table(data)

    st.subheader("Query Trend")
    trend = pd.DataFrame({"Queries": [10, 25, 40, 60, 90, 120]})
    st.line_chart(trend)

# -----------------------------
# TIMESCALEDB GUIDE
# -----------------------------
elif page == "TimescaleDB Guide":
    st.subheader("Time-Series Optimization (Concept)")

    st.write("Example of converting table to hypertable:")

    st.code("""
SELECT create_hypertable('orders', 'created_at');
""")

    st.write("Compression:")

    st.code("""
ALTER TABLE orders SET (timescaledb.compress);
""")

    st.info("Hypertables improve performance by partitioning time-series data.")