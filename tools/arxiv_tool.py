from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun

# Arxiv Tool
class ArxivTool:
    def __init__(self):
        self.api_wrapper = ArxivAPIWrapper(top_k_results=2, doc_content_chars_max=300)
        self.tool = ArxivQueryRun(api_wrapper=self.api_wrapper)

    def call_tool(self):
        return self.tool