

# Cold Email Generator

The Cold Email Generator automates the process of creating personalized cold emails for software services companies. Powered by OpenAI's GPT models, it extracts job requirements from client websites and generates contextually relevant emails, streamlining outreach efforts for Business Development Executives (BDEs) and Sales Representatives.

## Problem Statement

In the competitive software services industry, companies like Atlic Technologies, TCS, and Infosys often use cold emailing to offer their services to global clients such as Nike, JP Morgan, and Kroger. Crafting personalized cold emails that align with the specific job requirements is time-consuming and requires a deep understanding of the client’s needs.

For example, if Nike is hiring a software engineer with expertise in AI and Machine Learning, companies like Atlic can offer contractual staff to fill the role. However, manually creating emails tailored to such job posts demands effort and time, limiting the efficiency of sales teams.

## Solution

The Cold Email Generator leverages Large Language Models (LLMs) to automate and personalize cold emails. By inputting a job posting URL, the tool extracts the relevant skills and qualifications and generates a tailored email offering services related to the client’s needs. It also integrates portfolio links that showcase the company’s expertise in those areas.

## Key Objective

- Automate Cold Email Generation: Automatically create cold emails based on job posting requirements.
- Ensure Relevance: Highlight essential skills and qualifications extracted from the job post.
- Dynamic Portfolio Links: Include portfolio links that showcase relevant projects.
- Enhance Efficiency: Save time for sales teams by automating the email creation process.
- Increase Success Rate: Improve the chances of winning contracts by sending more targeted and professional emails.

### Key Components:
- **LangChain OpenAI**: Interacts with GPT models to generate email content.
- **LangChain Core**: Manages prompt templates and output parsing.
- **LangChain Community**: Loads job descriptions from the web.
- **Database Integration**: Stores and retrieves email content and portfolio data.

## Prerequisites

Ensure you have the following:
- Python 3.8+
- A valid **GITHUB_TOKEN** environment variable for OpenAI API authentication.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/cold-email-generator.git
    cd cold-email-generator
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Set up Environment**: Ensure you have the `GITHUB_TOKEN` environment variable set up:
    ```sh
    export GITHUB_TOKEN=your-token  # On Windows use `set GITHUB_TOKEN=your-token`
    ```

2. **Run the Script**:
    ```sh
    python email_generator.py
    ```

3. **Input Job URL**: When prompted, enter the URL of the job posting.

4. **Generate Email**: The script will extract job details, process your portfolio, and generate a personalized email. The generated email will be saved in the `emails/` directory as a text file.

## Example

```sh
$ python email_generator.py
Enter the job URL: https://example.com/job-posting
Generated email saved in emails/email.txt
```


## Contributing

We welcome contributions to the Cold Email Generator project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.


