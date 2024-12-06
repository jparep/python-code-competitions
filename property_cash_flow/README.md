# Property Cash Flow Analysis

## Problem Statement

A property manager needs an analysis of the cash flows for various rental properties held by the company. Write a query or function that will provide statistics for each property.

### Requirements

You need a summary of the total, minimum, maximum, and average cash flow received per property.

The result should have the following columns:

1. **name**: Name of the property.
2. **cash_flows**: Total number of cash flow records for the property.
3. **min_cash_flow**: Minimum cash flow for the property.
4. **max_cash_flow**: Maximum cash flow for the property.
5. **avg_cash_flow**: Average cash flow for the property (rounded to two decimal places).

The result should:
- Include only properties with an average cash flow greater than 10,000.
- Be sorted in ascending order by property name.

### Input Format

The input consists of two tables:
1. `properties`:
    - `id` (INT): Property ID (Primary Key).
    - `name` (VARCHAR): Name of the property.
2. `cash_flows`:
    - `property_id` (INT): Foreign key referencing `properties.id`.
    - `amount` (INT): Cash flow amount for the property.

### Example Input

**Properties Table**:
| id  | name           |
| --- | -------------- |
| 1   | Cozy Cottage   |
| 2   | Sunset Villa   |
| 3   | Harmony Haven  |

**Cash Flows Table**:
| property_id | amount |
| ----------- | ------ |
| 1           | 3762   |
| 1           | 4513   |
| 1           | 5829   |
| 1           | 7340   |
| 1           | 8014   |
| 1           | 15213  |
| 2           | 2318   |
| 2           | 5917   |
| 2           | 6343   |
| 2           | 8158   |
| 3           | 1065   |
| 3           | 1575   |
| 3           | 6417   |
| 3           | 7669   |
| 3           | 11604  |
| 3           | 11644  |
| 3           | 11739  |
| 3           | 12686  |
| 3           | 18495  |
| 3           | 19898  |

### Expected Output

The output should be a list of dictionaries with the following format:

```python
[
    {
        "name": "Harmony Haven",
        "cash_flows": 10,
        "min_cash_flow": 1065,
        "max_cash_flow": 19898,
        "avg_cash_flow": 11758.20
    }
]
