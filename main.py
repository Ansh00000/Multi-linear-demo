# Importing a single global Imports for convenience
from res.imports import *

# Taking the Data
# dataset = pd.read_csv("res/50_Startups.csv")
x = dc.Data.getdata().iloc[:, :-1]
y = dc.Data.getdata().iloc[:, -1]

# Converting the categorical data into numerical (Column :4 of dataset)
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

# Splitting the Data in Test case and Training set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)
y_test = np.array(y_test)

# Training the model
regressor = LinearRegression()
regressor.fit(x_train, y_train)

# predicting values of test cases
y_pred = regressor.predict(x_test)
y_pred = np.array(y_pred)
np.set_printoptions(precision=2)

# concatenating both arrays into single 2D array for easy comparison
var1 = y_pred.reshape(len(y_pred), 1)
var2 = y_test.reshape(len(y_test), 1)
output = np.concatenate((var1, var2), 1)

# printing the predicted VS real profit values
prnt.Printer().printToConsole(output)





