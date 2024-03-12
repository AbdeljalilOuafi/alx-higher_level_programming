#include "lists.h"

/**
 * check_cycle - function that checks if a list contains a cycle or not
 * @list: the linked list to be checked
 * Return: 1 if the list contains a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
