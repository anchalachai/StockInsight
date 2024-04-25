# FastAPI Stock Price API

This is a FastAPI application that provides HTTP APIs to perform operations on daily stock prices using the AlphaVantage API. 

## Requirements

- Python 3.8 or higher
- Poetry

## Setup Instructions

1. **Install Poetry**:
    - Make sure you have Python 3.7 or higher installed.
    - Install Poetry using pip:

        ```shell
        pip install poetry
        ```

2. **Clone the Project**:
    - Clone the project repository:

        ```shell
        git clone [repository_url]
        ```

    - Replace `[repository_url]` with the URL of your repository.

3. **Navigate to the Project Directory**:
    - Navigate to the project directory:

        ```shell
        cd [project_directory]
        ```

    - Replace `[project_directory]` with the name of your project directory.

4. **Create and Activate a Virtual Environment**:
    - Use Poetry to create a virtual environment and install dependencies:

        ```shell
        poetry install
        ```

    - Then, activate the virtual environment:

        ```shell
        poetry shell
        ```

5. **Run the Application**:
    - Start the FastAPI application using Uvicorn:

        ```shell
        uvicorn app:app --reload
        ```

    - This command starts the FastAPI application and makes it available locally on localhost.
    - The `--reload` flag enables automatic reloading of the application when you make changes to the code.

## Using the API

Once the application is running, you can use `curl` commands to call the API endpoints.

### Lookup Endpoint

- Get stock data for a specific symbol and date:

    ```shell
    curl "http://<local host >/lookup?symbol=SYMBOL&date=YYYY-MM-DD"
    ```

- Replace `SYMBOL` with the stock symbol (e.g., `AAPL`) and `YYYY-MM-DD` with the date (e.g., `2024-04-24`).

### Min Endpoint

- Get the lowest price traded over the last `n` days:

    ```shell
    curl "http://<local host >/min?symbol=SYMBOL&n=N"
    ```

- Replace `SYMBOL` with the stock symbol (e.g., `AAPL`) and `N` with the number of days (e.g., `10`).

### Max Endpoint

- Get the highest price traded over the last `n` days:

    ```shell
    curl "http://<local host>/max?symbol=SYMBOL&n=N"
    ```

- Replace `SYMBOL` with the stock symbol (e.g., `AAPL`) and `N` with the number of days (e.g., `10`).

## Feedback and Contributions

We welcome any feedback or contributions. If you encounter any issues or have suggestions for improvements, please feel free to open an issue or pull request.

Happy coding!
