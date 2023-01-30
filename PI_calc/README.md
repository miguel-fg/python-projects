# PI calculations

Python implementations of various PI calculation algorithms. Python is ideal to work with precise numbers (and data in general) thanks to its huge library of modules. In this case, the [Decimal](https://docs.python.org/3/library/decimal.html) module lets me focus on the algorithm without having to worry about data types not being able to store or display the value. 

## Leibniz 

Apparently Leibniz has enough things named after him that [this](https://en.wikipedia.org/wiki/List_of_things_named_after_Gottfried_Leibniz) Wikipedia entry exists, cool. This is a very simple series but EXTREMELY slow to converge, 1 million iterations is barely enough to get "3.14159". I may add a graph showing how it compares to the actual value of PI over each iteration.

The formula for $\pi$ is defined as

$$\frac{\pi}{4} = 1-\frac{1}{3}+\frac{1}{5}-\frac{1}{7}+\frac{1}{9}-...$$

## Chudnovsky

Much more efficient method to calculate $\pi$, this algorithm is converges rapidly and it's still being used to calculate its digits. In March 2022, it broke the 100 trillion digits world record. Be wary that because of the use of factorial in the formula, the time complexity of this algorithm increases extremely fast, I recommend not going past 100 as the precision setting without multithreading. 

The algorithm states that

$$\frac{1}{\pi} = 12\sum_{q=0}^{\infty} \frac{(-1)^q(6q)!(545140134q + 13591409)}{(3q)!(q!)^3(640320)^{3q + \frac{3}{2}}} $$

## Bailey-Borwein-Plouffe

$$\pi = \sum_{k=0}^{\infty} [\frac{1}{16^k}(\frac{4}{8k+1} - \frac{2}{8k+4} - \frac{1}{8k+5} - \frac{1}{8k+6})]$$
