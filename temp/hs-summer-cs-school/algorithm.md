1) Two-sum problem//

    The two sum algorithm finds all the pairs of 2 integers in an unsorted array that add up to a given number S
    
    The method looks at one number at a time, and stores it in its "dictionary." It uses the number as the key and the number's index in the array as the value.

    For each number n, the complementing number to sum up to the target is target - n. By looking up the complement in the dictionary, we'd know whether we've seen the complement before and what its index is.

    E.g - If the array is [-6, 7, 8, 11, -10] and the sume is one, it should return [-6, 7] and [11, -10] 

2) K-means clustering//

    The k-means clustering method takes a bunch of data and determines if there are clusters/groups of related objects within the data. 
    For example, you can use k-Means to find what are the 3 most prominent colors in an image by telling it to group pixels into 3 clusters based on their color value.hout deciding beforehand what categories to use. 
    The "k" in k-Means is a number. The algorithm assumes that there are k centers within the data that the various data elements are scattered around. The data that is closest to these so-called centroids become classified or grouped together. However, the k-means method doesn't signify the title/classification of the different groups. 
    
    The term "k-means" was first used by James MacQueen in 1967 but the standard algorithm was first proposed by Stuart Lloyd of Bell Labs in 1957 as a technique for pulse-code modulation, though it wasn't published as a journal article until 1982. In 1965, Edward W. Forgy published essentially the same method, which is why it is sometimes referred to as Lloyd-Forgy.
    
3) Shuffle//
    
    The shuffle method re-arranges the contents of an array. The algorithm first creates a new array that is empty. Then it randomly chooses an element from the original array and appends it to the new array until the original array is empty.

    Removing an element from an array is an O(n) operation and it is performed n times, which makes the total algorithm O(n^2).
    
    E.g if you have the array [1, 2, 3, 4, 5, 6], the first element can be any number from the array and then that number swaps with the last number. 
    
    If the number picked was 3, the array would then be [1, 2, 6, 4, 5, | 3] and any number after the "|" can't be swapped again; the next random number has to be picked from the array of [1, 2, 6, 4, 5] and the process repeats until there is only one number on the left side of the bar. 
    
    The Fisher–Yates shuffle is named after Ronald Fisher and Frank Yates, who first described it, and is also known as the Knuth shuffle after Donald Knuth. A variant of the Fisher–Yates shuffle, known as Sattolo's algorithm, may be used to generate random cyclic permutations of length n instead of random permutations.
    
    
