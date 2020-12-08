#include "lists.h"

/**
 * check_cycle - Identifies if there is a cycle in a singly linked list.
 * @list: Is the list in question.
 * Return: Returns 1 for Yes in a cycle. 0 if not.
 */

int check_cycle(listint_t *list)
{
	listint_t *curr_node = list;
	listint_t *nav_tool = curr_node;

	while (curr_node && nav_tool && curr_node ->next)
	{
		nav_tool = nav_tool->next;
		curr_node = curr_node->next->next;
		if (curr_node == nav_tool)
			return (1);
	}
	return (0);
}
