#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - Prints a singly linked list numbers
 * @head: the pointers to adddress head
 * @number: ...
 * Return: always answer.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *x = *head, *fresh;

	fresh = malloc(sizeof(listint_t));
	if (!fresh)
		return (NULL);
	fresh->n = number;

	if (!x || x->n >= number)
	{
		fresh->next = x;
		*head = fresh;
		return (fresh);
	}

	while (x && x->next && x->next->n < number)
		x = x->next;

	fresh->next = x->next;
	x->next = fresh;

	return (fresh);
}
