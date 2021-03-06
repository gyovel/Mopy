from abc import abstractmethod
from gevent import os
from Configurations.cm import Cm
from DataBases.Elastic.MainSchema import QuerySchema
from Parsers.Json.JsonParser import JsonParser

class IQuery:
    def __init__(self):
        self.isExists=False
        dir_path = os.path.dirname(os.path.realpath(__file__))
        queryFileDic = JsonParser(dir_path + Cm().config["ElasticSearch"]["queriesFile"]).FileToDictionary()
        for queryItem in queryFileDic["queries"]:
            if queryItem["name"] == self.queryName:
                self.schema=QuerySchema(queryItem)
                self.queryItem=queryItem["query"]
                self.isExists=True
        if self.isExists==False:
            raise ModuleNotFoundError("The query - \"" + self.queryName + "\" wasn't found")

    @abstractmethod
    def Query(self):
        self.schema.load(self.queryItem)



