
import streamlit as st

# Function to convert Grades to Points
def grade_to_points(grade):
    grade_map = {
        'A+': 4.0, 'A': 3.5, 'B': 3.0, 'C': 2.5, 'D': 2.0, 'F': 0.0
    }
    return grade_map.get(grade.upper(), 0.0)

# Function to calculate GPA
def calculate_gpa(credits, grades):
    total_credits = 0  # Initializing total credits to 0
    weighted_sum = 0
    
    for credit, grade in zip(credits, grades):
        credit = int(credit)
        points = grade_to_points(grade)
        
        total_credits += credit  # Accumulating total credits
        weighted_sum += credit * points
    
    if total_credits == 0:  # Avoid division by zero
        return 0.0
    
    gpa = weighted_sum / total_credits
    return min(gpa, 4.0)  # Ensuring max GPA is 4.0

st.set_page_config(page_title="GPA Calculator", page_icon=":mortar_board:")

st.title("GPA Calculator")

num_courses = st.number_input("Enter the number of Courses:", min_value=1, step=1, value=1)

credits = []
grades = []

st.write("Enter Credits and select Grade for each Course:")

columns = st.columns(2)
for i in range(num_courses):
    with columns[0]:  # Column for Credits
        credit = st.number_input(f"Credits:", min_value=0, step=1, value=0, key=f"credit_{i}")
        credits.append(credit)
    
    with columns[1]:  # Column for Grades
        grade = st.selectbox(f"Grade:", ('A+', 'A', 'B', 'C', 'D', 'F'), index=0, key=f"grade_{i}")
        grades.append(grade)

if st.button("Calculate GPA"):
    gpa = calculate_gpa(credits, grades)    
    st.subheader(f"Your GPA is {gpa:.2f}")
# These changes ensure that the GPA calculation is based on a total of 4 credits, and the maximum GPA is capped at 4.0. Additionally, I've corrected the condition where the total credits are checked for being 4; instead, it should be initialized to 0 and accumulate the credits.
