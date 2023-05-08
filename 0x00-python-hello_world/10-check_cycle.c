#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - assess if a check is found in linked list
 * @list: ...
 * Return: Answer on success
 */
int check_cycle(listint_t *list)
{
	listint_t *alx;
	listint_t *room;

	while (!list || list->next == NULL)
		return (0);

	alx = list->next;
	room = list->next->next;

	while (alx && room && room->next)
	{
		if (alx == room)
			return (1);

		alx = alx->next;
		room = room->next->next;
	}

	return (0);
}
