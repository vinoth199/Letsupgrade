{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "3\n",
      "5\n",
      "7\n",
      "11\n",
      "13\n",
      "17\n",
      "19\n",
      "23\n",
      "29\n",
      "31\n",
      "37\n",
      "41\n",
      "43\n",
      "47\n",
      "53\n",
      "59\n",
      "61\n",
      "67\n",
      "71\n",
      "73\n",
      "79\n",
      "83\n",
      "89\n",
      "97\n",
      "101\n",
      "103\n",
      "107\n",
      "109\n",
      "113\n",
      "127\n",
      "131\n",
      "137\n",
      "139\n",
      "149\n",
      "151\n",
      "157\n",
      "163\n",
      "167\n",
      "173\n",
      "179\n",
      "181\n",
      "191\n",
      "193\n",
      "197\n",
      "199\n"
     ]
    }
   ],
   "source": [
    "up = 200\n",
    "lw = 1\n",
    "#lw = lower limit and up = upper limit\n",
    "for num in range(lw, up + 1):\n",
    "   # all prime numbers are greater than 1\n",
    "   if num > 1:\n",
    "       for i in range(2, num):\n",
    "           if (num % i) == 0:\n",
    "               break\n",
    "       else:\n",
    "           print(num)"
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
