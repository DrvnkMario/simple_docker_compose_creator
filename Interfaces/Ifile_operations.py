# File operations interface. Overwrite its methods in your 
import abc

class Ifile_operations(metaclass=abc.ABCMeta):
    @classmethod 
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'save_file') and 
                callable(subclass.save_file))