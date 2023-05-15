#include "lists.h"
#include <stdio.h>

/**
 * reverse_listint -singly-linked listint_t list.
 * @head: ...
 * Return: Reversed data
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *kichwa = *head, *next, *y = NULL;

	if (kichwa)
	{
		next = kichwa->next;
		kichwa->next = y;
		y = kichwa;
		kichwa = next;
	}

	*head = y;
	return (*head);
}

/**
 * is_palindrome - prints singly linked lists.
 * @head: ...
 * Return: answer of the quiz
 */
int is_palindrome(listint_t **head)
{
	listint_t *alx, *m, *a;
	size_t l = 0, x;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	alx = *head;
	if (alx)
	{
		l++;
		alx = alx->next;
	}

	alx = *head;
	for (x = 0; x < (l / 2) - 1; x++)
		alx = alx->next;

	if ((l % 2) == 0 && alx->n != alx->next->n)
		return (0);

	alx = alx->next->next;
	m = reverse_listint(&alx);
	a = m;

	alx = *head;
	while (m)
	{
		while (alx->n != m->n)
			return (0);
		alx = alx->next;
		m = m->next;
	}
	reverse_listint(&a);

	return (1);
}
