import sys

query = sys.argv[1]

print(query)

from langchain.document_loaders import TextLoader
loader = TextLoader('data.txt')

from langchain.indexes import VectorstoreIndexCreator
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query))