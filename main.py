import streamlit as st
import cv2
import ExerciseTrainer as exercise
import time


def main():
    st.set_page_config(page_title='Krida AI', layout='centered')

    st.title('Krida AI')

    options = st.sidebar.selectbox('Select Option',
                                   ('Manual Exercise Mode', 'Auto Classify Mode'))

    # ===== MANUAL MODE =====
    if options == 'Manual Exercise Mode':

        st.sidebar.markdown('-------')

        exercise_general = st.sidebar.selectbox(
            'Select Exercise',
            ('Bicept Curl', 'Push Up', 'Squat', 'Shoulder Press')
        )

        st.write("Click to start exercise with webcam")

        start_button = st.button('Start Exercise')

        if start_button:
            time.sleep(1)

            cap = cv2.VideoCapture(0)
            exer = exercise.Exercise()

            if exercise_general == 'Bicept Curl':
                exer.bicept_curl(cap)

            elif exercise_general == 'Push Up':
                exer.push_up(cap)

            elif exercise_general == 'Squat':
                exer.squat(cap)

            elif exercise_general == 'Shoulder Press':
                exer.shoulder_press(cap)


    # ===== AUTO CLASSIFY MODE =====
    elif options == 'Auto Classify Mode':

        st.markdown('-------')
        st.write("Automatic exercise detection and counting")
        st.write("Just stand in front of camera and perform any exercise")

        auto_button = st.button("Start Auto Classify")

        if auto_button:
            time.sleep(1)
            exer = exercise.Exercise()
            exer.auto_classify_and_count()


if __name__ == '__main__':
    main()
