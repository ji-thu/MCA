#include <stdio.h>
#define MAX 100
int parent[MAX];

int find(int i) {
while (parent[i] != i)
i = parent[i];
return i;
}

void unionSets(int u, int v) {
int rootU = find(u);
int rootV = find(v);
parent[rootU] = rootV;
}

void kruskal(int graph[MAX][MAX], int V) {
int minCost = 0, edges = 0;

for (int i = 0; i < V; i++)
parent[i] = i;
printf("Edges in the Minimum Spanning Tree:\n");

while (edges < V - 1) {
int min = 999, u = -1, v = -1;

for (int i = 0; i < V; i++) {


for (int j = 0; j < V; j++) {
if (graph[i][j] != 0 && graph[i][j] < min && find(i) != find(j)) {
min = graph[i][j];
u = i;
v = j;
}
}
}

unionSets(u, v);
printf("%d -- %d == %d\n", u, v, min);
minCost += min;
edges++;

graph[u][v] = graph[v][u] = 0;
}
printf("Total cost of MST: %d\n", minCost);
}
int main() {
int V, graph[MAX][MAX];
printf("Enter the number of vertices: ");
scanf("%d", &V);
printf("Enter the adjacency matrix:\n");
for (int i = 0; i <V; i++) {
for (int j = 0; j < V; j++) {
scanf("%d", &graph[i][j]);
}
}
kruskal(graph, V);
return 0;
}
