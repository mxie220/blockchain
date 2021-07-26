## Blockchain

Task: Build a simplified blockchain.

Author: Michelle Xie

---

**Exercise 1: Finding the nounce**

Proof-of-work: Find a nounce that gives a hash starting with 4 bits of zeros, '0000'.
The average work required is exponential to the number of bits of zero so for this problem, we are expecting the average time it takes to find a nounce for a string of a total length 100 to be 100^4 = 100000000. 

Result:

| Input  | Nounce | Time |
| ------ | ------ | -----|
| michelle |  a46 | 0:00:07.035309 |
| 3 | eS9 | 0:00:37.121703 |
| helloworld | gdT | 0:00:53.632272 |
| blockchain | qPa | 0:04:47.842495 |
| michelle | ccccccccccccccccccccccccccccccccccccccccczcccccccccccccccccccccccccccccccccccccccccccccccccc | 0:16:32.526343 |
| 3 | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaZaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa | 0:02:12.748400 |

---

**Exercise 2: Constructing and verifying a blockchain**

Basically for the genesis block, start with '0' as minerId and find a nounce that is 99 in length. 
For all other blocks (the next 9) because I only need to build 10 blocks for the chain, will need to find a nounce of 35 in length because first 64 is made up of previous hash, 1 is made up of minderId which is '0' anyway and the entire length needs to be 100 in total.

