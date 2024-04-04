from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def load_data():
    iris = datasets.load_iris()
    X = iris.data  # Features
    y = iris.target  # Target variable
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def save_model(model, filename='linear_regression_model.pkl'):
    joblib.dump(model, filename)

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return mse, r2

def main():
    # Load data
    X, y = load_data()
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Save the model to disk
    save_model(model)
    
    # Evaluate the model
    mse, r2 = evaluate_model(model, X_test, y_test)
    
    # Print evaluation metrics
    print("Mean Squared Error:", mse)
    print("R-squared Score:", r2)

if __name__ == "__main__":
    main()
