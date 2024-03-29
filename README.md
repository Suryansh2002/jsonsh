# jsonsh

Disclaimer : This is slow and not recommended for use, 
Use a database.

As of now annotations of this is really messed up and typing doesn't go well.

Installing
----------

```sh
pip install -U jsonsh
```

if you are on Unix-like system, The performace can be increased by installing uvloop !
```sh
pip install -U uvloop
```

What is this !
-----------
This is a silly package , that uses pydantic to store data in different json files.

Data Fetched is in pydantic Model , which can be converted to dict using dict().

All examples below have data returned as a Pydantic Model !

Usage
------

### Base Example 


```py
import asyncio
from jsonsh import Template,Instance

instance = Instance("Data") #this is your data folder

@instance.register
class Test(Template):
    id:int
    age:int
    name:str

async def main():
    idk = Test(id = 10,age = 13,name = "hello")
    await idk.save() #this saves the file in your current working directory

asyncio.run(main())
```

### Finding and Updating Data

There are no advanced queries yet but you can find by id or particular value


```py
import asyncio
from jsonsh import Template,Instance

instance = Instance("Data")

@instance.register
class Test(Template):
    id:int
    age:int
    name:str

async def main():
    data = await Test.find_one(id = 10)
    print(data) #prints the data we found
    data.name = "Unknown" #changing name
    await data.save() #updating data

asyncio.run(main())
```

### Finding Multiple Data


```py
import asyncio
from jsonsh import Template,Instance

instance = Instance("Data")

@instance.register
class Test(Template):
    id:int
    age:int
    name:str

async def main():
    data = await Test.find_many(age = 10) #finding all dict with age as 10
    print(data) #prints the lists of multiple dicts

asyncio.run(main())
```

## Using Indexing 

```py
import asyncio
from jsonsh import Template,Instance

instance = Instance("Data")

@instance.register
class Test(Template):
    id:int
    age:int
    name:str

    class Meta:
        indexes = ["age","name"] 
    """
    this makes finding by age and name faster
    """

async def main():
    data = await Test.find_many(age = 10) #finding all dict with age as 10
    print(data) #prints the lists of multiple dicts

asyncio.run(main())
```

## Deleting files / entries

```py
import asyncio
from jsonsh import Template,Instance

instance = Instance("Data")

@instance.register
class Test(Template):
    id:int
    age:int
    name:str

    class Meta:
        indexes = ["age","name"] 
    """
    this makes finding by age and name faster
    """

async def main():
    data = await Test.delete_one(age = 10) #deleting a file entry with age as 10
    data = await Test.delete_one(id = 10) #deleting a file entry with id as 10
    print(data) #prints the lists of multiple dicts

asyncio.run(main())
```

#### Simple Caching 

```py

from jsonsh import Template,Instance

instance = Instance("Data",cache_state = True,capacity = 100) #this helps you to avoid reading files in finds

```
