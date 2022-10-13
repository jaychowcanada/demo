import numpy
import pandas
import sklearn.linear_model as lm
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# display the regression model in graph
def polynomialRegression(x, y):
    model = numpy.poly1d(numpy.polyfit(x, y, 5)) # make a polynomial model from numpy method
    line = numpy.linspace(1, 22, 80)  # line display setting to fit the data

    plt.scatter(x, y)
    plt.plot(line, model(line))
    plt.show()


def multipleRegression():
    data = {
    "publicFloat": [25, 50, 80], # % of shares holding in public
    "listingDuration": [50, 40, 45], # number of days since the companies listed
    "stockPrice": [30, 15, 5] # stock closing price at the above days
    }

    #load data into a DataFrame object:
    df = pandas.DataFrame(data)

    X = df[['publicFloat', 'listingDuration']]
    y = df['stockPrice']

    linRegr = lm.LinearRegression()
    linRegr.fit(X, y)

    predictedPrice = linRegr.predict([[35, 180]])  # predict the stock price ($87) for a stock with 35% shares holding in public and listed for half a year

    print(predictedPrice)

def train_and_predict(x, y):
    # allcate 80% of data to train the machine
    trainX = x[:80]
    trainY = y[:80]

    # allcate 20% of data to test the trained machine
    testX = x[80:]
    testY = y[80:]

    model = numpy.poly1d(numpy.polyfit(trainX, trainY, 4)) # build the regression model

    rSquare = r2_score(trainY, model(trainX)) # check how close the relationship between the variable by considering the R-squared.

    print(f'The R-squared of this trained model is {rSquare:.2f}. and the predicted value is {model(3):.2f}')


def main():
    # random data sets:
    numpy.random.seed(2)
    x = numpy.random.normal(10, 1, 100) 
    y = numpy.random.normal(50, 5, 100) / x

    # polynomialRegression(x, y)
    # multipleRegression()
    train_and_predict(x, y)

if __name__ == "__main__":
    main()