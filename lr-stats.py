class myLR:
    def __init__(self):
        self.m =  None
        self.b = None

    def fit(self, x_train, y_train):
        print("training values from excel sheet are : ", x_train)
        print("variable type of x_train : ",type(x_train))

        num = 0
        den = 0
        for i in range(x_train.shape[0]):
            num = num + ((x_train[i] - x_train.mean())*(y_train[0] - y_train.mean()))
            den = den + ((x_train[i] - x_train.mean())*(x_train[i] - x_train.mean()))

        self.m = num/den
        self.b = y_train.mean() - (self.m * x_train.mean())
        print("slope is ", self.m)
        print("intercept is ", self.b)

    def predict(self, x_test):
        return (self.m * x_test + self.b)
