# Given values
total_samples = 500
predicted_positive = 100
actual_positive = 50
true_positive = 45

# Calculate the metrics
false_positive = predicted_positive - true_positive
false_negative = actual_positive - true_positive
true_negative = total_samples - (true_positive + false_positive + false_negative)

# Calculate accuracy
accuracy = (true_positive + true_negative) / total_samples

# Calculate precision
precision = true_positive / (true_positive + false_positive)

# Calculate recall
recall = true_positive / (true_positive + false_negative)

# Calculate F1 score
f1_score = 2 * (precision * recall) / (precision + recall)

# Print the metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1_score)
