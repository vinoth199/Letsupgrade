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
      "Enter the lower value :100\n",
      " Enter the upper value :200\n",
      "153\n"
     ]
    }
   ],
   "source": [
    "#program for find first armstrong number between range using while loop\n",
    "#Answer:\n",
    "lower=int(input(\"Enter the lower value :\"))\n",
    "upper=int(input(\" Enter the upper value :\"))\n",
    "for num in range(lower, upper + 1):\n",
    "   order = len(str(num))\n",
    "   sum = 0\n",
    "   temp = num\n",
    "   while temp > 0:\n",
    "       digit = temp % 10\n",
    "       sum += digit ** order\n",
    "       temp //= 10\n",
    "\n",
    "   if num == sum:\n",
    "       print(num)\n",
    "       exit();"
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
