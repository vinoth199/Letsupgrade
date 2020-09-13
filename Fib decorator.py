{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, "
     ]
    }
   ],
   "source": [
    "#ans 1\n",
    "class ibonacci:\n",
    "\n",
    "    def __init__(self):\n",
    "        self.cache = {}\n",
    "\n",
    "    def __call__(self, n):\n",
    "        if n not in self.cache:\n",
    "            if n == 0:\n",
    "                self.cache[0] = 0\n",
    "            elif n == 1:\n",
    "                self.cache[1] = 1\n",
    "            else:\n",
    "                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)\n",
    "        return self.cache[n]\n",
    "\n",
    "fib = Fibonacci()\n",
    "\n",
    "for i in range(20):\n",
    "    print(fib(i), end=\", \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
