from .file_class import file
class compose_file(file):
    def __init__(self, filename, image_name: str = "alpine:latest", no_containers: int = 1, file_type: str = "yaml") -> None:
        super().__init__(filename, file_type) 
        self.content = "services:"  
        self.image_name = image_name
        self.no_containers = no_containers
        self.__build_file__()

    def __build_file__(self) -> None: # build docker-compose yaml
        for x in range(0, self.no_containers):
            self.content += f"\n  container_{x}: \n    image: {self.image_name}"

