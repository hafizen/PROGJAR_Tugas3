from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread
from multiprocessing import Process
from kirim_data import kirim_data
from datetime import datetime

maxsize = 1000

def client_thread():
    try:
        start = datetime.now()
        for i in range(maxsize):
            kirim_data(i)

        end = datetime.now() - start
        print(f"Request total {maxsize}")
        print(f"Waktu TOTAL yang dibutuhkan {end} detik")

    except Exception:
        print("limit reached")

def client_process():
    start = datetime.now()
    for k in range(maxsize):
        process = Process(target=kirim_data, args=(k,))
        process.start()
        process.join()

    end = datetime.now() - start
    print(f"Request total {maxsize}")
    print(f"Waktu TOTAL yang dibutuhkan {end} detik")

def client_pool():
    pools = []
    try:
        with ThreadPoolExecutor() as executor:
            start = datetime.now()
            for k in range(maxsize):
                pools = [executor.submit(kirim_data, nama=f"thread ke -{k}")]

            for pool in as_completed(pools):
                pool.result()

        end = datetime.now() - start
        print(f"Request total {maxsize}")
        print(f"Waktu TOTAL yang dibutuhkan {end} detik")
    except Exception:
        print("limit reached")


if __name__ == '__main__':
    #client_thread()
    # client_process()
    client_pool()
    