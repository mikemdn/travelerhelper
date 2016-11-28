import os
import pickle

profile_filename = "profiles"

# Gestion des scores


def get_profiles():
    """This functions returns the dictionnary of existing profiles"""

    if os.path.exists(profile_filename): # if the file exists, we get the information in it
        profile_file = open(profile_filename, "rb")
        my_depickler = pickle.Unpickler(profile_file)
        profiles = my_depickler.load()
        profile_file.close()
    else: # it the file doesn't exist, we create a new profile dictionnary
        profiles = {}
    return profiles


def save_profiles(profiles):
    """This functions saves the new profiles in the file"""

    profile_file = open(profile_filename, "wb")
    mon_pickler = pickle.Pickler(profile_file)
    mon_pickler.dump(profiles)
    profile_file.close()