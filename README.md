# BCJR_Trellis
This is the project of EE5680 Error-Correcting Codes. We want to construct the BCJR trellis over $ GF(2^b) $. </br>
There are two steps for building BCJR trellis: </br>
1. Build BCJR pre-trellis 
2. Delete vertices and edges from the end

## Example
A parity check matrix of a [5,3] binary linear block code is given by </br>
![H](https://github.com/ChenBlue/BCJR_Trellis/blob/master/FIG/parity-check-matrix.JPG) </br>
The length of code n is 5, so there are $5+1=6$ stages in BCJR trellis. We denotes that </br>
* $ V=V_0 \cup V_1 \cup ... \cup V_n $: $V_k$ denotes the vertices set in kth stage.
* $ E=E_{0,1} \cup E_{1,2} \cup ... \cup E_{n-1,n}$: $E_{k,k+1}$ denotes the edge set in from kth stage to (k+1)th stage.
The initial vertex is always 0: $V_0 ={(00)}$. Next, we connect the verticex to the next stage. $ V_1={(00)+(11)\times 0=(00), (00)+(11)\times 1=(11)} $, and $ E_{0,1}={(00) \rightarrow (00), (00) \rightarrow (11)} $. And from $V_1$ to $V_2$, we use the second column of parity-chcek matrix, and so on. Then, we can construct the BCJR pre-trellis shown as followin. 
![pre-trellis](https://github.com/ChenBlue/BCJR_Trellis/blob/master/FIG/BCJR-pre-trellis.JPG)

In $ GF(2^b) $, there are $2^b$ edges starting from one vertex.
