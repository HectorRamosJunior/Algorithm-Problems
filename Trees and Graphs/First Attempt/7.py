'''
    Build Order: 
    You are given a list of projects and a list of dependencies (which
    is a list of pairs of projects, where the first project is dependant
    on the second project.) All of a project's dependencies must be built
    before the project is. Find a build order that will allow the project
    to be built. If there is no valid build order, return an error.
'''

def getBuildOrder(projectList, dependencyList):
    nodeList = [Node(x) for x in projectList]
    headNodes = nodeList

    for n in nodeList:
        for d in dependencyList:
            if n.data == d[1]:
                n.edges.append(d[0])
                headNodes.remove(n)

    buildOrder = list(headNodes)

    for n in headNodes:
        check = dfs(n, buildOrder)
        if not check:
            return "Error"

    return buildOrder

def dfs(root, buildOrder, visitedNodes[]):
    if root in visitedNodes:
        return False

    visitedNodes.append(root)

    if not root in buildOrder:
        buildOrder.append(root)

    if root.edges:
        for n in root.edges:
            dfs(n, buildOrder, visitedNodes)

    return True


