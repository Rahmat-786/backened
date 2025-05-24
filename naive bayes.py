from sklearn.naive_bayes import GaussianNB # Assuming continuous features
# ... (Load your data into X and y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

gnb = GaussianNB()
gnb.fit(X_train, y_train)

y_pred = gnb.predict(X_test)

print("Naive Bayes Accuracy:", accuracy_score(y_test, y_pred))


