#include "lists.h"

/**
 * check_cycle - function checks if there a cycle in the singly-linked-list.
 * @list: pointer to the beginning of the node
 * cuur, check: current variable and checking a variable
 * Return: no cycle0, if there is a cycle 1
 */
int check_cycle(listint_t *list)
{
	listint_t *curr, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	curr = list;
	check = curr->next;

	while (curr != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (curr == check)
			return (1);
		curr = curr->next;
		check = check->next->next;
	}
	return (0);
}
