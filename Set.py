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
      "Vowels are: {'i', 'o', 'a', 'e', 'u'}\n"
     ]
    }
   ],
   "source": [
    "#A set is an unordered collection of items.\n",
    "#Set items are unique and immutable.  \n",
    "#methods:\n",
    "#The set add() method adds a given element to a set. If the element is already present, it doesn't add any element.\n",
    "vowels = {'a', 'e', 'i', 'u'}\n",
    "vowels.add('o')\n",
    "print('Vowels are:', vowels)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The frozen set is: frozenset({'sex', 'age', 'name'})\n"
     ]
    }
   ],
   "source": [
    "#The frozenset() function returns an immutable frozenset object initialized with elements from the given iterable.\n",
    "person = {\"name\": \"John\", \"age\": 23, \"sex\": \"male\"}\n",
    "\n",
    "fSet = frozenset(person)\n",
    "print('The frozen set is:', fSet)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "#The issubset() method returns True if all elements of a set are present in another set (passed as an argument). If not, it returns False.\n",
    "A = {1, 2, 3}\n",
    "B = {1, 2, 3, 4, 5}\n",
    "C = {1, 2, 4, 5}\n",
    "print(A.issubset(B))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "#The issuperset() method returns True if a set has every elements of another set (passed as an argument). If not, it returns False.\n",
    "A = {1, 2, 3, 4, 5}\n",
    "B = {1, 2, 3}\n",
    "C = {1, 2, 3}\n",
    "print(B.issuperset(A))"
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
