
import pickle
# writing to a file
example_dict = {1: "6", 2: "2", 3: "f"}
file_out = open("dict.pickle", "wb")
pickle.dump(example_dict, file_out)
file_out.close()

# reading from a file
file_in = open("dict.pickle", "rb")
example_dict = pickle.load(file_in)
file_in.close()

# writing to a file using a context manager (to be studied at Python Intermediate)
example_dict = {1: "6", 2: "2", 3: "f"}
with open("dict.pickle", "wb") as file_out:
    pickle.dump(example_dict, file_out)

# reading from a file using a context manager (to be studied at Python Intermediate)
with open("dict.pickle", "rb") as file_in:
    example_dict = pickle.load(file_in)
