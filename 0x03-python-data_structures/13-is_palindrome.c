#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the list
 *
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *skip_1, *skip_2, *prev_s1, *first_half, *second_half, *mid;

	if (!head || !(*head) || !((*head)->next))
		return (1);

	first_half = skip_1 = skip_2 = prev_s1 = *head;
	second_half = mid = NULL;

	while (skip_1 && skip_2 && skip_2->next)
	{
		prev_s1 = skip_1;
		skip_1 = skip_1->next;
		skip_2 = skip_2->next->next;
	}
	if (skip_2 == NULL)
		second_half = skip_1;
	else
	{
		mid = skip_1;
		second_half = skip_1->next;
	}
	prev_s1->next = NULL;
	reverse_list(&second_half);

	if (list_equiv(first_half, second_half))
		return (1);
	else
		return (0);
}

/**
 * list_equiv - checks if two linked lists contain identical data
 * @l1: list one
 * @l2: list two
 *
 * Return: 1 or 0
 */
int list_equiv(listint_t *l1, listint_t *l2)
{
	while (l1 || l2)
	{
		if (l1->n != l2->n || !l1 || !l2)
			return (0);
		if (l1)
			l1 = l1->next;
		if (l2)
			l2 = l2->next;
	}
	return (1);
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to head of list
 *
 * Return: always void
 */
void reverse_list(listint_t **head)
{
	listint_t *next = NULL, *prev = NULL, *cur;

	cur = *head;
	while (cur)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	*head = prev;
}
