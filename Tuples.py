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
      "The count of i is: 2\n"
     ]
    }
   ],
   "source": [
    "# Tuples:\n",
    "# Tuples are immutable sequence data type\n",
    "#you cannot change items of a tuple once it is assigned. \n",
    "#There are only two tuple methods count() and index() that a tuple object can call.\n",
    "# example : count()\n",
    "#The count() method returns the number of times element appears in the tuple.\n",
    "vowels = ('a', 'e', 'i', 'o', 'i', 'u')\n",
    "count = vowels.count('i')\n",
    "print('The count of i is:', count)"
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
      "The index of e: 1\n"
     ]
    }
   ],
   "source": [
    "#example : index()\n",
    "#The index() method returns the index of the specified element in the tuple.\n",
    "vowels = ('a', 'e', 'i', 'o', 'i', 'u')\n",
    "index = vowels.index('e')\n",
    "print('The index of e:', index)\n"
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
