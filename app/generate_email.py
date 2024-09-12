import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_community.document_loaders import WebBaseLoader
import portfolio
from utils import clean_text

class ColdEmailGenerator:
    def __init__(self, github_token):
        self.github_token = github_token
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.setup_environment()
        self.llm = self.initialize_llm()
        self.prompt_extract, self.prompt_email = self.create_prompts()

    def setup_environment(self):
        if not self.github_token:
            raise ValueError("GITHUB_TOKEN is not set")
        os.environ["OPENAI_API_KEY"] = self.github_token
        os.environ["OPENAI_BASE_URL"] = "https://models.inference.ai.azure.com/"

    def initialize_llm(self):
        GPT_MODEL = "gpt-4o-mini"
        return ChatOpenAI(model=GPT_MODEL)

    def create_prompts(self):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAP TEXT FROM WEBPAGE:
            {page_data}
            ### INSTRUCTIONS:
            The scraped text is from career page of a company website.
            Your job is to extract the job postings and return them in json format containing the following
            keys: 'role', 'experience', 'skills' and 'description'.
            Only return the valid JSON.
            ### VALID JSON(NO PREAMBLE):
            """
        )
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}
            
            ### INSTRUCTION:
            You are Mohan, a business development executive at BuildAI. BuildAI is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of BuildAI 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase BuildAI's portfolio: {link_list}
            Remember you are Mohan, BDE at BuildAI. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        return prompt_extract, prompt_email

    def load_webpage_data(self, url):
        loader = WebBaseLoader(url)
        return clean_text(loader.load().pop().page_content)

    def extract_job_postings(self, page_data):
        output_parser = StrOutputParser()
        chain_extract = self.prompt_extract | self.llm | output_parser
        res = chain_extract.invoke({"page_data": page_data})
        json_parser = JsonOutputParser()
        return json_parser.parse(res)

    def process_portfolio(self, skills):
        csv_file_path = "resource/my_portfolio.csv"
        return portfolio.process_portfolio(csv_file_path, "portfolio", skills, 2).get("metadatas", [])

    def generate_email(self, job_description, links):
        output_parser = StrOutputParser()
        chain_email = self.prompt_email | self.llm | output_parser
        return chain_email.invoke({"job_description": str(job_description), "link_list": str(links)})

    def save_email_to_file(self, email_content, file_path=None):
        if file_path is None:
            file_path = os.path.join(self.base_path, 'emails', 'email.txt')
        
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "w") as f:
            f.write(email_content)

    def generate_cold_email(self, url):
        page_data = self.load_webpage_data(url)
        jobs = self.extract_job_postings(page_data)
        links = self.process_portfolio(jobs["skills"])
        email_content = self.generate_email(jobs, links)
        self.save_email_to_file(email_content)
        return email_content

# Example usage:
# generator = ColdEmailGenerator(github_token=os.getenv("GITHUB_TOKEN"))
# email_content = generator.generate_cold_email("https://example.com/job-posting")