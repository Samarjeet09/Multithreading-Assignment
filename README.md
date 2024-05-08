# Matrix Multiplication with Multiprocessing

This script demonstrates the use of multiprocessing in Python to perform matrix multiplication efficiently. It utilizes the `multiprocessing` module to parallelize the computation across multiple CPU cores.

## Requirements

- Python 3.x
- NumPy
- Pandas
- Matplotlib

## Usage

1. Install the required dependencies by running:
 ```bash
pip install numpy pandas matplotlib
```

2. Run the script using Python:


## Methodology

1. **generate_random_matrices(num_matrices, matrix_size):** This function generates a specified number of random matrices of a given size using NumPy.

2. **multiply_matrices_process(matrix_chunk, constant_matrix):** This function performs matrix multiplication for a chunk of matrices using a constant matrix. It uses the `np.dot()` function for matrix multiplication.

3. **perform_multiplication_with_processes(num_processes, matrices, constant_matrix):** This function parallelizes the matrix multiplication process across multiple processes using the `multiprocessing` module. It divides the list of matrices into chunks and distributes them among the specified number of processes.

4. The script calculates the time taken for matrix multiplication using different numbers of processes (from 1 to the number of CPU cores available) and plots the results using Matplotlib.

## Results

The script outputs the time taken for matrix multiplication using different numbers of processes and plots the results to visualize the performance improvement achieved through multiprocessing.

![alt text](https://github.com/Samarjeet09/Multithreading-Assignment/blob/main/imgs/img3.png)
### cpu utilization
<div style="display: flex;">
    <img src="https://github.com/Samarjeet09/Multithreading-Assignment/blob/main/imgs/img1.png" alt="alt text" width="400">
    <img src="https://github.com/Samarjeet09/Multithreading-Assignment/blob/main/imgs/img2.png" alt="alt text" width="400">
</div>


