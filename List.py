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
      "hai\n"
     ]
    }
   ],
   "source": [
    "print (\"hai\")"
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
      "['Mathematics', 'chemistry', 1997, 2000, 20544]\n"
     ]
    }
   ],
   "source": [
    "#A list is a data structure in Python that is a mutable\n",
    "#List methods in Python:\n",
    "#append(): Used for appending and adding elements to List.It is used to add elements to the last position of List.\n",
    "List = ['Mathematics', 'chemistry', 1997, 2000] \n",
    "\n",
    "List.append(20544) \n",
    "\n",
    "print(List)"
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
      "['Mathematics', 'chemistry', 10087, 1997, 2000]\n"
     ]
    }
   ],
   "source": [
    "#insert(): Inserts an elements at specified position\n",
    "List = ['Mathematics', 'chemistry', 1997, 2000] \n",
    "# Insert at index 2 value  \n",
    "\n",
    "List.insert(2,10087)      \n",
    "\n",
    "print(List)     "
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
      "[1, 2, 3, 2, 3, 4, 5]\n",
      "[2, 3, 4, 5, 1, 2, 3, 2, 3, 4, 5]\n"
     ]
    }
   ],
   "source": [
    "#extend(): Adds contents to List2 to the end of List1.\n",
    "List1 = [1, 2, 3] \n",
    "\n",
    "List2 = [2, 3, 4, 5] \n",
    "\n",
    "  \n",
    "# Add List2 to List1 \n",
    "List1.extend(List2)         \n",
    "\n",
    "print(List1) \n",
    "\n",
    "  \n",
    "# Add List1 to List2 now \n",
    "List2.extend(List1)  \n",
    "\n",
    "print(List2) "
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
      "15\n"
     ]
    }
   ],
   "source": [
    "#sum() : Calculates sum of all the elements of List\n",
    "List = [1, 2, 3, 4, 5] \n",
    "\n",
    "print(sum(List)) "
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
  "celltoolbar": "Raw Cell Format",
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
