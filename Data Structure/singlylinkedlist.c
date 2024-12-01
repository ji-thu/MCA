#include<stdio.h>
#include<stdlib.h>
int count=0;
struct node
{
int data;
struct node* next;
}
*new,*head=NULL,*h,*l,*sl;
void create()
{
new=(struct node*)malloc(sizeof(struct node));
printf("Enter the data to the node ");
scanf("%d",&new->data);
new->next=NULL;
}
void ins_beg()
{
create();
if(head==NULL)

{
head=new;
}
else
{
new->next=head;
head=new;
}
count++;
}
void ins_end()
{
create();
if(head==NULL)
{
head=new;
}
else
{
h=head;
while(h->next!=NULL)
{
h=h->next;
}
h->next=new;
}
count++;
}
void ins_pos()
{
int pos,i;

printf("Enter the position");
scanf("%d",&pos);
if(pos==1)
ins_beg();
else if(pos==count+1)
ins_end();
else if((pos>count+1)||(pos<1))
printf("Invalid position");
else
{
create();
h=head;
for(i=0;i<pos-2;i++)
h=h->next;
new->next=h->next;
h->next=new;
count++;
}
}
void display()
{
if(head==NULL)
printf("List is empty");
else
{
h=head;
printf("Linked list elements are ");
while(h!=NULL)
{
printf("%d -> ",h->data);
h=h->next;

}
//printf("%d ",h->data);
}
}
void del_beg()
{
if(head==NULL)
printf("List is empty");
else
{
h=head;
head=head->next;
printf("Deleted element is %d ",h->data);
free(h);
count--;
}
}
void del_end()
{
if(head==NULL)
printf("List is empty");
else
{
l=head;
sl=head;
while(l->next!=NULL)
{
sl=l;
l=l->next;
}
sl->next=NULL;

printf("Deleted element is %d ",l->data);
free(l);
count--;
}
}
void del_pos()
{
int pos,i;
if(head==NULL)
printf("List is empty");
else
{
printf("Enter the position to delete ");
scanf("%d",&pos);
if(pos==1)
del_beg();
else if(pos==count)
del_end();
else
{
l=head;
sl=head;
for(i=0;i<pos-1;i++)
{
sl=l;
l=l->next;
}
sl->next=l->next;
printf("Deleted element is %d ",l->data);
free(l);
count--;

}
}
}
void main()
{
int ch=0;
do
{
printf("\nChoose option \n");
printf("1 Insert at beginning \n2) Insert at end \n3) Insert at a position \n4) Delete atbeginning \n5) Delete at end \n6) Delete at a position \n7)Display \n8) Exit\n");
scanf("%d",&ch);
switch(ch)
{
case 1:
ins_beg();
break;
case 2:
ins_end();
break;
case 3:
ins_pos();
break;
case 4:
del_beg();
break;
case 5:
del_end();
break;
case 6:
del_pos();
break;

case 7:
display();
break;
case 8:
printf("Exiting");
break;
default:
printf("Wrong Choice");
}
}
while(ch!=8);
}
