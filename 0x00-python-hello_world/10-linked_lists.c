#include <stdlib.h>
#include "lists.h"

/**
  * check_cycle - Checks if list contains a cycle.
  * @list: the singly-linked list.
  * Return: 0 or 1.
  */

  int check_cycle(listint_t *list)
  {
          listint_t *first, *last;

          if (list == NULL || list->next == NULL)
                  return (0);

          first = list->next;
          last = list->next->next;

          while (first && last && last->next)
           {
                   if (first == last)
                           return (1);

                   first = first->next;
                   last = last->next->next;
           }

           return (0);
  }
