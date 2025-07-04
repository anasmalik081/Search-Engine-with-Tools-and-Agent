from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import DuckDuckGoSearchRun

# DuckDuckGoSearch
class DuckDuckGoTool:
    def __init__(self):
        self.tool = DuckDuckGoSearchRun(name="search")
    
    def call_tool(self):
        return self.tool