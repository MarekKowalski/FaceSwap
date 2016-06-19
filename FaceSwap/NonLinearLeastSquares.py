import numpy as np
from scipy import optimize

def LineSearchFun(alpha, x, d, fun, args):
    r = fun(x + alpha * d, *args)
    return np.sum(r**2)

def GaussNewton(x0, fun, funJack, args, maxIter=10, eps=10e-7, verbose=1):
    x = np.array(x0, dtype=np.float64)

    oldCost = -1
    for i in range(maxIter):
        r = fun(x, *args)
        cost = np.sum(r**2)

        if verbose > 0:
            print "Cost at iteration " + str(i) + ": " + str(cost)

        if (cost < eps or abs(cost - oldCost) < eps):
            break
        oldCost = cost

        J = funJack(x, *args)
        grad = np.dot(J.T, r)
        H = np.dot(J.T, J)
        direction = np.linalg.solve(H, grad)

        #optymalizacja dlugosci kroku
        lineSearchRes = optimize.minimize_scalar(LineSearchFun, args=(x, direction, fun, args))
        #dlugosc kroku
        alpha = lineSearchRes["x"]

        x = x + alpha * direction
        
    if verbose > 0:
        print "Gauss Netwon finished after "  + str(i + 1) + " iterations"
        r = fun(x, *args)
        cost = np.sum(r**2)
        print "cost = " + str(cost)
        print "x = " + str(x)

    return x

def SteepestDescent(x0, fun, funJack, args, maxIter=10, eps=10e-7, verbose=1):
    x = np.array(x0, dtype=np.float64)

    oldCost = -1
    for i in range(maxIter):
        r = fun(x, *args)
        cost = np.sum(r**2)

        if verbose > 0:
            print "Cost at iteration " + str(i) + ": " + str(cost)

        #warunki stopu
        if (cost < eps or abs(cost - oldCost) < eps):
            break
        oldCost = cost

        J = funJack(x, *args)
        grad = 2 * np.dot(J.T, r)
        direction = grad

        #optymalizacja dlugosci kroku
        lineSearchRes = optimize.minimize_scalar(LineSearchFun, args=(x, direction, fun, args))
        #dlugosc kroku
        alpha = lineSearchRes["x"]

        x = x + alpha * direction

    if verbose > 0:
        print "Steepest Descent finished after "  + str(i + 1) + " iterations"
        r = fun(x, *args)
        cost = np.sum(r**2)
        print "cost = " + str(cost)
        print "x = " + str(x)


    return x

