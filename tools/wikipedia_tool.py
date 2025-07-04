from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

# Wikipedia Tool
class WikipediaTool:
    def __init__(self):
        self.api_wrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=300)
        self.tool = WikipediaQueryRun(api_wrapper=self.api_wrapper)

    def call_tool(self):
        return self.tool