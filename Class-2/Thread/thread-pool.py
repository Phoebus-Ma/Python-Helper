###
# Thread pool test.
# 
# License - MIT.
###

# pip install threadpool
import threadpool
import random
import time


# thread_function - Thread test function.
def thread_function(id):
# {
    time.sleep(id)

    print('id : %d done.' % id)
# }


# Main function.
def main():
# {
    # Create thread pool.
    thrd_pool = threadpool.ThreadPool(5)

    # Create request function.
    reqs = threadpool.makeRequests(thread_function, range(1,6))

    # Thread pool add request function.
    [thrd_pool.putRequest(req) for req in reqs]

    # Wait all thread done.
    thrd_pool.wait()

    print()
# }


# Program entry.
if '__main__' == __name__:
    main()
