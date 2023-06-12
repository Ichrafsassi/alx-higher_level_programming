#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome-adds new node at the end of list listint_t
 * @head: pointer to pointer of first node of listint_t
 * Return: 1 if palindrome, 0 if its not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prv = NULL;
	listint_t *next;

	if (!head || !*head || !(*head)->next)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		next = slow->next;
		slow->next = prv;
		prv = slow;
		slow = next;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (prv != NULL && slow != NULL)
	{
		if (prv->n != slow->n)
			return (0);

		prv = prv->next;
		slow = slow->next;
	}

	return (1);
}
