#include<stdio.h>
#include<stdlib.h>
int front=-1,rear=-1;
int queue[10],data,i,size;
void enqueue()
{
if(rear==size-1)
{
printf("\n The queue is full");
}
else
{
printf("\n enter the data to be inseted");
scanf("%d",&data);
rear++;
queue[rear]=data;
printf("The element is inserted");
if(front==-1)
{
front=0;
}
}
}
void dequeue()
{
if(front==-1||front>rear)
{
printf("\n The queue is empty");
}
else{
printf("%d is deleted",queue[front]);
front++;
}
}
void display()
{
if(front==-1)
{
printf("The queue is empty");
}
else{
printf("\n The elements are:");
for(i=front;i<=rear;i++)
{
printf("\t %d",queue[i]);
}
}
}
int main()
{
int ch;
printf("\n Enter the array size");
scanf("%d",&size);
do
{
printf("\n 1. For enqueue \n 2. For dequeue \n 3. For display \n 4. Exit \n");
scanf("%d",&ch);
switch(ch)
{
case 1:
enqueue();
break;
case 2:
dequeue();
break;
case 3:
display();
break;
case 4:
exit(0);
default:
printf("invalid");
}
}
while(1);
}
