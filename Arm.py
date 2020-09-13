{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#ans 2:\n",
    "lower = int(input(\"Enter lower range: \"))\n",
    "upper = int(input(\"Enter upper range: \"))\n",
    "#generator function armstrong()\n",
    "def armstrong():\n",
    "  for num in range(lower,upper + 1):\n",
    "   sum = 0\n",
    "   temp = num\n",
    "   while temp > 0:\n",
    "       digit = temp % 10\n",
    "       sum += digit ** 3\n",
    "       temp //= 10\n",
    "   if num == sum:\n",
    "       print(num)\n",
    "# generator object  is x\n",
    "x = armstrong()\n",
    "print(x)\n",
    "\n",
    " \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "Jupyter Notebook\n",
    "Arm\n",
    "\n",
    "#ans 2:\n",
    "2\n",
    "lower = int(input(\"Enter lower range: \"))\n",
    "3\n",
    "upper = int(input(\"Enter upper range: \"))\n",
    "4\n",
    "#generator function armstrong()\n",
    "5\n",
    "def armstrong():\n",
    "6\n",
    "  for num in range(lower,upper + 1):\n",
    "7\n",
    "   sum = 0\n",
    "8\n",
    "   temp = num\n",
    "9\n",
    "   while temp > 0:\n",
    "       digit = temp % 10\n",
    "11\n",
    "       sum += digit ** 3\n",
    "12\n",
    "       temp //= 10\n",
    "13\n",
    "   if num == sum:\n",
    "14\n",
    "       print(num)\n",
    "15\n",
    "# generator object  is x\n",
    "16\n",
    "x = armstrong()\n",
    "17\n",
    "print(x)\n",
    "18\n",
    "​\n",
    "19\n",
    " \n",
    "20\n",
    "​\n",
    "1\n",
    "​\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#ans 2:\n",
    "lower = int(input(\"Enter lower range: \"))\n",
    "upper = int(input(\"Enter upper range: \"))\n",
    "#generator function armstrong()\n",
    "def armstrong():\n",
    "  for num in range(lower,upper + 1):\n",
    "   sum = 0\n",
    "   temp = num\n",
    "   while temp > 0:\n",
    "       digit = temp % 10\n",
    "       sum += digit ** 3\n",
    "       temp //= 10\n",
    "   if num == sum:\n",
    "       print(num)\n",
    "# generator object  is x\n",
    "x = armstrong()\n",
    "print(x)\n",
    "next(x)\n"
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
