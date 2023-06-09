#coded with 💖 by marwaneldesouki
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("../DataSet/keys_power.csv") 

X = df[['Length', 'Contains Numbers Binary']]
print(X)
y = df['Power Status']



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create the KNN model with k=3 (you can adjust the value of k as per your requirement)
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model using the training set
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
# Print the classification report
print(classification_report(y_test, y_pred))

# Calculate and print the accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Assuming you have a new key with length=9 and it contains numbers
new_example = pd.DataFrame([[22, 1]], columns=['Length', 'Contains Numbers Binary'])
predicted_power_status = knn.predict(new_example)
print("Predicted Power Status:", predicted_power_status)


#coded with 💖 by marwaneldesouki 
