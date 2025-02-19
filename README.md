# Description

Welcome to an AI-powered engineering challenge! You have inherited a project that originally focused on data engineering. However, the business team now requires AI-powered content generation and analytics to enhance customer interactions. Your task is to extend the existing system and integrate LLM-based capabilities while maintaining stable and scalable AI pipelines.
## Scenario

Some critical business data has been imported from an Excel file into a PostgreSQL database. For reasons unknown it couldn't come from a better source :(. This dataset contains customer interactions but it has inconsistencies and missing values... The previous developer started working on a Flask API that provides simple statistics, but the team now wants to incorporate **LLM-based insights** for content generation, research assistance, and text summarization.
  
## Data overview

**Customers**

| Customer Id | Occupation   | Type |
|------------|-------------|--------|
| 1          | Jedi        | Red    |
| 2          | Batman      | Orange |
| 3          | Santa Claus | Blue   |
| 4          | Mover       | Orange |

  
<br>

**External interactions**

| Date Start       | Interaction | Customers | Topic                     | Sentiment |
| ---------------- | ----------- | --------- | ------------------------- | --------- |
| 04/10/2019 09:00 | Email       | 1         | Drug Interaction Concerns | Negative  |
| 11/02/2020 16:10 | Call        | 4         | Side Effects Discussion   | Positive  |
| 05/03/2020 11:23 | Bird        | 4         | Drug Efficacy             | Positive  |
| 11/02/2020 16:24 | Call        | 5         | Prescription Guidelines   | Positive  |


<br>

**Products of discussion**

| Date    | Product|
|---------|--------|
| 01-2019 | Sand   |
| 02-2019 | Sand   |
| 03-2019 | Sand   |
| 04-2019 | Sand   |


## Tasks
### Update existing tables

 * Add data about topic and sentiment to the existing PostgreSQL database
 * Create all necessary tables based on the data required to implement the API endpoints

### Endpoints implementation

The previous data engineer was half way creating a Flask API. The API currently only returns some statistics on the data. The business folks would really like send every customer a personalised email based on past interactions, get summarization of these interactions and some statistical insights. You need to extend the existing **Flask API** to integrate AI-powered insights. Here some example endpoints:

1. `/api/v1/generate-content/{customer_id}`
    * Request: GET
    * Response:

```json
{
	"customer_id": 1,
	"generated_content": {
		"Content_type": "email",
		"Content": "Dear Jedi,\n\nThank you for reaching out regarding our latest products. Based on...",
	}
}
```

2. `/api/v1/summarized_interactions/{customer_id}`
   * Request: GET
   * Response:

```json
   {
    "customer_id": 1,
    "summary": {
        "total_interactions": 5,
        "most_frequent_channel": "Email",
        "last_interaction": {
            "date": "2024-01-25",
            "channel": "Call",
            "topic": "Product inquiry"
        },
        "key_topics": [
            "Product inquiry",
            "Drug efficacy",
            "Regulatory compliance"
        ],
        "summary_text": "Customer 1 frequently contacts us via email, primarily inquiring about drug efficacy, dosage recommendations, and regulatory compliance. The most recent interaction was a phone call regarding..."
    }
}
```

**Note**: You don’t need to call an actual LLM during development. Instead, mock the output of the LLM. The actual LLM integration should only happen after deployment(?).


3. The business team would also like to receive data about number of interactions per product for each type of the customers. But the person who made a request is currently on vacation for 4 weeks and there are no details on how the API response should look like. You'll have to come up with the first version of it yourself, and they will review it after getting back from the holiday.

### Data processing & AI pipeline setup

- Clean and preprocess customer interaction data.
- Implement a retrieval-augmented generation (RAG) system, integrating relevant interactions with the LLM requests. (_Reminder_: Placeholder for a LLM mock is prefered.)
- Ensure modular and scalable architecture, where AI models can be updated or swapped easily(if its mock only then how?).

### Testing & observability

- Implement **unit** test for individual components of the application (API endpoints, data processing functions, RAG system, mock LLM) .
- Write an **integration** test to ensure to ensure the entire system works as expected. 
- Think about **logging** and **monitoring** in this application. Log key events, such as API requests, data preprocessing steps, and LLM interactions. 
    * You don't need to set up monitoring, but think about  tools and best practices for real-time observability in a production environment. How would you set it up, and which tools would you use?

## Bonus points for:

* Implementing CI/CD pipeline
* Proposing a better alternative to `yoyo-migrations` for database schema migration. If possible, provide a brief example of how the new tool could be used to manage migrations in this project.
* Suggesting creative improvements to enhance the project's functionality, scalability, or maintainability.
* Teaching us something new! Whether it's a best practice, a novel approach, or an interesting tool, we'd love to learn from you.


## Some additional notes...

The previous hypothetical developer left a couple of tests in the tests folder, to check if the local docker step works.
* To check your database is there: ```pytest tests/intergration/utils/db/test_postgres.py```<br>
* To check test the api: ```pytest tests/intergration/test_app.py```<br>
* To test the factory methods for calling statistics: <br> 
```pytest tests/intergration/repository/statistics/test_postgres.py```

* Requirements can be found in the `pyproject.toml`. Requirements are managed via pip-tools.

* Helpful shell script to get the database up and runningf: ```./start_local_db_docker.sh```

* The required items for this project will be:
    * Python*
    * Docker (or podman if you like a little spice in your life).

* To build the full application you can run the following command:
    1) ```docker-compose up --build``` (Note: for podman ```podman compose -f "docker-compose.yml" up -d --build```)
    2) ```yoyo apply artifacts/migrations```
    3) ```pytests .```

  
* To remove the containers and images: ```docker-compose down --rmi all``` or ```podman compose down```
* Please don't work too hard, I'll feel bad.
* Please ask any questions you have (90% sure there is an error somewhere).

  

## Submission: 

For correct submission, please create a repository with your preferred GIT provider, and share the link to the repository per Email. Email submission of work files will be blocked by the mail-server, thus will not be successful. 


# Pre-reqs(poetry installation): Optional

### Install the [poetry](https://python-poetry.org/docs/#installation)

NOTE : if you don't want to use poetry you can manually install packages listed in pyproject.toml

# Installation

1. clone and cd into the repo
2. Run

    ```shell
    poetry install
    ```

    to install packages
3. Run

    ```shell
    poetry shell
    ```

    to to activate the environment
