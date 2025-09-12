# Important Topics/Algos

## QuickSelect

QuickSelect is an algorithm to find the **$k$-th smallest (or largest) element** in an unsorted array.  
It is related to QuickSort but only recurses on one side of the partition.

- **Average time complexity:** $O(n)$  
- **Worst-case time complexity:** $O(n^2)$ (bad pivot choices every time)  
- **Space complexity:** $O(1)$ (in-place, recursive stack $O(\log n)$ on average)

### Implementation

```cpp
#include <bits/stdc++.h>
using namespace std;

// Partition function: rearranges elements around a pivot
// After partitioning:
// - elements <= pivot are on the left
// - elements > pivot are on the right
// Returns the final index of the pivot
int partition(vector<int>& arr, int left, int right) {
    // Choose a random pivot to reduce chance of worst case
    int pivot_idx = left + rand() % (right - left + 1);
    int pivot = arr[pivot_idx];
    swap(arr[pivot_idx], arr[right]); // move pivot to end

    int i = left;
    for (int j = left; j < right; j++) {
        if (arr[j] <= pivot) {
            swap(arr[i], arr[j]);
            i++;
        }
    }
    swap(arr[i], arr[right]); // place pivot in its correct position
    return i;
}

// QuickSelect: finds the k-th smallest element (1-indexed)
// arr: input array
// left, right: current subarray bounds
// k: the order statistic (1 = smallest, n = largest)
int quickSelect(vector<int>& arr, int left, int right, int k) {
    if (left == right) return arr[left]; // only one element

    int pivot_idx = partition(arr, left, right);

    // number of elements in left part including pivot
    int count = pivot_idx - left + 1;

    if (count == k) {
        // pivot is the k-th smallest
        return arr[pivot_idx];
    } else if (k < count) {
        // k-th element is in the left part
        return quickSelect(arr, left, pivot_idx - 1, k);
    } else {
        // k-th element is in the right part
        // adjust k because we discard left part
        return quickSelect(arr, pivot_idx + 1, right, k - count);
    }
}
```

### Practice problems
* https://leetcode.com/problems/kth-largest-element-in-an-array/

## Trie (Prefix Tree)

An efficient data structure for information retrieval. Good for string problems (prefix, alphabets, etc).

### Implementation

```cpp
const int ALPHABET = 26;

struct TrieNode {
    TrieNode *children[ALPHABET];
    int terminal;
};

TrieNode *new_node() {
    TrieNode *new_node = new TrieNode;

    for(int i = 0; i < ALPHABET; ++i) {
        new_node->children[i] = NULL;
    }

    new_node->terminal = 0;
    return new_node;
}

void insert(TrieNode *node, string s) {
    for (char c : s) {
        int idx = int(c - 'a');

        if (!node->children[idx]) {
            node->children[idx] = new_node();
        }

        node = node->children[idx];
    }

    ++node->terminal;
}

void remove(TrieNode *node, string s) {
    for (char c : s) {
        int idx = int(c - 'a');

        if (!node->children[idx]) {
            return;
        }

        node = node->children[idx];
    }

    --node->terminal;
}

bool search(TrieNode *node, string s) {
    for (char c : s) {
        int idx = int(c - 'a');

        if (!node->children[idx]) {
            return false;
        }

        node = node->children[idx];
    }

    return node && (node->terminal > 0);
}

```

### Practice problems
* https://codeforces.com/problemset/problem/706/D

## Huffman Coding
