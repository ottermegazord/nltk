from sklearn.datasets as load_iris

iris = load_iris()

X = iris.data
y = iris.target

print(X.shape)
print(y.shape)