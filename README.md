# IT4663 - Tối ưu lập kế hoạch
**Paper reviewer assignment**
The chair of a conference must assign scientific papers to reviewers in
a balance way. There are 𝑁 papers 1, 2, … , 𝑁 and 𝑀 reviewers
1, 2, … , 𝑀. Each paper 𝑖 has a list 𝐿(𝑖) of reviewers who are willing to
review that paper. A review plan is an assignment reviewers to
papers. The load of a reviewer is the number of papers he/she have
to review. Given a constant 𝑏, compute the assignment such that:
- Each paper is reviewed by exactly 𝑏 reviewers
- The maximum load of all reviewers is minimal
- In the solution, each paper 𝑖 is represented by a list
𝑟(𝑖, 1), 𝑟(𝑖, 2), . . . , 𝑟(𝑖, 𝑏) of 𝑏 reviewers asssigned to this paper
> Input
- Line 1 contains 𝑁, 𝑀 and 𝑏
- Line 𝑖 + 1 (𝑖 = 1, … , 𝑁) contains a positive integer 𝑘 followed by
𝑘 positive integers representing the list 𝐿(𝑖)
> Output
- Line 1: contains 𝑁
- Line 𝑖 + 1 (𝑖 = 1, . . . , 𝑁): contains 𝑏 and 𝑏 integers
𝑟(𝑖, 1), 𝑟(𝑖, 2), . . . , 𝑟(𝑖, 𝑏) which are the list of reivewers assigned
to paper �
