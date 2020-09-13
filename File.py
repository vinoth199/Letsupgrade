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
      "<_io.TextIOWrapper name='test.dat' mode='w' encoding='UTF-8'>\n",
      "Now is the time to close the file\n",
      "Enter a file name: Trag.png\n",
      "There is no file named Trag.png\n"
     ]
    }
   ],
   "source": [
    "#ans 2\n",
    "f = open(\"test.dat\",\"w\") \n",
    "f.write(\"Now is the time\") \n",
    "f.write(\" to close the file\")\n",
    "print(f) \n",
    "f.close()\n",
    "f = open(\"test.dat\",\"r\") \n",
    "text = f.read() \n",
    "print (text )\n",
    "filename = input('Enter a file name: ') \n",
    "try: \n",
    "  f = open (filename, \"r\") \n",
    "except IOError: \n",
    "  print( 'There is no file named', filename )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
