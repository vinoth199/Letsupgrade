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
      "d = {}\n"
     ]
    }
   ],
   "source": [
    "#Dictionary in Python is an unordered collection of data values, used to store data values like a map, \n",
    "#unlike other Data Types that hold only single value as an element, Dictionary holds (key : value )pair.\n",
    "#METHODS:\n",
    "#clear() = The clear() method removes all items from the dictionary.\n",
    "d = {1: \"one\", 2: \"two\"}\n",
    "\n",
    "d.clear()\n",
    "print('d =', d)"
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
      "Orignal:  {1: 'one', 2: 'two'}\n",
      "New:  {1: 'one', 2: 'two'}\n"
     ]
    }
   ],
   "source": [
    "#copy()=They copy() method returns a shallow copy of the dictionary\n",
    "original = {1:'one', 2:'two'}\n",
    "new = original.copy()\n",
    "\n",
    "print('Orignal: ', original)\n",
    "print('New: ', new)"
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
      "dict_items([('apple', 2), ('orange', 3), ('grapes', 4)])\n"
     ]
    }
   ],
   "source": [
    "#item()= The items() method returns a view object that displays a list of dictionary's (key, value) tuple pairs.\n",
    "sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }\n",
    "\n",
    "print(sales.items())"
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
      "The popped element is: 2\n",
      "The dictionary is: {'orange': 3, 'grapes': 4}\n"
     ]
    }
   ],
   "source": [
    "#pop()= The pop() method removes and returns an element from a dictionary having the given key.\n",
    "sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }\n",
    "\n",
    "element = sales.pop('apple')\n",
    "print('The popped element is:', element)\n",
    "print('The dictionary is:', sales)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1: 'one', 2: 'two'}\n"
     ]
    }
   ],
   "source": [
    "#The update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.\n",
    "d = {1: \"one\", 2: \"three\"}\n",
    "d1 = {2: \"two\"}\n",
    "d.update(d1)\n",
    "print(d)"
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
