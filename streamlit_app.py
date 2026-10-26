
import streamlit as st
import pandas as pd
# ==================================
# 1. APP CONFIGURATION
# ==================================
st.set_page_config(
    page_title="ProjectFlow",
    page_icon="📊",
    layout="wide"
)
# ==================================
# 2. SAMPLE DATA (ข้อมูลสมมติ)
# ==================================

projects = pd.DataFrame([
    {
        "Project": "CCT Data Migration",
        "Milestones": 4,
        "Progress": 55,
        "Requested": 300000,
        "Approved": 280000,
        "Actual": 65000,
        "Status": "In Progress"
    },
    {
        "Project": "MFA / ThaID",
        "Milestones": 3,
        "Progress": 30,
        "Requested": 150000,
        "Approved": 120000,
        "Actual": 35000,
        "Status": "In Progress"
    },
    {
        "Project": "HERO OBEC CARE",
        "Milestones": 5,
        "Progress": 70,
        "Requested": 200000,
        "Approved": 190000,
        "Actual": 45000,
        "Status": "In Progress"
    }
])

# ==================================
# 3. SIDEBAR NAVIGATION
# ==================================

with st.sidebar:
    st.title("📊 ProjectFlow")
    st.caption("Project Monitoring System")

    page = st.radio(
        "Navigation",
        [
            "Dashboard",
            "Projects",
            "Activities",
            "Budget",
            "Monthly Reports"
        ]
    )

    st.divider()
    st.caption("Prototype v0.1")
    st.info("Demo data only")

# ==================================
# 4. DASHBOARD
# ==================================

if page == "Dashboard":

    st.title("Overview Dashboard")
    st.caption(
        "Project planning, monitoring and budget tracking"
    )

    total_projects = len(projects)
    total_requested = projects["Requested"].sum()
    total_approved = projects["Approved"].sum()
    total_actual = projects["Actual"].sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Projects", total_projects)
    col2.metric("Requested", f"฿{total_requested:,.0f}")
    col3.metric("Approved", f"฿{total_approved:,.0f}")
    col4.metric("Actual Spent", f"฿{total_actual:,.0f}")

    st.divider()

    st.subheader("Project Overview")

    st.dataframe(
        projects,
        hide_index=True,
        use_container_width=True
    )

    st.subheader("Project Progress")

    for _, project in projects.iterrows():

        st.write(
            f"{project['Project']} — {project['Progress']}%"
        )

        st.progress(project["Progress"] / 100)

    st.divider()

    st.subheader("Budget Comparison")

    budget_chart = projects.set_index("Project")[
        ["Requested", "Approved", "Actual"]
    ]

    st.bar_chart(budget_chart)

# ==================================
# 5. PROJECTS
# ==================================

elif page == "Projects":

    st.title("Projects")
    st.write("จัดการข้อมูลโครงการและ Milestones")

    st.dataframe(
        projects[["Project", "Milestones", "Progress", "Status"]],
        hide_index=True,
        use_container_width=True
    )

    st.info("Coming next: Add / Edit Projects")

# ==================================
# 6. ACTIVITIES
# ==================================

elif page == "Activities":

    st.title("Activity Monitoring")
    st.write("ติดตามกิจกรรมและบันทึกผลการดำเนินงาน")

    st.info("Coming next: Activity Update Form")

# ==================================
# 7. BUDGET
# ==================================

elif page == "Budget":

    st.title("Budget Tracking")
    st.write("ติดตามงบที่ขอ งบอนุมัติ และค่าใช้จ่ายจริง")

    budget_data = projects[
        ["Project", "Requested", "Approved", "Actual"]
    ].copy()

    budget_data["Remaining"] = (
        budget_data["Approved"] - budget_data["Actual"]
    )

    st.dataframe(
        budget_data,
        hide_index=True,
        use_container_width=True
    )

# ==================================
# 8. MONTHLY REPORTS
# ==================================

elif page == "Monthly Reports":

    st.title("Monthly Progress Reports")
    st.write("สรุปผลการดำเนินงานรายเดือน")

    st.info("Coming next: Monthly Report Builder")
