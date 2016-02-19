import functools

# returns the maximum sum of a path starting at the top of
# the triangle and moving to adjacent number on the row below
# all the way from index i,j to the bottom
@functools.lru_cache(maxsize=4096)
def getMaxTotal(i,j):
    if i>=len(triangle) or j>=len(triangle[i]):
        raise ValueError("i,j are out of bounds of the triangle! "+str(i)+","+str(j))
    if i==len(triangle)-1:
        return triangle[i][j]
    return triangle[i][j] + max(getMaxTotal(i+1,j),getMaxTotal(i+1,j+1))

# returns the maximum sum of a path starting at the top of
# the triangle and moving to adjacent number on the row below
# all the way from the top to the bottom
def getAnswer():
    for i in range(len(triangle))[::-1]:
        for j in range(len(triangle[i])):
            t = getMaxTotal(i,j)
    return t

if __name__=="__main__":
    with open("ProjectEuler_0067.input.txt","r") as f:
        triangleContent = f.readlines()
    triangle = []
    for line in triangleContent:
        triangle.append([int(x) for x in line.split(' ')])
    print(getAnswer())
