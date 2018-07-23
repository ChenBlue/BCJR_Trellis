# BCJR_Trellis
This is the project of EE5680 Error-Correcting Codes. We want to construct the BCJR trellis over $ GF(2^b) $. </br>
There are two steps for building BCJR trellis: </br>
1. Build BCJR pre-trellis 
2. Delete vertices and edges from the end

## Example
A parity check matrix of a [5,3] binary linear block code is given by </br>
![H](https://github.com/ChenBlue/BCJR_Trellis/blob/master/FIG/parity-check-matrix.JPG) </br>
The length of code n is 5, so there are $5+1=6$ stages in BCJR trellis. 

### Step1. Build BCJR pre-trellis
We denotes that </br>
* $ V=V_0 \cup V_1 \cup ... \cup V_n $: $V_k$ denotes the vertices set in kth stage.
* $ E=E_{0,1} \cup E_{1,2} \cup ... \cup E_{n-1,n}$: $E_{k,k+1}$ denotes the edge set in from kth stage to (k+1)th stage.
The initial vertex is always 0: $V_0 =\{(00)\}$. Next, we connect the verticex to the next stage. $ V_1=\{(00)+(11)\times 0=(00), (00)+(11)\times 1=(11)\} $, and $ E_{0,1}=\{(00) \rightarrow (00), (00) \rightarrow (11)\} $. And from $V_1$ to $V_2$, we use the second column of parity-chcek matrix, and so on. Then, we can construct the BCJR pre-trellis shown as followin. </br>
![pre-trellis](https://github.com/ChenBlue/BCJR_Trellis/blob/master/FIG/BCJR-pre-trellis.JPG) </br>

### Step2. Delete vertices and edges from the end
I only keep vertex 0 at the last stage $V_n$. Next, delete edges which don't connnect vertex 0 at $V_n$ so on so forth, and then only keep the vertices and edges which have connection to the next stage from $V_n$ to $V_0$ and from $E_{n-1,n}$ to $E_{0,1}$. Therefore, we can construct the BCJR trellis which is illustrated as the following figure. </br>
![pre-trellis](https://github.com/ChenBlue/BCJR_Trellis/blob/master/FIG/BCJR_trellis_example.JPG) </br>

## Finite Field Arithmetic
In $ GF(2^b) $, there are $2^b$ edges connecting to the vertex at the next stage.

### Addition
It's the same as **XOR** operation in $ GF(2^b) $.

### Multiplication
Refer to the primitive polynomial table shown as the following. </br>

| degree | primitive polynomial | degree | primitive polynomial |
| ------- |-----------| ------- | ---------- 
|2 | 7 | 7 | 211
|3 | 13 | 8 | 435
|4 | 23 | 9 | 1021
|5 | 45 | 10 | 2011
|6 | 103 | 11 | 4005

> The primitive polynomial table is expressed as octal. </br>

First, do the standard multiplication. Second, derive the remainder of polynomial. For example, in $ GF(2^2) $, find $ 11\times 11 $. First, we get 101. Next, find the remainder of 101 divides by primitive polynomial 111, and then we can get 10.

## Result
I implemented a function *plot_section(i,j)* which can plot the BCJR trellis from *ith* layer $ V_i $ to *jth* layer $ V_j $.

### Case 1
parity-check matrix **H**: </br>
| 1 | 1 | 1 | 0 | 0 | 0 | 0 |
| -- | -- | -- | -- |---| --- | --- 
| 0 | 1 | 0 | 1 | 0 | 0 | 0
| 1 | 0 | 0 | 0 | 1 | 1 | 0
| 1 | 0 | 0 | 0 | 1 | 0 | 1
