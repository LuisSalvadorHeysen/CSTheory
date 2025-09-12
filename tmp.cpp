const int ALPHABET = 26;

struct trieNode {
    trieNode *children[ALPHABET];
    int terminal;
};

trieNode *new_node() {
    trieNode *new_node = new trieNode;
    new_node->terminal = 0;
    for (int i = 0; i < ALPHABET; ++i) {
        new_node->children[i] = NULL;
    }
    return new_node;
}

void insert(trieNode *root, string word) {
    trieNode *node = root;
    for (char c : word) {
        int idx = int(c - 'a');
        if (!node->children[idx]) {
            node->children[idx] = new_node();
        }
        node = node->children[idx];
    }
    ++node->terminal;
}

void del(trieNode *root, string word) {
    trieNode *node = root;
    for (char c : word) {
        int idx = int(c - 'a');
        node = node->children[idx];
    }
    --node->terminal;
}

bool search(trieNode *root, string word) {
    trieNode *node = root;
    for (char c : word) {
        int idx = int(c - 'a');
        if (!node->children[idx]) {
            return false;
        }
        node = node->children[idx];
    }
    return node && node->terminal;
}const
