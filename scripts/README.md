# Local development

## Running locally on macOS w/ Appple Silicon

1) Install brew

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2) Install Python 3.12

    ```bash
    brew install python@3.12
    ```

    Verify

    ```bash
    python3.12 --version
    ```

3) Setup a virtual environment

    ```bash
    python3.12 -m venv .venv
    source .venv/bin/activate
    ```

    Select Python interpreter in vscode

4) Update pip

    ```bash
    pip install --upgrade pip
    ```

5) Install requirements

    ```bash
    pip install -r requirements.txt
    ```

6) Run the app

    ```bash
    briefcase dev  
    ```
