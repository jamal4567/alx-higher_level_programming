#include "lists.h"
/**
 *check_cycle -  checks if a singly linked list has a cycle in it.
 *
 *@list: singly linked list
 *
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *x, *y;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}
	x = list->next;
	y = list->next->next;
	while (x && y && y->next)
	{
		x = x->next;
		y = y->next->next;
		if (x == y)
			return (1);
	}
	return (0);
}
