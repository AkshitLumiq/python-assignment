from pysr import PySRRegressor
import csv

l = []
with open('Python_assignmentSpecial.csv', newline='') as f:
  reader = csv.reader(f)
  l = list(reader)


y=[]
X=[]
for i in l:
  try:
    y.append([float(i[0])])
  except ValueError:
    pass

for i in range(1, 201):
    X.append([i])

# print(X)
# print(y)

model = PySRRegressor(
    niterations=40,  # < Increase me for better results
    binary_operators=["+", "*", "-", "/"],
    unary_operators=[
        "cos",
        "exp",
        "sin",
        "inv(x) = 1/x",
        "log",
        "tan",
        # ^ Custom operator (julia syntax)
    ],
    extra_sympy_mappings={"inv": lambda x: 1 / x},
    # ^ Define operator for SymPy as well
    loss="loss(prediction, target) = (prediction - target)^2",
    # ^ Custom loss function (julia syntax)
)

model.fit(X, y)

print(model)