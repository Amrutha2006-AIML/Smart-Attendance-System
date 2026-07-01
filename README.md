# Smart Attendance System Using Face Recognition

## Abstract

The Smart Attendance System is an Artificial Intelligence (AI) based application designed to automate the attendance process using face recognition technology. The system captures student facial images through a webcam, trains a machine learning model using the Local Binary Pattern Histogram (LBPH) algorithm, and identifies registered students during live recognition. Once a student is successfully recognized, the attendance is automatically recorded with the current date and time in a CSV file.

The project eliminates manual attendance procedures, reduces proxy attendance, and provides an efficient and cost-effective attendance management solution. It is developed using Python, OpenCV, NumPy, and file handling techniques, making it suitable for educational institutions and small organizations.

---

# Introduction

Traditional attendance systems require manual roll calls or paper-based registers, which consume valuable classroom time and are prone to human errors. They also make it easy for students to mark attendance on behalf of others.

To overcome these limitations, this project introduces an AI-based Smart Attendance System that automatically identifies students using facial recognition technology. The system captures facial images, trains an LBPH face recognition model, and recognizes students in real time using a webcam. Attendance is recorded automatically only for registered students, thereby improving accuracy and reducing manual effort.

---

# Problem Statement

Manual attendance systems have several drawbacks:

* Time-consuming attendance process.
* Human errors while recording attendance.
* Proxy attendance by students.
* Difficulty in maintaining attendance records.
* Lack of automation.

An intelligent attendance system capable of recognizing students automatically and storing attendance digitally is therefore required.

---

# Objectives

* Automate attendance recording using facial recognition.
* Eliminate manual attendance registers.
* Prevent proxy attendance.
* Improve attendance accuracy.
* Store attendance digitally in CSV format.
* Develop a simple and user-friendly attendance system.

---

# Technologies Used

| Technology     | Purpose                              |
| -------------- | ------------------------------------ |
| Python         | Programming Language                 |
| OpenCV         | Face Detection and Recognition       |
| NumPy          | Numerical Operations                 |
| Haar Cascade   | Face Detection                       |
| LBPH Algorithm | Face Recognition                     |
| CSV            | Attendance Storage                   |
| Tkinter        | Graphical User Interface (GUI)       |
| Arduino        | Hardware Feedback (LED, LCD, Buzzer) |

---

# System Architecture

The Smart Attendance System consists of four major phases:

### Phase 1: Face Registration

Students enter their unique ID and Name.

The webcam captures approximately 50 facial images from different positions and stores them inside the dataset folder.

The student information is also stored in the `names.txt` file for future identification.

---

### Phase 2: Model Training

After the dataset is created, the system trains the LBPH Face Recognizer using all captured images.

Each image is associated with the corresponding student ID.

The trained model is then saved as:

```text
trainer/trainer.yml
```

This model is later used during real-time attendance recognition.

---

### Phase 3: Face Recognition

During attendance marking,

* Webcam captures live video.
* Haar Cascade detects faces.
* Detected faces are converted into grayscale.
* LBPH predicts the student's identity.
* Prediction confidence is calculated.
* If confidence is acceptable, the student is recognized successfully.

Unknown faces are rejected automatically.

---

### Phase 4: Attendance Recording

Once a student is recognized,

* The student's name is retrieved.
* Duplicate attendance is checked.
* Current date and time are recorded.
* Attendance is saved into

```text
attendance.csv
```

Only one attendance entry is recorded per student during a session.

---

# Project Workflow

```text
Student Registration
        │
        ▼
Capture Face Images
        │
        ▼
Dataset Creation
        │
        ▼
Train LBPH Model
        │
        ▼
Generate trainer.yml
        │
        ▼
Start Recognition
        │
        ▼
Detect Face
        │
        ▼
Recognize Student
        │
        ▼
Check Duplicate Entry
        │
        ▼
Store Attendance
```

---

# Modules Description

## 1. Face Capture Module

Responsible for collecting student facial images.

Functions:

* Opens webcam.
* Detects faces.
* Captures approximately 50 images.
* Saves images into dataset folder.
* Stores student ID and Name.

---

## 2. Face Training Module

Responsible for training the machine learning model.

Functions:

* Reads captured images.
* Extracts IDs.
* Trains LBPH recognizer.
* Saves trained model.

---

## 3. Face Recognition Module

Responsible for recognizing registered students.

Functions:

* Opens webcam.
* Detects faces.
* Predicts identity.
* Displays student name.
* Rejects unknown faces.

---

## 4. Attendance Module

Responsible for attendance management.

Functions:

* Creates attendance.csv.
* Saves Name.
* Saves Date.
* Saves Time.
* Prevents duplicate attendance.

---

## 5. GUI Module

Provides a user-friendly interface.

Functions:

* Face Registration
* Model Training
* Attendance Recognition
* Live Camera Display
* Status Messages

---

## 6. Arduino Integration Module

Provides hardware feedback.

Functions:

* LED indication
* LCD Display
* Buzzer Alert
* Recognition Status Display

---

# Features

* Automatic Attendance Recording
* Face Detection using Haar Cascade
* Face Recognition using LBPH
* Student Registration
* Dataset Generation
* Model Training
* Real-Time Attendance
* Duplicate Entry Prevention
* CSV Attendance Storage
* User-Friendly GUI
* Arduino Hardware Support

---

# Advantages

* Eliminates manual attendance.
* Saves classroom time.
* Prevents proxy attendance.
* Easy to use.
* Cost-effective.
* Digital attendance records.
* Fast recognition process.
* Simple implementation using Python.

---

# Limitations

* Recognition accuracy depends on lighting conditions.
* Performance decreases with poor image quality.
* Requires student registration before use.
* Stores attendance locally.
* Limited scalability for very large datasets using LBPH.

---

# Results

The developed Smart Attendance System successfully recognizes registered students using facial recognition technology and records attendance automatically.

The system:

* Detects student faces accurately.
* Identifies registered users.
* Rejects unknown individuals.
* Prevents duplicate attendance.
* Stores attendance records with timestamps.
* Provides a simple and interactive user interface.

---

# Future Enhancements

* Replace LBPH with FaceNet or DeepFace.
* Integrate cloud database support.
* Develop a web-based dashboard.
* Add liveness detection.
* Support multiple face recognition simultaneously.
* Mobile application integration.
* Attendance analytics dashboard.
* Email and SMS notification support.

---

# Folder Structure

```text
Smart-Attendance-System/
│
├── dataset/
├── trainer/
│     └── trainer.yml
├── evaluation.py
├── capture.py
├── train.py
├── recognize.py
├── names.txt
├── attendance.csv
├── requirements.txt
├── README.md
└── images/
```

---

# Conclusion

The Smart Attendance System demonstrates the practical application of Artificial Intelligence and Computer Vision in automating classroom attendance. By combining Haar Cascade face detection with the LBPH face recognition algorithm, the system provides a reliable solution for identifying registered students and recording attendance automatically. The project reduces manual effort, minimizes proxy attendance, and maintains attendance records digitally. Its modular architecture, ease of use, and potential for future enhancements make it a valuable academic project and a strong addition to a software engineering portfolio.


