from gentopia.tools import BaseTool
from pydantic import BaseModel, create_model
from typing import Optional
from bs4 import BeautifulSoup
import requests

class ULAExtractorTool(BaseTool):
    name = "ula_extractor_tool"
    description = "Fetches and extracts text content from a url containing a user license agreement."
    args_schema: Optional[BaseModel] = create_model("ULAExtractorArgs", url=(str, ...))

    def _run(self, url: str) -> str:
        try:
            # get the url content
            response = requests.get(url)
            response.raise_for_status()

            # remove all html characters from the page, leaving us with only the text content
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content = soup.get_text().strip()

            return text_content
        except Exception as e:
            return f"ERROR: {e}"

    async def _arun(self, url: str) -> str:
        raise NotImplementedError("Async not implemented.")
