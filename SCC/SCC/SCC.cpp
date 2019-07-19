// SCC.cpp : 定义控制台应用程序的入口点。
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
	FILE *fp; //文件指针
	char arr[MAXLINE][MAXCOLUMN] = { 0 };  //定义3行10列的二维数组并初始化
	int i = -1;
	if ((fp = fopen("D:/File/Algo/Part 10/SCC.txt", "r")) == NULL) { //打开txt文件
		perror("File open error!\n");
		return 0;
	}
	
	std::map<int, std::list<int>> graph;
	std::map<int, std::list<int>> graph_rev;
	int count = 0;
	int temp_1;
	int temp_2;
	while ((fgets(arr[++i], MAXCOLUMN + 1, fp)) != NULL) //读取一行并存到arr数组，百度fgets
	{
		printf("%d: ", i);
		//打印行号
							  //puts(arr[i]);
		char *subarr = strtok(arr[i], " ");  //以空格为分隔符从arr[i]中获得字串,百度strtok

		while (subarr != NULL) {
			
			//printf("%d\t", temp_1);  //打印data[i][j]
			
										 //int temp_2 = atoi(subarr);						 //data数组列加一
			count++;
			if(count==1)
			{ 
				temp_1 = atoi(subarr);  //将字串转为int型数据存入data数组
			}
			else if (count == 2)
			{
				temp_2 = atoi(subarr);
				count = 0;
				graph.count(temp_1);
			}
			subarr = strtok(NULL, " ");  //继续获得arr[i]中的字串
			
		}
		printf("\n");
	}
	//循环完毕后，所有数据已在data数组中
	printf("\n");
	fclose(fp);  //关闭指针
    return 0;
}

