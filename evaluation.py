import cv2
import os
import numpy as np
import random
from collections import defaultdict

dataset_path = "dataset"

# Load all images
data = []

for file in os.listdir(dataset_path):
    path = os.path.join(dataset_path, file)
    img = cv2.imread(path, 0)

    if img is None:
        continue

    try:
        id = int(file.split('.')[1])
    except:
        continue

    data.append((img, id))

# Shuffle data
random.shuffle(data)

# Split (80% train, 20% test)
split = int(0.8 * len(data))
train_data = data[:split]
test_data = data[split:]

# Prepare training data
train_faces = [x[0] for x in train_data]
train_ids = [x[1] for x in train_data]

# Train recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(train_faces, np.array(train_ids))

# Testing
correct = 0
total = 0

y_true = []
y_pred = []

for img, actual_id in test_data:
    predicted_id, confidence = recognizer.predict(img)

    y_true.append(actual_id)
    y_pred.append(predicted_id)

    total += 1

    if predicted_id == actual_id:
        correct += 1

# Accuracy
if total == 0:
    print("No test data available")
else:
    accuracy = (correct / total) * 100

    # Calculate Precision, Recall, F1 (macro average)
    classes = list(set(y_true))
    precision_list = []
    recall_list = []
    f1_list = []

    for c in classes:
        TP = sum((p == c and t == c) for p, t in zip(y_pred, y_true))
        FP = sum((p == c and t != c) for p, t in zip(y_pred, y_true))
        FN = sum((p != c and t == c) for p, t in zip(y_pred, y_true))

        precision = TP / (TP + FP) if (TP + FP) != 0 else 0
        recall = TP / (TP + FN) if (TP + FN) != 0 else 0

        if (precision + recall) != 0:
            f1 = 2 * (precision * recall) / (precision + recall)
        else:
            f1 = 0

        precision_list.append(precision)
        recall_list.append(recall)
        f1_list.append(f1)

    precision = sum(precision_list) / len(precision_list)
    recall = sum(recall_list) / len(recall_list)
    f1_score = sum(f1_list) / len(f1_list)

    print("Training Samples:", len(train_data))
    print("Testing Samples:", len(test_data))
    print("Correct Predictions:", correct)
    print("Accuracy:", accuracy, "%")
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1_score)