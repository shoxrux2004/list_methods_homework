def main(fruits,x,i):
    """
    You will be given a list of fruits. Add the x fruit to the i index and return it.
    Args:
        fruits(list): parameter 
        x(str): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    a=fruits.insert(i,x)
    return fruits
print(main(fruits=['apple','banan'],x='kiwi',i=1))