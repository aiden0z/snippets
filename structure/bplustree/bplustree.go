package bplustree

// BPTree describe a B+ tree.
type BPTree struct {
	Root *Node
}

// Node describe the tree node.
type Node struct {
	Parent   *Node   // Parent node
	Items    []Item  // The items in node
	Children []*Node // Children nodes
	Next     *Node   // Next neighbor node
	Previous *Node   // Previous neihbor node
}

// Item represents a single object in the tree.
type Item interface {
	Less(than Item) bool
	String() string
}
