{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5300a260",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<re.Match object; span=(8, 15), match='regular'>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "text = \"this is regular expression practice session.\"\n",
    "\n",
    "pattern = \"regular\"\n",
    "re.search(pattern, text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "3cff843b",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1995595099.py, line 14)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[22], line 14\u001b[1;36m\u001b[0m\n\u001b[1;33m    f = lambda x,y: print(text[i]) for i in range(8,15)\u001b[0m\n\u001b[1;37m                                   ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "def data(x):\n",
    "    return x * x\n",
    "\n",
    "print(data(5))\n",
    "\n",
    "get_square = lambda x: x*x\n",
    "print(get_square(55))\n",
    "# lambda argument(x): expression\n",
    "\n",
    "for i in range(8,15):\n",
    "    text[i]\n",
    "    print(text[i])\n",
    "\n",
    "f = lambda x,y: print(text[i]) for i in range(8,15)\n",
    "f(8,15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "753560b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "def get_squares(x):\n",
    "    return x**2\n",
    "f = lambda x: list(map(get_squares, range(x)))\n",
    "f(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "ec94e558",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2, 4, 6, 8]\n"
     ]
    }
   ],
   "source": [
    "d = list(filter(lambda x: x%2==0, [1,2,3,4,5,6,7,8]))\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "a187b02f",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "Generator expression must be parenthesized (3466296772.py, line 3)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[42], line 3\u001b[1;36m\u001b[0m\n\u001b[1;33m    print(list(map(print, lambda x:text[i] for i in range(8,15)))\u001b[0m\n\u001b[1;37m                          ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m Generator expression must be parenthesized\n"
     ]
    }
   ],
   "source": [
    "print(text)\n",
    "\n",
    "print(list(map(print, lambda x:text[i] for i in range(8,15)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "27d66d32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<re.Match object; span=(8, 15), match='regular'>\n",
      "(8, 15)\n",
      "8\n",
      "15\n",
      "['__class__', '__class_getitem__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span', 'start', 'string']\n"
     ]
    }
   ],
   "source": [
    "match = re.search(\"regular\", text)\n",
    "print(match)\n",
    "print(match.span())\n",
    "print(match.start())\n",
    "print(match.end())\n",
    "print(dir(match))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "2e039aa5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['text', 'text'] 2\n",
      "(4, 8)\n",
      "(28, 32)\n"
     ]
    }
   ],
   "source": [
    "text = \"new text is not same as old text\"\n",
    "\n",
    "matches = re.findall(\"text\", text)\n",
    "print(matches, len(matches))\n",
    "\n",
    "m = re.finditer(\"text\", text)\n",
    "for val in m:\n",
    "    print(val.span())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "id": "35ad15ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<re.Match object; span=(51, 60), match='12-234-23'>\n",
      "<re.Match object; span=(61, 69), match='ab-cd_ef'>\n",
      "<re.Match object; span=(70, 75), match='a b c'>\n",
      "<re.Match object; span=(29, 35), match='ext 12'>\n",
      "<re.Match object; span=(83, 88), match='aaa11'>\n",
      "['new', 'text', 'not', 'same', 'old', 'text', 'contact', '234', 'cd_ef', 'abc', 'aaa11']\n",
      "['new tex', 't is no', 't same ', 'as old ', '. +=@$#', ' contac', ' ab-cd_', 'ef a b ']\n",
      "['new tex', 't is no', 't same ', 'as old ', '. +=@$#', ' contac', ' ab-cd_', 'ef a b ']\n",
      "<re.Match object; span=(35, 39), match='. +='>\n",
      "<re.Match object; span=(35, 40), match='. +=@'>\n",
      "<re.Match object; span=(35, 43), match='. +=@$# '>\n",
      "<re.Match object; span=(4, 5), match='t'>\n",
      "<re.Match object; span=(4, 8), match='text'>\n",
      "<re.Match object; span=(16, 20), match='same'>\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "text = 'new text is not same as old text 12. +=@$# contact 12-234-23 ab-cd_ef a b c abc 44 aaa11'\n",
    "\n",
    "m = re.search(r\"\\d\\d-\\d\\d\\d-\\d\\d\", text) # \\d is numeric match\n",
    "print(m)\n",
    "m = re.search(r\"\\w\\w-\\w\\w_\\w\\w\", text) # \\w is alphanumeric match\n",
    "print(m)\n",
    "m = re.search(r\"a\\sb\\sc\", text) # \\s space\n",
    "print(m)\n",
    "m = re.search(r\"\\w\\w\\w\\s\\d\\d\", text)\n",
    "print(m)\n",
    "m = re.search(r\"\\w\\w\\w\\d\\d\", text)\n",
    "print(m)\n",
    "m = re.findall(r\"\\w\\w\\w+\", text) # + is one or more like previous\n",
    "print(m)\n",
    "m = re.findall(r\"\\D\\D\\D\\D\\D\\D\\D\", text) # \\D non digit\n",
    "print(m)\n",
    "m = re.findall(r\"\\D{7}\", text) # {n} occures exactly n number of times\n",
    "print(m)\n",
    "m = re.search(r\"\\W\\W\\W\\W\", text) # \\W non alphanumeric\n",
    "print(m)\n",
    "m = re.search(r\"\\W{3,5}\", text) # {a,b} occurs a to b times\n",
    "print(m)\n",
    "m = re.search(r\"\\W{3,}\", text) # {a,} occurs a or more times\n",
    "print(m)\n",
    "m = re.search(r\"ti*\", text) # * occures 0 or more times\n",
    "print(m)\n",
    "m = re.search(r\"texts?\", text) # ? occurs once or none times\n",
    "print(m)\n",
    "m = re.search(r\"same?\", text) # ? occurs once or none times\n",
    "print(m)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 142,
   "id": "8d361c35",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<re.Match object; span=(4, 7), match='cat'>"
      ]
     },
     "execution_count": 142,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.search(r\"cat|dog\", \"the cat is here\") # this is OR condition"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "id": "0e1fbb06",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['cat', 'hat', 'sat']"
      ]
     },
     "execution_count": 145,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r\".at\", \"the cat in a hat sat there.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 147,
   "id": "4d62fb88",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[' cat', ' hat', ' sat']"
      ]
     },
     "execution_count": 147,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r\"..at\", \"the cat in a hat sat there\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "id": "b8530232",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['e cat', 'a hat', 'splat']"
      ]
     },
     "execution_count": 151,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r\"...at\", \"the cat in a hat sat splat there\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "18e9c578",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<re.Match object; span=(0, 1), match='1'>"
      ]
     },
     "execution_count": 153,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.search(r\"^\\d\", \"1 is number\") # only matching at start"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "id": "a93d287e",
   "metadata": {},
   "outputs": [],
   "source": [
    "re.search(r\"^\\d\", \"The 1 is number\") # no match"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "id": "05218999",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<re.Match object; span=(16, 17), match='2'>"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.search(r\"\\d$\", \"1 is number and 2\") # match at end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "e603b8e1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['t',\n",
       " 'h',\n",
       " 'i',\n",
       " 's',\n",
       " ' ',\n",
       " 's',\n",
       " 't',\n",
       " 'a',\n",
       " 't',\n",
       " 'e',\n",
       " 'm',\n",
       " 'e',\n",
       " 'n',\n",
       " 't',\n",
       " ' ',\n",
       " 'h',\n",
       " 'a',\n",
       " 's',\n",
       " ' ',\n",
       " ' ',\n",
       " 'n',\n",
       " 'u',\n",
       " 'm',\n",
       " 'b',\n",
       " 'e',\n",
       " 'r',\n",
       " 's',\n",
       " ' ',\n",
       " ' ',\n",
       " 'a',\n",
       " 'n',\n",
       " 'd',\n",
       " ' ',\n",
       " ' ',\n",
       " 'i',\n",
       " 'n',\n",
       " ' ',\n",
       " 'i',\n",
       " 't',\n",
       " '.']"
      ]
     },
     "execution_count": 160,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'[^\\d]', \"this statement has 3 numbers 34 and 4 in it.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "78dc5da4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['this statement has ', ' numbers ', ' and ', ' in it.']"
      ]
     },
     "execution_count": 162,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'[^\\d]+', \"this statement has 3 numbers 34 and 4 in it.\") # + to get words together"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "id": "7de919da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['this statement has 3 numbers', ' 34 ', ' 4 in it']"
      ]
     },
     "execution_count": 170,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'[^.&!]+', \"this statement has 3 numbers! 34 & 4 in it.\") # this will exclude ! & . from statement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 172,
   "id": "c06bbea2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'this statement has 3 numbers 34  4 in it'"
      ]
     },
     "execution_count": 172,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "''.join(re.findall(r'[^.&!]+', \"this statement has 3 numbers! 34 & 4 in it.\")) # joining the above list with spaces"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 178,
   "id": "569ae7d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['state-ment', 'num-bers']"
      ]
     },
     "execution_count": 178,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'[\\w]+-[\\w]+', \"this state-ment has 3 num-bers! 34 & 4 in it.\") # search pattern"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 180,
   "id": "3c5e5b3a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['state-ment', 'num-bers']"
      ]
     },
     "execution_count": 180,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'\\w+-\\w+', \"this state-ment has 3 num-bers! 34 & 4 in it.\") # search pattern # another way"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 182,
   "id": "eb86b7e5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['fish', 'paw']"
      ]
     },
     "execution_count": 182,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "re.findall(r'cat(fish|pat|paw)', \"we have catfish has catclaw has catpaw who spend time on the tree.\") # this matches cat with fish / pat / paw to match with statement"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "id": "9e923cde",
   "metadata": {},
   "outputs": [],
   "source": [
    "import timeit\n",
    "\n",
    "def func():\n",
    "    for i in range(1,1000):\n",
    "        pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 198,
   "id": "48e07811",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "54.6 µs ± 5.99 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)\n"
     ]
    }
   ],
   "source": [
    "%%timeit \n",
    "func()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c992062",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
