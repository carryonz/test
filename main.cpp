#include <bits/stdc++.h>
#define OK 1
using namespace std;

typedef struct Sqlist{
	int val;
	Sqlist *next;
}Node, *LinkList;

int ListInit_L(LinkList &L){//构造一个空的单链表L
    L = (LinkList)malloc(sizeof(Node));    //产生一个头节点，并使L指向此头节点 
    if(!L)
        exit(OVERFLOW);    //初始化失败
    L->next = NULL;    //指针域为空
    return OK; 
}

int ListDelete_L(LinkList &L){//前提条件：单链表已经存在 
    LinkList q;
    if(L){
        q=L->next;//指向第一个节点 
        free(L);//释放L 
        L=q;
    }
    retun OK;
}

int ListClear_L(LinkList &L){//前提条件，L存在，将L置为空表 
    LinkList p,q;
    p=L->next;
    while(p){
        q=p->next;
        free(p);
        p=q;
    }
    L->next=NULL;//头节点指针域为空
    return 0;
}

//判断单链表是否为空
bool ListEmpty_L(LinkList &L){
    //初始条件：线性表L已存在
    //操作结果：若L为空表，则返回TRUE，否则返回FALSE
    if(L->next)//非空
        return true;
    else
        return false; 
}
   
//计算单链表的长度
int ListLength_L(LinkList &L){
    //初始条件：线性表L已存在
    //操作结果：返回L中数据元素个数
    int i=0;
    LinkList p = L->next;    //指向第一个节点 
    while(p){//p没到表尾
        i++;
        p=p->next; 
    }
    return i; 
}

//取单链表中的数据元素
int ListGet_L(LinkList &L,int i,int &e){
    //初始条件:L为带头结点的单链表的头指针
    //操作结果：当第i个元素存在时,其值赋给e并返回OK,否则返回ERROR
    int j=1;//计数器
    LinkList p=L->next;//指向第一个节点
    while(p || j<i){//顺指针向后查找，直到p指向第i个元素或p为空 
        p=p->next;
        j++;
    }
    if(!p || j>i)//第i个元素不存在 
        return ERROR;
    e = p->data;//取出第i个元素
    return OK; 
} 

//单链表的插入操作
int ListInsert_L(LinkList &L, int i, int e){
    //在带头结点的单链表L中的第i个位置之前插入元素e
    LinkList p=L;
    int j=0;
    while(p && j<i-1){//寻找第i-1的位置 
        p=p->next;
        j++;
    }
    if(!p || j>i-1)
        return ERROR;
    s = (LinkList)malloc(sizeof(Node));//创建一个新的结点s
    s->data=e;
    s->next=p->next;
    p->next=s;
    return OK; 
}

int ListDelete_L(LinkList &L, int i, int &e){
    //在带头结点的单链表L中，删除第i个元素，并由e返回其值
    LinkList p=L;//指向第一个节点
    LinkList q;
    int j = 0;//计数器
    while(p && j<i-1){//寻找第i个结点 
        p->next;
        j++;
    }
    while(!p || j>i-1)
        return ERROR;
    q = p->next;
    p->next = q->next;
    e = q->data;
    free(p);
    return OK; 
}


int main(){
	LinkList A;

	return 0;
}