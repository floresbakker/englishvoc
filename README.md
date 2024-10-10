# englishvoc

A RDF-based vocabulary to model the English language into RDF. English documents can thus be represented, queried, generated, validated, analysed, transformed and reused as semantic objects themselves.

# Abstract



# Description



# Introduction



# Background



# Objective



# Audience



# Status

Unstable & unfinished. Work in progress.

# Example - "The big dog runs in the park"

Take for example the following sentence:

```
The big dog runs in the park
```

This can be modeled in RDF using the English Vocabulary:

```
prefix example: <https://example.org/english/>
prefix rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix english: <https://www.english.org/model/def/>

example:Document
  a english:Document ;
  rdf:_1 example:ExampleSentence .

example:ExampleSentence
  a english:Sentence ;
  rdf:_1 example:The_big_dog ;
  rdf:_2 example:runs_in_the_park .

example:The_big_dog
  a english:NounPhrase ;
  rdf:_1 example:The ;
  rdf:_2 example:big ;
  rdf:_3 example:dog .

example:The
  a english:Determiner ;
  english:fragment "The" .

example:big
  a english:Adjective ;
  english:fragment "big" .

example:dog
  a english:Noun ;
  english:fragment "dog" .

example:runs_in_the_park
  a english:VerbPhrase ;
  rdf:_1 example:runs ;
  rdf:_2 example:in_the_park .

example:runs
  a english:Verb ;
  english:fragment "runs" .

example:in_the_park
  a english:PrepositionalPhrase ;
  rdf:_1 example:in ;
  rdf:_2 example:the_park .

example:in
  a english:Preposition ;
  english:fragment "in" .

example:the_park
  a english:NounPhrase ;
  rdf:_1 example:the ;
  rdf:_2 example:park .

example:the
  a english:Determiner ;
  english:fragment "the" .

example:park
  a english:Noun ;
  english:fragment "park" .

``` 
 