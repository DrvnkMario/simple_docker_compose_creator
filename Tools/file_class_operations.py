
class file_class_operations:
    from File_classes import file_class
    @staticmethod
    def save_file(file: file_class) -> None:
        temp = open(f"{file.file_name}.{file.file_type}", "w")
        temp.write(file.content)