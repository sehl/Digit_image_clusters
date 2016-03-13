## Class Cluster Analysis

Python code to extract digit 'types' from Kaggle/MNIST Digit Recognizer
dataset. Training data is first sorted by its label, then each digit is run
through a k-means clustering algorithm to extract different styles of
handwriting.

## Visualization Description
It occurred to me that everyone writes certain digits in different ways, for
instance what I call the 'z' two versus the 'loopy' two:

!['z' two][1]
!['loopy' two][2]

Or the 'closed' four versus the 'open' four:

!['closed' four][3]
!['open' four][4]

So, using the sklearn KMeans module, I extracted four, ten, and twenty clusters
for each digit in the labeled training set. Since the KMeans algorithm
initializes randomly, running with different seeds (which I did not do for
continuity purposes) will slightly alter which digit attributes are extracted in
each cluster set, but I found it interesting that the 'one with a hat' didn't
come out clearly until the 20-cluster set and that the 'seven with a mustache'
is vaguely in two of the 10-cluster means, but is very clear in only one of the
20-cluster set. Also, some people write really slanted ones!

![4-clusters per digit][5]
![10-clusters per digit][6]
![20-clusters per digit][7]

  [1]: http://i.imgur.com/z72eSGl.png
  [2]: http://i.imgur.com/1dpO0Po.png
  [3]: http://i.imgur.com/R73PjkP.png
  [4]: http://i.imgur.com/zQynypC.png
  [5]: http://i.imgur.com/JZxTuP9.png
  [6]: http://i.imgur.com/QBoZvbU.png
  [7]: http://i.imgur.com/ZoEMmEA.png

