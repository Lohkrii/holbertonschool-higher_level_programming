#include "lists.h"

/**
 * insert_node - Inserts a new node in a sorted listint_t list
 * @head: pointer to pointer of current head of the list
 * @number: value for the new node
 *
 * Return: pointer to new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL, *tool = NULL;

	if (!head)
	{
		return (NULL);
	}
	current = malloc(sizeof(listint_t));

	if (current == NULL)
	{
		return (NULL);
	}

	current->n = number;

	if (*head == NULL || (*head)->n > number)
	{
		current->next = *head;
		*head = current;
		return (current);
	}

	tool = *head;
	for (;tool->next && tool->next->n < number;)
	{
		tool = tool->next;
	}
	current->next = tool->next;
	tool->next = current;

	return (current);
}
