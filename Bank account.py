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
      "Enter owner name : Vinoth\n",
      "Hello Vinoth\n",
      "Balance : 0.0\n",
      "Enter amount to be Deposited: 358923\n",
      "\n",
      " Amount Deposited: 358923.0\n",
      "Enter amount to be Withdrawn: 37989\n",
      "\n",
      " You Withdrew: 37989.0\n",
      "\n",
      " Net Available Balance= 320934.0\n"
     ]
    }
   ],
   "source": [
    "#Bank account :\n",
    "class Bank_Account: \n",
    "\n",
    "    def __init__(self): \n",
    "\n",
    "        self.balance=0.00\n",
    "        name=input(\"Enter owner name : \")\n",
    "        print(\"Hello\",name) \n",
    "        print(\"Balance :\",self.balance)\n",
    "  \n",
    "\n",
    "    def deposit(self): \n",
    "\n",
    "        amount=float(input(\"Enter amount to be Deposited: \")) \n",
    "\n",
    "        self.balance += amount \n",
    "\n",
    "        print(\"\\n Amount Deposited:\",amount) \n",
    "\n",
    "  \n",
    "\n",
    "    def withdraw(self): \n",
    "\n",
    "        amount = float(input(\"Enter amount to be Withdrawn: \")) \n",
    "\n",
    "        if self.balance>=amount: \n",
    "\n",
    "            self.balance-=amount \n",
    "\n",
    "            print(\"\\n You Withdrew:\", amount) \n",
    "\n",
    "        else: \n",
    "\n",
    "            print(\"\\n Insufficient balance  \") \n",
    "\n",
    "  \n",
    "\n",
    "    def display(self): \n",
    "\n",
    "        print(\"\\n Net Available Balance=\",self.balance) \n",
    "\n",
    "s = Bank_Account() \n",
    "s.deposit() \n",
    "s.withdraw() \n",
    "s.display()"
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
