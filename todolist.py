import streamlit as st

st.title("To do list")
st.header("Manage your tasks")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

task = st.text_input(
    "Enter your task",
    placeholder="eg: complete python assignment"
)

if st.button("Add task"):
    if task.strip() == "":
        st.warning("please enter a task")
    else:
        st.session_state.tasks.append(task)
        st.success("task added")
        st.subheader("your tasks")

for i, task_item in enumerate(st.session_state.tasks, start=1):
    st.write(f"{i}. {task_item}")

    Done = st.checkbox("done", key=f"task_{i}")
    if Done:
        st.success("TASK COMPLETED")