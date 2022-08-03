class file:
    def __init__(self, file_name: str = "file", file_type: str = "txt", content: str = "") -> None:
        self.file_name = file_name
        self.file_type= file_type
        self.content = content
    
    def __build_file__(self) -> None: # Private method to build file while object is initialized
        pass                          # Overwrite it in your own file class

    def __str__(self):
        return self.content