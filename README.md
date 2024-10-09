# englishvoc

A RDF-based vocabulary to model English into RDF. English documents can thus be represented, queried, generated, validated, analysed, transformed and reused as semantic objects themselves.

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
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix english: <https://www.english.org/model/def/>

example:Document
  a english:Document ;
  rdf:_1 example:ExampleSentence .

example:ExampleSentence
  a english:Sentence ;
  rdf:_1 example:NounPhrase_1 ;
  rdf:_2 example:VerbPhrase_1 .

example:NounPhrase_1
  a english:NounPhrase ;
  rdf:_1 example:Determiner_1 ;
  rdf:_2 example:TerminalNode_1 ;
  rdf:_3 example:Noun_1 .

example:Determiner_1
  a english:Determiner ;
  english:fragment "The" .

example:TerminalNode_1
  a english:TerminalNode ;
  english:fragment "big" .

example:Noun_1
  a english:Noun ;
  english:fragment "dog" .

example:VerbPhrase_1
  a english:VerbPhrase ;
  rdf:_1 example:Verb_1 ;
  rdf:_2 example:PrepositionalPhrase_1 .

example:Verb_1
  a english:Verb ;
  english:fragment "runs" .

example:PrepositionalPhrase_1
  a english:PrepositionalPhrase ;
  rdf:_1 example:Preposition_1 ;
  rdf:_2 example:NounPhrase_2 .

example:Preposition_1
  a english:Preposition ;
  english:fragment "in" .

example:NounPhrase_2
  a english:NounPhrase ;
  rdf:_1 example:Determiner_2 ;
  rdf:_2 example:Noun_2 .

example:Determiner_2
  a english:Determiner ;
  english:fragment "the" .

example:Noun_2
  a english:Noun ;
  english:fragment "park" .

``` 
 