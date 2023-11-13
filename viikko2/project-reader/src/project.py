class Project:
    def __init__(self, name, description, authors, lisence, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.authors = authors
        self.lisence = lisence
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        string = (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.lisence}\n\n"
        )

        string += "Authors:"
        for author in self.authors:
            string += f"\n– {author}"
        
        string += "\n\nDependencies:"
        for d in self.dependencies:
            string += f"\n– {d}"
        

        string += "\n\nDevelopment dependencies:"
        for d in self.dev_dependencies:
            string += f"\n– {d}"
        
        return string