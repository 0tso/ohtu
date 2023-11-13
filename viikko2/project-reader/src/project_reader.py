from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        p = toml.loads(content)
        main = p["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(main["name"], main["description"], main["authors"], main["license"], list(main["dependencies"].keys()), list(main["group"]["dev"]["dependencies"].keys()))
