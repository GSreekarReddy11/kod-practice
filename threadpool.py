from concurrent.futures import ThreadPoolExecutor
import time
def prepare_report(time):
    print(name, "report started")
    time.sleep(2)
    print(name, "report completed")

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(prepare_report, "Ananya")
    executor.submit(prepare_report, "Rahul")
    executor.submit(prepare_report, "Priya")
    executor.submit(prepare_report, "Abhi")
print("All reports completed")