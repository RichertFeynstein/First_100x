import time

while True:
    start_time = time.time()
    while time.time() - start_time < 10:
        print("Hello, World!")
    time.sleep(10)

#Hello World program - my first for 100x