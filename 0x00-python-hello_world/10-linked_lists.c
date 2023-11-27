#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - Checks if list contains a cycle.
  * @list: the singly-linked list.
  * Return: 0 or 1.
  */

  int check_cycle(listint_t *list)
  {
	  listint_t *first = list;
	  listint_t *last = list;

          while (first != NULL && first->next != NULL)
	  {
		  last = last->next;
		  first = first->next->next;

		  if (last == first)
		  {
			  return (1);
		  }
	  }

           return (0);
  }
