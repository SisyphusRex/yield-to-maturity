This is a work in progress.

Years ago, in a Finance class, I came upon the Yield to Maturity formula for a bond.  I could solve for all variables using
algebra except one: interest (r).

After progressing in my mathematics regimen and learning some new calculus, I discovered the tool I needed.
Newton's Method of Approximation.

I previous performed the calculus on the Yield to Maturity formula and tested its efficacy in Excel.
This venture is to rewrite the algorithm in Python and make a program that will solve for any variable given the others.

The  attached Excel and Word files are my original work from 2019.

This is my original email:
Do you remember that complex financial equation I had?  It concerns the valuation of a bond taking into account the time value of money.  I could not calculate the the value of r given all other variables because I could not isolate r algebraically.  I could estimate r by plugging in different values until the output was very close to the expected value, but that seemed arbitrary and time consuming.  Microsoft Excel and financial calculators can approximate r automatically but their methods are hidden.

After scouring the internet, I discovered some complex methods of approximation including Newton's Method.  Newton's Method is used for approximating the zeroes of a function, but I adapted it to suit my needs by a simple subtraction.  It does so by calculating the x-intercept of the tangent line of an initial (arbitrary) point on the function, and then calculates the x-intercept of the tangent line of the point identified on the function from the previous tangent line.  Each successive calculation, or iteration, is more accurate and closer to the actual zero of the function.  The values converge on the actual value.  The basic algorithm looks like this:
image.png
Now that I know how to differentiate, I was able to find the derivative of my complex equation and create my own algorithm!  There is much calculation just for one iteration so I ported the equation to Excel and copied it for each iteration.  I compared my results to Excel's built in financial tools and I believe my approximation is more accurate!  From my perspective, this is the first time anyone has applied Newton's Method to Bond Valuation and Yield to Maturity.  I am keen to learn, though, what algorithm Excel uses and why it truncates or rounds after a certain amount of digits.


Yield to Maturity equation:
$P = C \ast \frac{1 - {(1 + r)}^{-N}}{r} + \frac{M}{{(1 + r)}^N}$
* P: present value of the bond; market price
* C: annual interest payment to investor
* N: number of years until the bond matures
* M: maturity value of the bond; par value
* r: rate of return; yield to maturity; annual rate of return from fixed interest security at a given price, P, and held until maturity

Newton's Method:
$x_1 = x_0 - \frac{f(x_0)}{f'(x_0)}$


Newton's Method on Yield to Maturity with respect to r:
$r_{n+1} = r_n - \frac{C * \frac{1 - {(1+r)}^{-N}}{r} + \frac{M}{{(1+r)}^N} - P}{C * \frac{rN{(1+r)}^{-(N-1)} + {(1+r)}^{-N}-1}{r^2} + \frac{-MN{(1+r)}^{N-1}}{{(1+r)}^{2N}}}$

Newton's Method, or Newton-Raphson method, is a root-finding algorithm for finding the roots, or zeroes, of a function where f(x) = 0.  You start with an initial guess of x, calculate the tangent line of the function at x, then find the x intercept of the tangent line.  Then you calculate the tangent line of the function at the x intercept.  This is repeated and the more you repeat the process, the closer x becomes to the root.

We are substituting the rate of return, r, for x.  Given the values of all other variables, the root of the function will be the rate of return, r.


NOTE: I want this program to be a Yield To Maturity equation solver.  The user will pick a variable to solve for, provide values for the other variables, and my program will solve for that variable.  Most variables will be solved algebraically, but r must be solved using Newton's method.


* Compile
    1. move to above root directory
    2. javac -d yield2maturity/bin yield2maturity/src/*.java
* Run
    1. java -cp yield2maturity/bin yield2maturity.src.Bootstrap