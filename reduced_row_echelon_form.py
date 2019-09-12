import numpy as np

A = np.array([[1, 0, 1, 1],
             [1, 0, 1, 1],
             [0, 1, 1, 1],
             [1, 1, 1, 0],
             [1, 1, 1, 0]])


def gaussian_elim(A):
    
    A = A.astype(np.float64)

    #First convert to row-echelon form
    for row_count in range(min(A.shape)):

        col_count = row_count

        #find the maximum value in the current column
        max_num_col = np.max(abs(A[row_count:,col_count])) #maximum value
        max_num_col_pos = np.where(abs(A[row_count:,col_count]) == max_num_col)[0][0] #the position of maximum value

        #swap this row with the row where the maximum value exists
        A[[row_count, col_count + max_num_col_pos]] = A[[col_count + max_num_col_pos, row_count]]

        #reduce the pivot of this row to 1
        if A[row_count][col_count] == 0:
            continue
        A[row_count] = A[row_count] / A[row_count][col_count]

        #convert the below row of this column to 0
        for row_count2 in range(row_count+1, len(A[:,0])):
            if A[row_count2][col_count] == 0:
                continue
            A[row_count2] = A[row_count2] - A[row_count2][col_count] / A[row_count][col_count] * A[row_count]

    #Second convert to reduced row-echelon form
    for row_count in range(min(A.shape)):
        col_count = row_count

        if row_count == 0:
            continue

        for count, num in enumerate(A[row_count]):
            
            if num == 1:
                for recall_count in range(1,row_count+1):
                    if A[row_count-recall_count][count] != 0:
                        A[row_count-recall_count] = A[row_count-recall_count] - A[row_count-recall_count][count]/A[row_count][count]*A[row_count]

                break    
    
    return A


print(gaussian_elim(A))
