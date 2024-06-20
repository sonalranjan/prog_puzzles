import "slices"

// https://app.codesignal.com/arcade/graphs-arcade/in-the-pseudoforest/GeaKuCxLvje3bfsBx

func solution(n int, wmap [][]int, start int, k int) []int {
	adjList := buildAdjList(n, wmap)
	visited := make([]int, n)
	for i := 0; i < n; i++ {
		visited[i] = -1
	}

	// fmt.Printf("START: visited=%#v adjList=%#v \n", visited, adjList)
	// doBFS(start, &adjList, &visited, 0, k)
	doBFSNR(start, adjList, &visited, k)

	ret := []int{}
	for i := 0; i < n; i++ {
		if visited[i] != -1 {
			ret = append(ret, i)
		}
	}

	return ret
}

func doBFSNR(sn int, adjList map[int][]int, visited *[]int, maxLevel int) {
	nodes := [][]int{{sn, 0 /* start level */}}
	currIdx := 0
	for len(nodes[currIdx:]) > 0 {
		rn, level := nodes[currIdx][0], nodes[currIdx][1]
		// fmt.Printf("BFS currIdx=%v rn=%v level=%v \n", currIdx, rn, level)

		currIdx += 1

		if (*visited)[rn] != -1 {
			continue
		}

		// exit if maxLevel is reached
		if level > maxLevel {
			return
		}

		// mark visited
		(*visited)[rn] = level

		// insert unvisited neighbors
		for _, nb := range adjList[rn] {
			if (*visited)[nb] != -1 {
				continue
			}
			nodes = append(nodes, []int{nb, level + 1})
		}
	}

	return
}

func doBFS(rn int, adjList *map[int][]int, visited *[]int, level int, maxLevel int) {
	// fmt.Printf("BFS rn=%v level=%v maxLevel=%v \n", rn, level, maxLevel)

	if (*visited)[rn] != -1 {
		return
	}

	(*visited)[rn] = level

	if level >= maxLevel {
		return
	}

	// fmt.Printf("BFS_iter visited=%#v adjList[%d]=%#v\n", visited, rn, (*adjList)[rn])
	for _, nb := range (*adjList)[rn] {
		if (*visited)[nb] != -1 {
			continue
		}
		doBFS(nb, adjList, visited, level+1, maxLevel)
	}

	return
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
