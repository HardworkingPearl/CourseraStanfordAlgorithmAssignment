// SCC.cpp : �������̨Ӧ�ó������ڵ㡣
//

#include "stdafx.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <list>
#include <map>
#define MAXLINE 100//3
#define MAXCOLUMN 2//10

int main()
{
	FILE *fp; //�ļ�ָ��
	char arr[MAXLINE][MAXCOLUMN] = { 0 };  //����3��10�еĶ�ά���鲢��ʼ��
	int i = -1;
	if ((fp = fopen("D:/File/Algo/Part 10/SCC.txt", "r")) == NULL) { //��txt�ļ�
		perror("File open error!\n");
		return 0;
	}
	
	std::map<int, std::list<int>> graph;
	std::map<int, std::list<int>> graph_rev;
	int count = 0;
	int temp_1;
	int temp_2;
	while ((fgets(arr[++i], MAXCOLUMN + 1, fp)) != NULL) //��ȡһ�в��浽arr���飬�ٶ�fgets
	{
		printf("%d: ", i);
		//��ӡ�к�
							  //puts(arr[i]);
		char *subarr = strtok(arr[i], " ");  //�Կո�Ϊ�ָ�����arr[i]�л���ִ�,�ٶ�strtok

		while (subarr != NULL) {
			
			//printf("%d\t", temp_1);  //��ӡdata[i][j]
			
										 //int temp_2 = atoi(subarr);						 //data�����м�һ
			count++;
			if(count==1)
			{ 
				temp_1 = atoi(subarr);  //���ִ�תΪint�����ݴ���data����
			}
			else if (count == 2)
			{
				temp_2 = atoi(subarr);
				count = 0;
				graph.count(temp_1);
			}
			subarr = strtok(NULL, " ");  //�������arr[i]�е��ִ�
			
		}
		printf("\n");
	}
	//ѭ����Ϻ�������������data������
	printf("\n");
	fclose(fp);  //�ر�ָ��
    return 0;
}

