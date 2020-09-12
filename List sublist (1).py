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
      "enter the no of element :8\n",
      "1\n",
      "5\n",
      "6\n",
      "4\n",
      "1\n",
      "2\n",
      "3\n",
      "5\n",
      "it's a Match\n"
     ]
    }
   ],
   "source": [
    "#ans 1:\n",
    "lst=[]\n",
    "n = int(input(\"enter the no of element :\"))\n",
    "for i in range(0,n):\n",
    "\tele=int(input())\n",
    "lst.append(ele)\n",
    "sub = [1,1,5]\n",
    "if (set(lst).issubset(set(sub))):\n",
    "\t print(\"it's a Match\")\n",
    "else:\n",
    "\t print(\"it's gone\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the no of element :8\n",
      "1\n",
      "5\n",
      "6\n",
      "5\n",
      "1\n",
      "2\n",
      "3\n",
      "6\n",
      "it's gone\n"
     ]
    }
   ],
   "source": [
    "lst=[]\n",
    "n = int(input(\"enter the no of element :\"))\n",
    "for i in range(0,n):\n",
    "\tele=int(input())\n",
    "lst.append(ele)\n",
    "sub = [1,1,5]\n",
    "if (set(lst).issubset(set(sub))):\n",
    "\t print(\"it's a Match\")\n",
    "else:\n",
    "\t print(\"it's gone\")\n"
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
