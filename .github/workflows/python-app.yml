name: get stock price

on:
  schedule:
    - cron: "*/5 1-20 * * 1-6"
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.9
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install requests
          pip install BeautifulSoup4
      
      - name: Check out code
        uses: actions/checkout@v4

      - name: Run Python script
        run: python test1.py
