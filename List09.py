def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    sanoq=fruits.count('apple')
    if fruits[0]=='apple':
        fruits[0]=0
    if fruits[1]=='apple':
        fruits[1]=1
    if fruits[2]=='apple':
        fruits[2]=2
    if fruits[3]=='apple':
        fruits[3]=3
    if fruits[4]=='apple':
        fruits[4]=4
    list1=[sanoq,fruits[0],fruits[1],fruits[2],fruits[3],fruits[4]]
    return list1
print(main(fruits=['apple','kiwi','apple','apple','banan']))