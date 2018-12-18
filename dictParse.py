from lib.mapper import Mapper
from os import path

# Grab words file
abbrevMap = path.join("resources","dictParse","abbreviations.json")

# Parse words file, following are notes
## Modify to remove abbreviations
### 1. Check mapper file when s*. is found
### 2. Stop and request user to provide mapping when not found
### 3. Append to mapper file
mapGenders = r"\{\S\}"
dictString = "{m}"

mapperBot = Mapper(abbrevMap,dictString,mapWord)
print(mapperBot.map())

## Parse dictionary to json
### 1. German :: English
### 2. German {[f,m,n,pl]} --> die/der/das/plural die German
### 3. German1 | German2 :: English1 English2
### 4. German (comment) :: English (comment)
### 5. German [note] :: English [note]

# Save words down as json