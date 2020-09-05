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
      "Lowercase string: python is awesome\n"
     ]
    }
   ],
   "source": [
    "#A string is a sequence of characters enclosed in quotation marks. \n",
    "#methods:\n",
    "#The casefold() method is an aggressive lower() method which converts strings to case folded strings for caseless matching.\n",
    "string = \"PYTHON IS AWESOME\"\n",
    "print(\"Lowercase string:\", string.casefold())"
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
      "Centered String:     Python is awesome    \n"
     ]
    }
   ],
   "source": [
    "#The center() method returns a string which is padded with the specified character.\n",
    "string = \"Python is awesome\"\n",
    "\n",
    "new_string = string.center(24)\n",
    "\n",
    "print(\"Centered String: \", new_string)"
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
      "The count is: 2\n"
     ]
    }
   ],
   "source": [
    "#The string count() method returns the number of occurrences of a substring in the given string.\n",
    "string = \"Python is awesome, isn't it?\"\n",
    "substring = \"is\"\n",
    "count = string.count(substring)\n",
    "print(\"The count is:\", count)"
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
      "False\n"
     ]
    }
   ],
   "source": [
    "#The endswith() method returns True if a string ends with the specified suffix. If not, it returns False.\n",
    "text = \"Python is easy to learn.\"\n",
    "result = text.endswith('to learn')\n",
    "print(result)"
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
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "#The isalpha() method returns True if all characters in the string are alphabets. If not, it returns False.\n",
    "name = \"Monica\"\n",
    "print(name.isalpha())\n",
    "name = \"Monica Geller\"\n",
    "print(name.isalpha())"
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
