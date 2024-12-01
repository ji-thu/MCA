#include<stdio.h>
void main() {
int a1[10], a2[10], a3[20], s1, s2, s3, i, j, k;
printf("Enter the size of array 1: ");
scanf("%d", &s1);
printf("Enter elements of array 1: ");
for(i = 0; i < s1; i++)
scanf("%d", &a1[i]);
printf("Enter the size of array 2: ");
scanf("%d", &s2);
printf("Enter elements of array 2: ");
for(i = 0; i < s2; i++)
scanf("%d", &a2[i]);
s3 = s1 + s2;
i = j = k = 0;
// Merging two sorted arrays
while(i < s1 && j < s2) {
if(a1[i] < a2[j]) {
a3[k] = a1[i];
i++;
} else {
a3[k] = a2[j];
j++;
}
k++;
}
// Copy remaining elements from array 1 if any
while(i < s1) {
a3[k] = a1[i];
i++;
k++;
}
// Copy remaining elements from array 2 if any
while(j < s2) {
a3[k] = a2[j];
j++;
k++;
}
printf("Merged array is: ");
for(i = 0; i < s3; i++)
printf("%d ", a3[i]);
printf("\n");
}
