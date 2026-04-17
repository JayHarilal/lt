Name: Jayaveer Harilal
Student Number: 2110071
ELEN3020A Lab Test 1
=======
# ELEN3020A Lab Test 1
Student Name: Jayaveer Harilal  
Student Number: 2110071  

## Testing Process  
This project demostrates the testing process for 'getbest.py' which finds the top student mark from a CSV file.  

### Bugs found and fixes  
Uninitialised variables in getCols() - 'num_col' and 'mark_col' could be returned when not assigned.  
Column indexing - The list is 0-based but used a 1-based index.  
Student number not captured because of index - 'best_idx' was not updated in findTop().  
Printed the index, not the student number - Returned the index value instead of the student number.  

### Test Cases  
The following test scenarios were ran and are included:  
TEST FILE | DATA | EXPECTED OUTPUT  
testdat0.csv | Original data | The top student was 167381 with 90  
testdat1_markfirst.csv | Different column order | The top student was 167381 with 50  
testdat2_onestudent.csv | One student in file | The top student was 1600071 with 72  
testdat3_marksascending.csv | Marks in order (ascending) | The top student was 167381 with 99  
testdat4_marksdescending.csv | Marks in order (descending) | The top student was 167381 with 99  

### Running the tests  
Git bash   

# Run full test process  
python tests/testgetbest1.py  

# Run final test manually  
python getbest.py testdat0.csv

