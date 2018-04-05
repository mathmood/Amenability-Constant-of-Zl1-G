# Amenability constant of the center of group algebra for finite groups

The notion of amenability of Banach algebras initiated by Johnson's memoirs in which he showed that for every amenable group G, its group algebra is amenable and vice versa. 
Later, it was observed that this does not hold if one look at the centre of the group algebra. In 
>Azimifard, Ahmadreza; Samei, Ebrahim; Spronk, Nico Amenability properties of the centres of group algebras. J. Funct. Anal. 256 (2009), no. 5, 1544–1564.
it was shown that for large classes of compact groups, including SU(2), the centre of the group algebra is not amenable. 

It is immediate that finite group have amenable centres for their group algebras. So one may wondering, while all the group algebra of finite groups have amenebaility constant one, what are the amenability constants of the centre of the group algebras for finite groups.
This constant will be denoted throughout by the ZL-amenability constant of G.
In the aforementioned paper, the authors provided a formula which computes the ZL-amenability constant of G for finite groups when only the character table of G is provided. In a subsequent paper, my coauthors and I studied some particular classes of (very) nilpotent groups and came up with simplified ZL-amenability constant formulas.
> Alaghmandan, Mahmood; Choi, Yemon; Samei, Ebrahim ZL-amenability constants of finite groups with two character degrees. Canad. Math. Bull. 57 (2014), no. 3, 449–462. 

In this project, we first write a simple short code which reads the character table of a finite group from a square csv file and computes the ZL-amenability constant of G. Note the calculation in this code is mainly computing the formula in Azimifard et al paper and therefore holds for any finite groups.

```
import numpy as  np
import pandas as pd


def amenabilityConstant(fileName):
    df = pd.read_csv(fileName)
    n= len(df.T)
    am = 0
    g= 0
    col = list(range(0,n))
    df = pd.read_csv(fileName, names = col)
    for i in range(0, n):
        g = g + df.at[i, 0]**2

    dim = []
    conju = []
    for j in range(0,n):
        k =0
        for i in range(0,n): k = k + abs(df.at[i,j])**2
        conju.append(g/k)

    for k in range(0,n):
        for l in range(0,n):
            x =0
            for i in range(0,n):
                x = x + (df.at[i,0]**2 * df.at[i,l] * np.conj(df.at[i,k]) )
            am = am + (abs(x) * conju[k] * conju[l])
    am = am / (g**2)
    return am
```

To test the code, I use character table of symmetric groups. One may note that complicated pattern of the character tables of these groups makes calculating their ZL-amenability constant very hard without machine. But first we need to rely another program to find their character table. For this task, I used GAP. 

To do this, you need to first install GAP on your machine. Then run it and in the terminal ask for the character table of symmetric group of n elements (n should be a positive integer greater than 1).

```
> cd /Applications/Gap4/
> sh bin/gap.sh
> g:= SymmetricGroup( n );   #To call the symmetric group of n elements
> tbl:= CharacterTable( g ); # To call the character table
> Display(tbl);  # To present the table
```

The outcome would have the character table as well as some info regarding the order of conjugacy classes. Note that the later is not required in our computations. Therefore, we just copy and paste the table part in a csv file. The file needs to be cleaned as GAP uses "." to denote 0 and some other issues. The following code makes your table ready for the ZL-amenability constant function. 

```
def dataCleansing (filename):
    df = pd.read_csv(filename)
    n = len(df.T)

    col = list(range(0,n))
    df = pd.read_csv(filename, names = col)

    df = df.drop([0], axis =1)
    df = df.T.reset_index(drop=True).T

    df.to_csv(filename,  encoding='utf-8', columns=None, header=None, index=None, index_label=None, line_terminator='\n')
    return None
```
 
 I applied the following process for S3, S4, ..., S13. Their cleaned character tables can be found attached to this project. Finally, I used "amenabilityConstant" function to compute their ZL-constant. The outcome is as follows.

```
n,  ZL-constant Sn
2,  1
3,  2.3333333333333335
4,  7.083333333333333
5,  30.083333333333332
6,  134.70833333333334
7,  842.9821428571429
8,  4785.397116815476
9,  37803.2452943581
10, 269104.0945024847
11, 2662160.8938092054
12, 24817250.259653185
13, 5820687459.998998
