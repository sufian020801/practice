import unittest
from training import load_data, split_data, train_model, evaluate_model
import joblib
from sklearn import datasets
class TestFunctions(unittest.TestCase):

    def test_load_data(self):
        X, y = load_data()
        self.assertIsNotNone(X)
        self.assertIsNotNone(y)
        self.assertEqual(X.shape[1], 4)  # Assuming Iris dataset always has 4 features

    def test_split_data(self):
        X = [[1, 2], [3, 4], [5, 6], [7, 8]]
        y = [1, 2, 3, 4]
        X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)
        self.assertEqual(len(X_train), 3)
        self.assertEqual(len(X_test), 1)
        self.assertEqual(len(y_train), 3)
        self.assertEqual(len(y_test), 1)

    def test_train_model(self):
        X_train = [[1, 2], [3, 4], [5, 6]]
        y_train = [1, 2, 3]
        model = train_model(X_train, y_train)
        self.assertIsNotNone(model)

    def test_evaluate_model(self):
        model = joblib.load('linear_regression_model.pkl')
        self.assertIsNotNone(model)
        iris = datasets.load_iris()
        X_test = iris.data  # Test features
        y_test = iris.target  # Test target variable
        mse, r2 = evaluate_model(model, X_test, y_test)
        self.assertIsNotNone(mse)
        self.assertIsNotNone(r2)

if __name__ == '__main__':
    unittest.main()
