import json
import pickle
import numpy as np
#global variables
__locations = None
__data_columns = None
__model = None

# function which can return us an estimated price for the given  location, BHK,sqrtfoot area and bathroom


def get_estimated_price(location, sqft, bhk, bath):
    try:  # the behaviour of puthon list method is that if the element is not found it throws  an error so
        # we r using try and except and id it cannot find the index we initialize it to -1
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    print(type(__data_columns))
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)
# in order to retun the price we have to do is we have a model in which we r going to call a predict model
# we all know that when we have sklearn saved model we can call a predict method which will take an input which
# is X then for that given input it shoul return the output which is estimated price the input which it will take
# is a 2 dimentional array and we r going to create a numpy array will call it x and for that x we will wrap it up
# into the array so that it become two dimentional array


def get_location_names():
    # function
    fun()
    return __locations  # returns the location name


def load_saved_artifacts():  # load_saved_artifacts is a function and this method will load the saved artifacts which
    # is my columns json and pickel
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    with open("./artifacts/columns.json", 'r') as f:  # reading the file
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

        # calling json file with this method
# what ever object is loaded will be converted into a dictionary on which we can call data column key that will
# return us data column and out of all those data column starting with column No. 3 r our locations
# we can use index slising to get element from the list starting with No. 3
    global __model
    with open("./artifacts/Bengaluru_House_Data_model.pickle", 'rb') as f:
        __model = pickle.load(f)
        # doing same for pickle and loading the moedl into __model

    print("loading saved artifacts ....done")


def fun():
    load_saved_artifacts()
    print(get_estimated_price('1st Phase Jp Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase Jp Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 3, 3))
