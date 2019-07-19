// SCC-Cplus.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include<fstream>
#include <stdio.h>
#include <string>
#include <stdlib.h>
#include <list>
#include <map>
#include <vector>
#include <algorithm>
#include <boost/algorithm/string.hpp>
#define _ITERATOR_DEBUG_LEVEL 0

#define MAXLINE 1//3
#define MAXCOLUMN 2//10
const unsigned int MAX_LINES = 1024;

class SCC
{
private:
	std::map<int, std::list<int>> graph;
	std::map<int, int> leader;
	std::map<int, int> f;
	std::map<int,int> explored;
	int t = 0;
	int s = 0;
	int count = 0;
	int n = 0;


public:
	std::map<int, int> Getf()
	{
		return f;
	}

	std::map<int, int> getLeader()
	{
		return leader;
	}

	SCC(std::map<int, std::list<int>> _graph, int _n, std::map<int, int> _explored)
	{
		graph = _graph;
		n = _n;
		explored = _explored;
	}

	~SCC()
	{

	}

	void DFS_Loop()
	{
		for (int i = n; i > 0; i--)
		{
			if (!explored[i]) // 没找到
			{
				s = i;
				DFS(i);
			}
		}
	}

	void DFS(int i)
	{
		count += 1;
		if (count % 5000 == 0)
		{
			std::cout << count << std::endl;
		}
		explored[i]=1;
		if (!leader.count(s)) // 没找到
		{
			leader[s] = 1;
		}
		else
		{
			leader[s]++;
		}

		if (graph.count(i))
		{

			for (std::list<int>::const_iterator iter = graph[i].begin(); iter != graph[i].end(); iter++)
			{
				if (!explored[*iter])
				{
					DFS(*iter);
				}
			}
		}
		t++;
		f[i] = t;
	}

};


int main()
{
	std::map<int, std::list<int>> graph;
	std::map<int, std::list<int>> graph_rev;
	std::map<int, int> explored;
	int count = 0;
	int temp_1;
	int temp_2;
	int n = 0;

	int count_0 = 0;

	std::ifstream inFile;
	std::string tmpStr("");
	std::string *a = new std::string[MAX_LINES];
	int index = 0;
	std::vector<std::string> result;
	inFile.open("H:/Algo/SCC/_SCC.txt", std::ios::in);
	if (!inFile)
	{
		std::cout << "文件打开失败！" << std::endl;
		return 1;
	}
	while (getline(inFile, tmpStr))
	{
		
		count_0++;
		if (count_0 % 5000 == 0)
		{
			std::cout << count_0 << std::endl;
		}
		a[index] = tmpStr;

		if (tmpStr != "")
		{
			boost::split(result, tmpStr, boost::is_any_of(" "));
			//for (int i = 0; i < result.size(); i++)
			//	std::cout << result[i] << std::endl;
			temp_1 = stoi(result[0]);
			temp_2 = stoi(result[1]);
			//std::cout << temp_1 << "-" << temp_2 << std::endl;
			explored[temp_1] = 0;
			explored[temp_2] = 0;
			if (temp_1 > n)
			{
				n = temp_1;
			}
			if (temp_2 > n)
			{
				n = temp_2;
			}
			count = 0;
			
			if (graph.count(temp_1))// if graph has this father node already
			{
				graph[temp_1].push_back(temp_2);
			}
			else // if not
			{
				graph[temp_1] = std::list<int>{ temp_2 };
			}
			if (graph_rev.count(temp_2))// if graph has this father node already
			{
				graph_rev[temp_2].push_back(temp_1);
			}
			else // if not
			{
				graph_rev[temp_2] = std::list<int>{ temp_1 };
			}
		}
		//index += 1;
	}

 	delete[] a;

	SCC* scc= new SCC(graph_rev,n,explored);
	scc->DFS_Loop();
	std::map<int, int> f_0 = scc->Getf();
	delete scc;
	graph_rev.clear();

	std::map<int, std::list<int>> graph_0;
	std::map<int, int> explored_0;
	for (auto& x : graph)
	{
		explored_0[f_0[x.first]] = 0;

		for (std::list<int>::const_iterator iter = x.second.begin(); iter != x.second.end(); iter++)
		{
			graph_0[f_0[x.first]].push_back(f_0[*iter]);
			explored_0[f_0[*iter]]=0;
		}
	}
	graph.clear();

	
	scc = new SCC(graph_0,n, explored_0);
	scc->DFS_Loop();
	
	std::map<int, int> leader = scc->getLeader();

	std::list<int> SCCs;
	for (auto& x : leader)
	{
		SCCs.push_back(x.second);
	}

	SCCs.sort();
	SCCs.reverse();
	int count_five = 0;
	for (std::list<int>::const_iterator it = SCCs.begin(); it != SCCs.end(); ++it)//std::list<int>::const_iterator iter= graph[i].begin(); iter != graph[i].end(); iter++
	{
		std::cout << *it<<",";
		count++;
		if(count==5)
		{
			break;
		}
	}
	printf("\n");
	std::cout << std::endl;




	//循环完毕后，所有数据已在data数组中
	getchar();
	return 0;
}

