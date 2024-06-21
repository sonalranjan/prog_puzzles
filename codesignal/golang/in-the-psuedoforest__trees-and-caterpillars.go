import "slices"

// https://app.codesignal.com/arcade/graphs-arcade/in-the-pseudoforest/EywKKTcqGrfbavDrw

type AdjListT map[int][]int

func solution(n int, edges [][]int) []int {
	adjList := buildAdjList(n, edges)
	isTree := doTraversal(adjList)
	counts := []int{0, 0}

	for _, v := range isTree {
		if !v[0] {
			continue
		}

		counts[0] += 1
		if !v[1] {
			continue
		}
		counts[1] += 1
	}

	return counts
}

// no more than 2 nodes with degree >= 2
func doTraversal(adjList AdjListT) map[int][2]bool {
	// fmt.Printf("adjList=%#v \n", adjList)

	n := len(adjList)
	isTree := make(map[int][2]bool) // [is tree, is caterpillar]

	dfsmark := make([]int, n)
	for sn := 0; sn < n; sn++ {
		dfsmark[sn] = -1
	}

	for sn := 0; sn < n; sn++ {
		if dfsmark[sn] != -1 {
			continue // visited
		}

		treeFlags := [2]bool{true, true} // is tree, is caterpillar.

		nodes := [][2]int{{sn, 0}}
		currIdx := 0
		for len(nodes[currIdx:]) > 0 {
			rn, pn := nodes[currIdx][0], nodes[currIdx][1]

			// fmt.Printf("sn=%v pn=%v currIdx=%#v nodes=%#v neighbors=%#v\n", sn, pn, currIdx, nodes[currIdx:], adjList[rn])

			currIdx += 1
			dfsmark[rn] = sn
			for _, nb := range adjList[rn] {

				if dfsmark[nb] != -1 {
					// visited
					// back-edge ? mark as not a tree
					if nb != pn {
						treeFlags[0] = false
					}

					continue
				}

				nodes = append(nodes, [2]int{nb, rn})
			}

			if !treeFlags[0] {
				// fmt.Printf("** sn=%v rn=%v treeFlags=%#v \n", sn, rn, treeFlags)

				treeFlags[1] = false
				continue
			}

			// degree check
			count := 0
			for _, nb := range adjList[rn] {
				if len(adjList[nb]) >= 2 {
					// non-terminal node
					count += 1
				}
				if count > 2 {
					treeFlags[1] = false // not a caterpillar
					break
				}
			}

		}

		isTree[sn] = treeFlags
	}

	// fmt.Printf("isTree=%#v \n", isTree)

	return isTree
}

func buildAdjList(n int, wmap [][]int) map[int][]int {
	adjList := make(map[int][]int)
	for i := 0; i < n; i++ {
		adjList[i] = []int{}
	}

	insertFunc := func(n1, n2 int) {
		if !slices.Contains(adjList[n1], n2) {
			adjList[n1] = append(adjList[n1], n2)
		}
	}

	for _, e := range wmap {
		insertFunc(e[0], e[1])
		insertFunc(e[1], e[0])
	}

	return adjList
}
