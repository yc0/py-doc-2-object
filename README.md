# py-doc-2-object
The tool is useful when you try to parse your test-cases written in DSL or in the form of documents. It can help you convert documents to objects of your specific languages

[![Generic badge](https://img.shields.io/badge/python-3.*-lightgrey.svg)](https://shields.io/)


## prerequisite
- it is composed by python 3
- currently, only support c++

## usage
`python3 convert.py <sub-cmd> "<context>"`

## type
### stringify

- example 1

`python3 convert.py stringify "['abc','abc']"`

- **result**

`{"abc","abc"}`
### charify

- example 1

`python3 convert.py charify "[a,b,c,d,e]"`

- **result**

`{'a','b','c','d'}`

- example 2

`python3 convert.py charify "[[a,b,c]],[d,e]]"

- **result**

`{{'a','b','c'}},{'d','e'}}`

### string

- example 1

`python3 convert.py string  "[               
[Apple, Apple],
[orange, banana, orange]
]"
`
- **result**

`{{"Apple","Apple"},{"orange","banana","orange"}}`
