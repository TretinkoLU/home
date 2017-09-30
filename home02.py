matrix = [[8, 7, 0, 5, 11],
         [10, 6, 2, 2, 5],
         [6, 3, 2, 3, 12]]

result = False

for x in range(0, len(matrix)):
	
	indexOfMin = matrix[x].index(min(matrix[x]))
    isUnique = matrix[x].count(matrix[x][indexOfMin])
	
	if  isUnique < 2:
		verticalList = []
		
		for a in range(0, len(matrix)):
            verticalList.append(matrix[a][indexOfMin])

        indexOfMax = verticalList.index(max(verticalList))

        if x == indexOfMax:
            result = (x, indexOfMin)
            print(result)
            break
        else:
            continue


if result == False:
    print("False")