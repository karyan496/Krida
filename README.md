# **Krida – AI Fitness Trainer**

Krida is an AI-powered fitness trainer application that uses computer vision and deep learning to track body movements, recognize exercises, and count repetitions in real time.
The system supports both **manual exercise selection** and **automatic exercise classification**, making workouts smart, interactive, and hands-free.

---

## 🚀 Features

* Real-time exercise tracking using webcam
* AI-based pose estimation using **MediaPipe**
* Automatic exercise recognition using **Deep Learning (LSTM model)**
* Supports multiple exercises:

  * Push-ups
  * Squats
  * Bicep Curls
  * Shoulder Press
* Accurate repetition counting
* Stop gesture using **hands-joined detection**
* Interactive UI built with **Streamlit**

---

## 🛠 Technologies Used

* Python
* OpenCV
* MediaPipe
* TensorFlow / Keras
* Scikit-Learn
* Streamlit
* NumPy
* Joblib

---

## 📁 Project Structure

This project is divided into multiple Python modules.
Each file has a specific role:

### 1. **main.py**

This is the entry point of the application.

* Provides Streamlit-based UI
* Allows the user to:

  * Select exercise manually
  * Start webcam mode
  * Run automatic classification mode
* Handles navigation and user interaction

**Purpose:**
Acts as the main controller of the application.

---

### 2. **ExerciseTrainer.py**

This is the core logic file of the project.

It contains:

* Exercise class
* Functions to:

  * Count repetitions
  * Process webcam frames
  * Detect stop gesture
  * Run auto-classify mode
* Logic for:

  * Push-ups
  * Squats
  * Bicep curls
  * Shoulder press
* Deep learning model integration for exercise classification

**Purpose:**
Handles all exercise processing, AI classification, and counting logic.

---

### 3. **PoseModule2.py**

Custom pose detection module built on top of MediaPipe.

Contains:

* `posture_detector` class
* Functions to:

  * Detect human pose
  * Draw landmarks
  * Calculate angles between joints
  * Extract coordinates

**Purpose:**
Responsible for pose estimation and angle calculations used by ExerciseTrainer.

---

### 4. **AiTrainer_utils.py**

Utility helper file.

Includes:

* Image resizing functions
* FPS calculation
* Distance calculation between two points

**Purpose:**
Provides supporting helper functions used across the project.

---

### 5. **Trained Model Files**

These are required for auto classification mode:

* `final_forthesis_bidirectionallstm_and_encoders_exercise_classifier_model.h5`
  → Trained LSTM model

* `thesis_bidirectionallstm_scaler.pkl`
  → Feature scaler

* `thesis_bidirectionallstm_label_encoder.pkl`
  → Label encoder

**Purpose:**
Used for automatic exercise recognition.

---

### 6. **requirements.txt**

Contains all Python dependencies required to run the project.

**Purpose:**
Allows easy installation of all required libraries.

---

## ⚙ Installation

### Step 1 – Clone the repository

```bash
git clone https://github.com/your-username/krida.git
cd krida
```

### Step 2 – Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3 – Run the application

```bash
streamlit run main.py
```

---

## 🧑‍💻 How to Use

1. Run the application
2. Choose mode from sidebar:

   * **WebCam Mode** → Select exercise manually
   * **Auto Classify Mode** → Let AI detect exercise
3. Start performing exercise
4. Repetitions will be counted automatically
5. Join your hands together to stop the session

---

## 🎯 Future Improvements

* Add more exercises
* Improve auto classification accuracy
* Add form correction feedback
* Add mobile app support

---

## 📌 Conclusion

Krida is designed to act as a virtual AI gym trainer that helps users perform exercises correctly and track progress in real time using computer vision and deep learning.
