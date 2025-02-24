# Median Expenses

## Overview

This project provides two solutions to compute the median of expenses up to the first Sunday of each month. The implementation includes a naive approach using sorting and a more optimized approach utilizing the Quickselect algorithm.

## Features

- Extracts expenses up to the first Sunday of each month.

- Computes the median using two different methods:

  - **solution1:** Uses Python's built-in sorting function followed by median calculation.

  - **solution2:** Utilizes Quickselect, an efficient selection algorithm that finds the k-th smallest element in O(n) time on average.

## Usage

To use the solutions, provide an expenses in the format:

```
expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}
```
