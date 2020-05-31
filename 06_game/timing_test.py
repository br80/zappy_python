framerate = 10

frame_time = 1 / framerate

start_time = time.time()

for i in range(10000):
    print(i)

processing_time = time.time() - start_time

processing_time

# If frame_time - processing_time is negative, wait_time will be 0
wait_time = max([0, frame_time - processing_time])
time.sleep(wait_time)

print(time.time() - start_time)
