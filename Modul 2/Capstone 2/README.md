# TransJakarta Data Analysis

## Background
TransJakarta is a transportation company. In the upcoming period, the company has a desire to expand its business into the advertising field. Broadly speaking, this advertising business is intended for brands that want to advertise their products on TransJakarta-operated vehicles. It is known that TransJakarta has various types of vehicles and, especially, varying passenger density levels. Therefore, pricing determination is expected to be divided into classes based on specific criteria. **Hence, TransJakarta requires insights to classify their vehicles for pricing determination in advertising spaces on the vehicles, based on the data they possess**.

## Problem Statement
TransJakarta aims to classify their vehicles for pricing determination in advertising spaces on the vehicles based on the data they possess. Consequently, the following questions arise:

1. What is the relationship between the data variables in determining passenger numbers?
2. How is the proportion and quantity of different vehicle types based on available routes?
3. How can the class division be achieved based on data variables?

## Stakeholder
Business Development TransJakarta Team

## Domain Knowledge:
    - **Raw data**
        - **tahun**: year of the data is collected.
        - **bulan**: month of the data is collected.
        - **jenis**: type of vehicle.
        - **kode_trayek**: route code.
        - **trayek**: route.
        - **jumlah_penumpang**: the number of passengers.
     - **After data manipulation**
        - **Date**: year and month of the data is collected.

## Usage

To use the program, download and run the `simpleLibrary.py` file:

```bash
python simpleLibrary.py
```

### Create Function
To add a new book, select option `[2]` from the menu and enter the book information when prompted. The following fields should be completed when adding a book: Author, Year, Title, City, Publisher, ISBN, and Category. Once you have entered all the necessary information for a new book, the program will generate a unique book ID based on the date of book added and category of the book.

### Read Function
To show list of book, select option `[1]` from the menu. The program includes filter and sort functions that can be used to display the desired view. You can apply the filter function to either all fields or specific fields. Similarly, the sort function can be configured to sort by ascending or descending order on selected fields.

Additionally, there is an option to reset the book list to its initial state, removing any applied filter and sort settings.

### Update Function
To update a book, select option `[3]` from the menu. You could choose the book that you would be updated by enter the index of the book. After selecting the option to update a book, the program will display the book information and allow you to select which field(s) to update. It is possible to update all fields except for the book ID.

### Delete Function
To delete a book, select option `[4]` from the menu and  enter the index of the book as it appears on the list that you wish to delete.


## Contact
If you have any questions or feedback, please contact me at akbarezamuhammad10@gmail.com.
