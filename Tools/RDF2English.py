# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 18:40:53 2023

@author: Flores Bakker

The english Vocabulary.

Usage: 

1. Place an arbitrary ontology (as turtle file *.ttl) in the input folder.
2. In the command prompt, run 'python englishvoc.py'
3. Go to the output folder and grab your enriched turtle file, now including english fragments.


"""
import os
import pyshacl
import rdflib 
from rdflib import Namespace

# Get the current working directory in which the RDF2english.py file is located.
current_dir = os.getcwd()

# Set the path to the desired standard directory. 
directory_path = os.path.abspath(os.path.join(current_dir, '..'))

# namespace declaration
english = Namespace("https://www.english.org/model/def/")

# Function to read a graph (as a string) from a file 
def readGraphFromFile(file_path):
    # Open each file in read mode
    with open(file_path, 'r', encoding='utf-8') as file:
            # Read the content of the file and append it to the existing string
            file_content = file.read()
    return file_content

# Function to write a graph to a file
def writeGraph(graph):
    graph.serialize(destination=directory_path+"/englishvoc/Tools/Output/"+filename_stem+"-english.ttl", format="turtle")

# Function to call the PyShacl engine so that a RDF model of an english script can be serialized to english code.
def iteratePyShacl(english_generator, serializable_graph):
        
        # call PyShacl engine and apply the english vocabulary to the serializable english model
        pyshacl.validate(
        data_graph=serializable_graph,
        shacl_graph=english_generator,
        data_graph_format="turtle",
        shacl_graph_format="turtle",
        advanced=True,
        inplace=True,
        inference=None,
        iterate_rules=False, #rather than setting this to true, it is better to do the iteration in the script as PyShacl seems to have some buggy behavior around iteration.
        debug=False,
        )
        
       
        statusquery = serializable_graph.query('''
            
prefix english: <https://www.english.org/model/def/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

ASK
WHERE 
  # 
  {
  ?script rdf:type english:Document;
        english:fragment [].
}
        ''')   

        resultquery = serializable_graph.query('''
            
prefix english: <https://www.english.org/model/def/>
prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?english_fragment
WHERE {
  ?script rdf:type english:Document;
         english:fragment ?english_fragment.
  
}

        ''')   

        # Check whether another iteration is needed. If every OWL and RDFS construct contains a english:syntax statement, the processing is considered done.
        for status in statusquery:
            print ('status = ', status)
            if status == False:
                writeGraph(serializable_graph)
                iteratePyShacl(english_generator, serializable_graph)
            else: 
                 print ("File " + filename_stem+"-english.ttl" + " created in output folder.")
                 writeGraph(serializable_graph)
        
                 for result in resultquery:
                    english_fragment = result["english_fragment"]
                    output_file_path = directory_path+"/englishvoc/Tools/Output/"+filename_stem+".py"
                    
                    # Write the english content to the output file
                    with open(output_file_path, "w", encoding="utf-8") as file:
                        file.write(english_fragment)
                    print ("File " + filename_stem+".rq" + " created in output folder.")

                 
# loop through any turtle files in the input directory
for filename in os.listdir(directory_path+"/englishvoc/Tools/Input"):
    if filename.endswith(".ttl"):
        file_path = os.path.join(directory_path+"/englishvoc/Tools/Input", filename)
        
        # Establish the stem of the file name for reuse in newly created files
        filename_stem = os.path.splitext(filename)[0]
        
        # Get the english vocabulary and place it in a string
        english_generator = readGraphFromFile(directory_path+"/englishvoc/Specification/englishvoc - core.ttl")
        
        # Get some english code represented in triples
        english_script_string = readGraphFromFile(file_path) + english_generator
        
        # Create a graph
        serializable_graph = rdflib.Graph().parse(data=english_script_string , format="ttl")
        serializable_graph.bind("english", english)
                        
        # Inform user
        print ('\nCreating english fragments for file',filename, '...')
        
        # Call the shacl engine with the english vocabulary
        iteratePyShacl(english_generator, serializable_graph)
        
        # Inform user
        print ('Done.')
