##  QA Assignment for Load Test

```bash on UI
pip install -r requirements.txt
locust -f tests/load_test.py  
```

```bash on BE
pip install -r requirements.txt
locust -f tests/load_test.py --headless -u 10 -r 2 -t 1m --host http://0.0.0.0 --html reports/report.html --csv reports/report.csv
```

## Usage

- UI: bash on UI - click on http://0.0.0.0:8089 when you see on terminal
- This represents the maximum number of concurrent virtual users (simulated users) that will be active during your load
  test.
- The spawn rate indicates how quickly new virtual users are started or "spawned" during the ramp-up phase of your load
  test.
- The host parameter specifies the target host or the base URL of the web application or API that you want to test.
- BE: bash on BE - tests run without doing anything.
- You can see the results on reprts/ path.
