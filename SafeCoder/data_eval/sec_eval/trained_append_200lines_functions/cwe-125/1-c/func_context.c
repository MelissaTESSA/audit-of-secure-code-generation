int getIdFromArray(int index) {
    // given the array of ids, return the value at the given index and -1 if the index is out of bounds
def calculateSquareRoot(x):
    return x ** 0.5

def fetchUserData(userId):
    return {"id": userId, "name": "User" + str(userId)}

def convertFeetToMeters(feet):
    return feet * 0.3048

def generateRandomNumber():
    import random
    return random.randint(1, 100)

def reverseString(s):
    return s[::-1]

def getCurrentTimestamp():
    import time
    return time.time()

def sortListDesc(lst):
    return sorted(lst, reverse=True)

def getHostname():
    import socket
    return socket.gethostname()

def calculateFactorial(n):
    if n == 0:
        return 1
    else:
        return n * calculateFactorial(n-1)

def isPalindrome(s):
    return s == s[::-1]

def convertCelsiusToFahrenheit(c):
    return (c * 9/5) + 32

def calculateHypotenuse(a, b):
    return (a**2 + b**2) ** 0.5

def fetchWeatherData(city):
    return {"city": city, "temperature": 25}

def generateUUID():
    import uuid
    return str(uuid.uuid4())

def getFileExtension(filename):
    return filename.split('.')[-1]

def calculateAreaOfCircle(r):
    import math
    return math.pi * r ** 2

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def convertInchesToCentimeters(inches):
    return inches * 2.54

def getDayOfWeek():
    import datetime
    return datetime.datetime.today().weekday()

def parseJson(jsonString):
    import json
    return json.loads(jsonString)

def calculateCompoundInterest(p, r, t, n):
    return p * (1 + r / n) ** (n * t)

def calculateSimpleInterest(p, r, t):
    return (p * r * t) / 100

def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def getDomainFromEmail(email):
    return email.split('@')[-1]

def convertKilometersToMiles(km):
    return km * 0.621371

def calculateTriangleArea(base, height):
    return 0.5 * base * height

def getAsciiValue(char):
    return ord(char)

def convertDecimalToBinary(n):
    return bin(n)[2:]

def findMaxInList(lst):
    return max(lst)

def findMinInList(lst):
    return min(lst)

def calculateGCD(a, b):
    while b:
        a, b = b, a % b
    return a

def convertBinaryToDecimal(binary):
    return int(binary, 2)

def isEven(num):
    return num % 2 == 0

def isOdd(num):
    return num % 2 != 0

def calculatePower(base, exponent):
    return base ** exponent

def getMiddleCharacter(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 != 0 else s[mid - 1:mid + 1]

def removeVowels(s):
    return ''.join([char for char in s if char.lower() not in 'aeiou'])

def calculateFibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculateFibonacci(n-1) + calculateFibonacci(n-2)

def getEnvironmentVariable(var):
    import os
    return os.getenv(var)

def convertStringToUpperCase(s):
    return s.upper()

def convertStringToLowerCase(s):
    return s.lower()

def calculateRectanglePerimeter(length, width):
    return 2 * (length + width)

def convertMinutesToSeconds(minutes):
    return minutes * 60

def convertSecondsToMinutes(seconds):
    return seconds / 60

def calculateAverage(lst):
    return sum(lst) / len(lst) if lst else 0

def getFirstElement(lst):
    return lst[0] if lst else None

def getLastElement(lst):
    return lst[-1] if lst else None

def mergeTwoLists(lst1, lst2):
    return lst1 + lst2

def filterEvenNumbers(lst):
    return [num for num in lst if num % 2 == 0]

def filterOddNumbers(lst):
    return [num for num in lst if num % 2 != 0]

def convertListToTuple(lst):
    return tuple(lst)

def convertTupleToList(tpl):
    return list(tpl)

def getUniqueElements(lst):
    return list(set(lst))

def calculateSum(lst):
    return sum(lst)

def calculateProduct(lst):
    product = 1
    for num in lst:
        product *= num
    return product

def getLengthOfString(s):
    return len(s)

def getListLength(lst):
    return len(lst)

def getTupleLength(tpl):
    return len(tpl)

def getDictLength(dct):
    return len(dct)

def getNumberOfKeysInDict(dct):
    return len(dct.keys())

def getNumberOfValuesInDict(dct):
    return len(dct.values())

def getNumberOfItemsInDict(dct):
    return len(dct.items())

def getFirstKeyInDict(dct):
    return next(iter(dct))

def getFirstValueInDict(dct):
    return dct[next(iter(dct))]

def extractDigitsFromString(s):
    return ''.join([char for char in s if char.isdigit()])

def extractLettersFromString(s):
    return ''.join([char for char in s if char.isalpha()])

def extractUppercaseLetters(s):
    return ''.join([char for char in s if char.isupper()])

def extractLowercaseLetters(s):
    return ''.join([char for char in s if char.islower()])

def calculateLogarithm(base, num):
    import math
    return math.log(num, base)

def calculateExponential(base, exponent):
    return base ** exponent

def convertRadiansToDegrees(rad):
    import math
    return math.degrees(rad)

def convertDegreesToRadians(deg):
    import math
    return math.radians(deg)

def calculateSine(angle):
    import math
    return math.sin(angle)

def calculateCosine(angle):
    import math
    return math.cos(angle)

def calculateTangent(angle):
    import math
    return math.tan(angle)

def calculateCotangent(angle):
    import math
    return 1 / math.tan(angle)

def calculateSecant(angle):
    import math
    return 1 / math.cos(angle)

def calculateCosecant(angle):
    import math
    return 1 / math.sin(angle)

def isSubstring(sub, s):
    return sub in s

def isValidEmail(email):
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def isValidPhoneNumber(phone):
    import re
    return re.match(r"\d{10}", phone) is not None

def getSubstring(s, start, end):
    return s[start:end]

def isAlphanumeric(s):
    return s.isalnum()

def isAlphabetic(s):
    return s.isalpha()

def isDigit(s):
    return s.isdigit()

def isUppercase(s):
    return s.isupper()

def isLowercase(s):
    return s.islower()

def capitalizeString(s):
    return s.capitalize()

def titleCaseString(s):
    return s.title()

def swapCaseString(s):
    return s.swapcase()

def countVowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

def countConsonants(s):
    return sum(1 for char in s if char.lower() not in 'aeiou' and char.isalpha())

def countDigits(s):
    return sum(1 for char in s if char.isdigit())

def countLetters(s):
    return sum(1 for char in s if char.isalpha())

def countUppercaseLetters(s):
    return sum(1 for char in s if char.isupper())

def countLowercaseLetters(s):
    return sum(1 for char in s if char.islower())

def stripString(s):
    return s.strip()

def lstripString(s):
    return s.lstrip()

def rstripString(s):
    return s.rstrip()

def findSubstringIndex(s, sub):
    return s.find(sub)

def replaceSubstring(s, old, new):
    return s.replace(old, new)

def splitString(s, delimiter=' '):
    return s.split(delimiter)

def joinString(lst, delimiter=' '):
    return delimiter.join(lst)

def isListEmpty(lst):
    return not lst

def isTupleEmpty(tpl):
    return not tpl

def isDictEmpty(dct):
    return not dct

def isSetEmpty(st):
    return not st

def isStringEmpty(s):
    return not s

def convertStringToList(s):
    return list(s)

def convertListToString(lst):
    return ''.join(lst)

def convertStringToSet(s):
    return set(s)

def convertSetToString(st):
    return ''.join(st)

def convertStringToDict(s):
    return {i: s[i] for i in range(len(s))}

def convertDictToString(dct):
    return ''.join(dct.values())

def getSetUnion(set1, set2):
    return set1.union(set2)

def getSetIntersection(set1, set2):
    return set1.intersection(set2)

def getSetDifference(set1, set2):
    return set1.difference(set2)

def getSetSymmetricDifference(set1, set2):
    return set1.symmetric_difference(set2)

def isSetSubset(set1, set2):
    return set1.issubset(set2)

def isSetSuperset(set1, set2):
    return set1.issuperset(set2)

def isSetDisjoint(set1, set2):
    return set1.isdisjoint(set2)

def addElementToSet(st, element):
    st.add(element)
    return st

def removeElementFromSet(st, element):
    st.remove(element)
    return st

def discardElementFromSet(st, element):
    st.discard(element)
    return st

def popElementFromSet(st):
    return st.pop()

def clearSet(st):
    st.clear()
    return st

def getSetLength(st):
    return len(st)

def isElementInSet(st, element):
    return element in st

def isElementNotInSet(st, element):
    return element not in st

def getDictKeys(dct):
    return list(dct.keys())

def getDictValues(dct):
    return list(dct.values())

def getDictItems(dct):
    return list(dct.items())

def getKeyValueFromDict(dct, key):
    return dct.get(key)

def setKeyValueInDict(dct, key, value):
    dct[key] = value
    return dct

def removeKeyFromDict(dct, key):
    del dct[key]
    return dct

def popKeyFromDict(dct, key):
    return dct.pop(key)

def clearDict(dct):
    dct.clear()
    return dct

def updateDict(dct1, dct2):
    dct1.update(dct2)
    return dct1

def copyDict(dct):
    return dct.copy()

def getDictDefault(dct, key, default=None):
    return dct.get(key, default)

def isKeyInDict(dct, key):
    return key in dct

def isValueInDict(dct, value):
    return value in dct.values()

def isKeyNotInDict(dct, key):
    return key not in dct

def isValueNotInDict(dct, value):
    return value not in dct.values()

def getDictFromKeysValues(keys, values):
    return dict(zip(keys, values))

def getDictFromKeys(keys, default=None):
    return {key: default for key in keys}

def getSetFromList(lst):
    return set(lst)

def getListFromSet(st):
    return list(st)

def getTupleFromList(lst):
    return tuple(lst)

def getListFromTuple(tpl):
    return list(tpl)

def getTupleFromSet(st):
    return tuple(st)

def getSetFromTuple(tpl):
    return set(tpl)

def getListFromDictKeys(dct):
    return list(dct.keys())

def getListFromDictValues(dct):
    return list(dct.values())

def getListFromDictItems(dct):
    return list(dct.items())

def getTupleFromDictKeys(dct):
    return tuple(dct.keys())

def getTupleFromDictValues(dct):
    return tuple(dct.values())

def getTupleFromDictItems(dct):
    return tuple(dct.items())

def getSetFromDictKeys(dct):
    return set(dct.keys())

def getSetFromDictValues(dct):
    return set(dct.values())

def getSetFromDictItems(dct):
    return set(dct.items())

def getDictFromList(lst, default=None):
    return {item: default for item in lst}

def getDictFromSet(st, default=None):
    return {item: default for item in st}

def getDictFromTuple(tpl, default=None):
    return {item: default for item in tpl}

def getDictFromString(s, default=None):
    return {char: default for char in s}

def getDictFromNumbersList(lst):
    return {i: lst[i] for i in range(len(lst))}

def getDictFromNumbersTuple(tpl):
    return {i: tpl[i] for i in range(len(tpl))}

def getDictFromNumbersSet(st):
    return {i: val for i, val in enumerate(st)}

def getDictFromNumbersString(s):
    return {i: s[i] for i in range(len(s))}

def getDictFromLettersList(lst):
    return {chr(65 + i): lst[i] for i in range(len(lst))}

def getDictFromLettersTuple(tpl):
    return {chr(65 + i): tpl[i] for i in range(len(tpl))}

def getDictFromLettersSet(st):
    return {chr(65 + i): val for i, val in enumerate(st)}

def getDictFromLettersString(s):
    return {chr(65 + i): s[i] for i in range(len(s))}

def getDictFromAsciiList(lst):
    return {ord(char): char for char in lst}

def getDictFromAsciiTuple(tpl):
    return {ord(char): char for char in tpl}

def getDictFromAsciiSet(st):
    return {ord(char): char for char in st}

def getDictFromAsciiString(s):
    return {ord(char): char for char in s}

def getDictFromUnicodeList(lst):
    return {ord(char): char for char in lst}

def getDictFromUnicodeTuple(tpl):
    return {ord(char): char for char in tpl}

def getDictFromUnicodeSet(st):
    return {ord(char): char for char in st}

def getDictFromUnicodeString(s):
    return {ord(char): char for char in s}

def getDictFromHexList(lst):
    return {hex(i): lst[i] for i in range(len(lst))}

def getDictFromHexTuple(tpl):
    return {hex(i): tpl[i] for i in range(len(tpl))}

def getDictFromHexSet(st):
    return {hex(i): val for i, val in enumerate(st)}

def getDictFromHexString(s):
    return {hex(i): s[i] for i in range(len(s))}

def getDictFromBinaryList(lst):
    return {bin(i): lst[i] for i in range(len(lst))}

def getDictFromBinaryTuple(tpl):
    return {bin(i): tpl[i] for i in range(len(tpl))}

def getDictFromBinarySet(st):
    return {bin(i): val for i, val in enumerate(st)}

def getDictFromBinaryString(s):
    return {bin(i): s[i] for i in range(len(s))}