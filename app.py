import streamlit as st
import pandas as pd

st.set_page_config(page_title="Employee Dashboard", layout="wide")

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 40px;
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💼 Employee Management System")

# SESSION STATE
if "employees" not in st.session_state:
    st.session_state.employees = []

# ================= ADD =================
st.sidebar.header("➕ Add Employee")

name = st.sidebar.text_input("Employee Name")
dept = st.sidebar.selectbox("Department", ["HR", "IT", "Finance", "Marketing"])
salary = st.sidebar.number_input("Salary")

if st.sidebar.button("Add Employee"):
    if name != "":
        st.session_state.employees.append({
            "Name": name,
            "Department": dept,
            "Salary": salary
        })
        st.success("Employee Added Successfully")
        st.rerun()
    else:
        st.error("Enter Employee Name")

# ================= DISPLAY =================
st.subheader("📊 Employee Records")

if st.session_state.employees:
    df = pd.DataFrame(st.session_state.employees)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No Employees Added Yet")

# ================= DELETE =================
st.subheader("🗑 Delete Employee")

if st.session_state.employees:
    delete_name = st.selectbox("Select Employee to Delete", df["Name"], key="delete")

    if st.button("Delete"):
        st.session_state.employees = [
            emp for emp in st.session_state.employees
            if emp["Name"] != delete_name
        ]
        st.success("Employee Deleted")
        st.rerun()

# ================= UPDATE =================
st.subheader("✏ Update Employee")

if st.session_state.employees:
    update_name = st.selectbox("Select Employee to Update", df["Name"], key="update")
    new_salary = st.number_input("New Salary")

    if st.button("Update Salary"):
        for emp in st.session_state.employees:
            if emp["Name"] == update_name:
                emp["Salary"] = new_salary
        st.success("Salary Updated")
        st.rerun()