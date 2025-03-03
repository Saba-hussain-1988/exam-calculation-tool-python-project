import streamlit as st
import math

# function check grade
def check_grade(percentage):
        if percentage >= 90:
            return "A+ (Excellent)"
        elif percentage >= 80:
            return "A (Very Good)"
        elif percentage >= 70:
            return "B (Good)"
        elif percentage >= 60:
            return "C (Satisfactory)"
        elif percentage >= 50:
            return "D (Pass)"
        else:
            return "F (Fail)"


st.title("Examination Calculation")

# student's information
name = st.text_input("Student's Name: ").title()
father_name = st.text_input("Father's Name: ").title()
_class = st.text_input("Class: ")
_date = st.date_input("Date: ")

# student's examination marks input
eng_outOf = st.number_input("English: out of")
english = st.number_input("English: Obtained Marks ")
urdu_outOf = st.number_input("Urdu: out of")
urdu = st.number_input("Urdu: Obtained Marks ")
math_outOf = st.number_input("Mathematics: out of")
math = st.number_input("Mathematics: Obtained Marks ")
sci_outOf = st.number_input("General Science: out of")
science = st.number_input("General Science: Obtained Marks ")
Sst_outOf = st.number_input("Social Study: out of")
study = st.number_input("Social Study: Obtained Marks ")
isl_outOf = st.number_input("Islamic Study: out of")
islamiyat = st.number_input("Islamic Study: Obtained Marks ")
com_outOf = st.number_input("Computer: out of")
computer = st.number_input("Computer: Obtained Marks ")
art_outOf = st.number_input("Art\ Fun: out of")
art = st.number_input("Art\ Fun: Obtained Marks ")


calculate_generate = st.button("Calculate and Generate")
if calculate_generate:
    #  make sure all fields are filled
    if name and father_name and _class and _date and eng_outOf and english and urdu_outOf and urdu and math_outOf and math and sci_outOf and science and Sst_outOf and study and isl_outOf and islamiyat and com_outOf and computer and art_outOf and art:

      # calculation
        total_marks = eng_outOf + urdu_outOf + math_outOf + sci_outOf + Sst_outOf + isl_outOf + com_outOf + art_outOf
        total_obtained_marks = english + urdu + math + science + study + islamiyat + computer +  art 
    
        # percentage
        percentage = (total_obtained_marks / total_marks) * 100
        percentage_final = format(percentage, ".2f")


        grade = check_grade(percentage)
        st.header("Result Card")
        st.write(f"Name: {name}")
        st.write(f"Father's Name: {father_name}")
        st.write(f"Class: {_class}")
        st.write(f"Date: {_date}")
        st.write(f"Total Marks: {total_marks}")
        st.write(f"Total Obtained Marks: {total_obtained_marks}")
        st.write("Percentage: " + str(percentage_final))
        st.write(f"Grade: {grade}")
    else :
        st.error("❌ Please fill all fields!")


st.markdown("<h6 style='text-align: center; color: grey;'>Developed and designed by <a href='mailto:sabamustafa27.88@gmail.com'>Saba Chohan</a></h6>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><a href='https://linkedin.com/in/saba-mustafa-ahmed-3aa41a322'><img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='20' height='20'></a> <a href='https://www.facebook.com/share/17fqow4nrL/'><img src='https://cdn-icons-png.flaticon.com/512/124/124010.png' width='20' height='20'></a> </p>", unsafe_allow_html=True)

