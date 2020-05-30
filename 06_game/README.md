## time() and sleep()

Timing is crucial for games and animation. We can import Python's `time` module to help us build our graphics display.

```python
import time

time.time() # The number of seconds since Jan 1, 1970
# 1590861260.771779
```

Let's wait a few seconds.

```python
time.time()
# 1590861311.3672168
```

Notice that the value of `time.time()` changed after some time had passed. We can also use the `time.sleep()` function to make Python pause for some amount of time.

```python
start_time = time.time()
# 1590861459.577342
time.sleep(5)
end_time = time.time()
# 1590861464.58429
print(f"Slept for {end_time - start_time} seconds.")
# Slept for 5.006947994232178 seconds.
```

Not exact, but pretty close.

