# Linear Regression Project

This tiny project is made for educational purposes. 

I want to do some practice using linear regression formulas and calculate other indicators like RSE,RSS, SE and the correlation between x and y.

I would also like to implement an import/export for different data sets (csv) and create random functions.

Finally, all the results are diplayed in a plot which is created using matplotlib.

# Predict a function using real data set

You can manually enter [x, y] values.
```
f = linearRegression()
f.insert(np.array([1,2,3]), np.array([1,2,3]))
f.prediction()
f.show()
```

![Plot #1](http://prioscuola.altervista.org/Figure_1.png)

:warning: [x, y] values must be stored in an array


# Create random [x, y] values and make a prediction

```
f = linearRegression()
f.create()
f.prediction()
f.show()
```

![Plot #2](http://prioscuola.altervista.org/Figure_2.png)
