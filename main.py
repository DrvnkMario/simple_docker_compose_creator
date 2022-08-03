import sys
sys.dont_write_bytecode = True # disable cache creation
from File_classes.compose_file import compose_file
from Tools.file_class_operations import file_class_operations 

if __name__ == "__main__":
    my_file = compose_file(sys.argv[1], sys.argv[2], int(sys.argv[3]))
    file_class_operations.save_file(my_file)